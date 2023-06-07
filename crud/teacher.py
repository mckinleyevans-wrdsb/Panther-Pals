from classes import teacher
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_teacher_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_teacher_data



##################
# Create a new teacher
# Save it to our mock data file
##################
def create(name, pronouns, department):
  # Get exising file content
  all_teacher_data = get_existing_data('teacher.json')

  # Create a new teacher
  new_teacher = teacher.Teacher(
    name = name,
    pronouns = pronouns,
    department = department
  )
  new_teacher_json = dumps(new_teacher.__dict__, default=lambda o: o.__dict__)
  new_teacher_json = loads(new_teacher_json)
  
  # Add new teacher to existing content
  all_teacher_data.append(new_teacher_json)

  # Write all content to file
  file = open('./mock/teacher.json', 'w')
  file.write(str(all_teacher_data))
  file.close()

  # return uuid of new teacher
  return new_teacher._uuid



##################
# Create a new teacher
# Download the new version of mock data
##################
def create_and_download(name, pronouns, department):
  # Get exising file content
  all_teacher_data = get_existing_data('teacher.json')
  # Create a new teacher
  new_teacher = teacher.Teacher(
    name = name,
    pronouns = pronouns,
    department = department
  )
  new_teacher_json = dumps(new_teacher.__dict__, default=lambda o: o.__dict__)
  new_teacher_json = loads(new_teacher_json)
  # Add new teacher to existing content
  all_teacher_data.append(new_teacher_json)
  # Write all content to file
  file = open('./mock/teacher.json', 'w')
  file.write(str(all_teacher_data))

  file = open('./mock/teacher.json', 'r')
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_teacher_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'teacher.json'
  tag.click()

  # return uuid of new teacher
  return new_teacher._uuid
  

##################
# If uuid is provided, read one teacher from file
# If no uuid is provided, read all teachers from file
##################
def read(uuid = None):
  # Fetch teacher class data
  all_teacher_data = get_existing_data('teacher.json')

  # No uuid provided - return all results
  if uuid == None:
    teacher_list = []
    for teacher_data in all_teacher_data:
      teacher_as_class = teacher.Teacher(
        name = teacher_data['_name'],
        pronouns = teacher_data['_pronouns'],
        department = teacher_data['_department']
      )
      teacher_as_class._uuid = teacher_data['_uuid']
      teacher_list.append(teacher_as_class)
    return teacher_list

  # uuid provided - search for the intended teacher object
  else:
    for teacher_data in all_teacher_data:
      if teacher_data['_uuid'] == uuid:
        teacher_as_class = teacher.Teacher(
          name = teacher_data['_name'],
          pronouns = teacher_data['_pronouns'],
          department = teacher_data['_department']

        )
        teacher_as_class._uuid = teacher_data['_uuid']
        return teacher_as_class
    
  return False