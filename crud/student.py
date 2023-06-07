from classes import student
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_student_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_student_data



##################
# Create a new student
# Save it to our mock data file
##################
def create(name, pronouns, grade, age):
  # Get exising file content
  student = get_existing_data('student.json')

  # Create a new student
  new_student = user.Student(
    name = name,
    pronouns = pronouns,
    grade = grade,
    age = age 
  )
  new_student_json = dumps(new_student.__dict__, default=lambda o: o.__dict__)
  new_student_json = loads(new_student_json)
  
  # Add new student to existing content
  all_student_data.append(new_student_json)

  # Write all content to file
  file = open('./mock/student.json', 'w')
  file.write(str(all_student_data))
  file.close()

  # return uuid of new student
  return new_student._uuid



##################
# Create a new student
# Download the new version of mock data
##################
def create_and_download(name, pronouns, grade, age):
  # Get exising file content
  all_student_data = get_existing_data('student.json')

  # Create a new student
  new_student = user.Student(
    name = name,
    pronouns = pronouns, 
    grade = grade, 
    age = age
  )
  new_student_json = dumps(new_student.__dict__, default=lambda o: o.__dict__)
  new_student_json = loads(new_student_json)
  
  # Add new student to existing content
  all_student_data.append(new_student_json)

  # Write all content to file
  file = open('./mock/student.json', 'w')
  file.write(str(all_student_data))

  file = open('./mock/student.json', 'r')
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_student_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'student.json'
  tag.click()
  
  



##################
# If uuid is provided, read one student from file
# If no uuid is provided, read all students from file
##################
def read(uuid = None):
  # Fetch student class data
  all_student_data = get_existing_data('student.json')

  # No uuid provided - return all results
  if uuid == None:
    student_list = []
    for student_data in all_student_data:
      student_as_class = user.Student(
        name = student_data['_name'],
        pronouns = student_data['_pronouns'], 
        grade = student_data['_grade'],
        age = student_data['_age']
      )
      student_as_class._uuid = student_data['_uuid']
      student_list.append(student_as_class)
    return student_list

  # uuid provided - search for the intended student object
  else:
    for student_data in all_student_data:
      if student_data['_uuid'] == uuid:
        student_as_class = user.Student(
          name = student_data['_name'],
          pronouns = student_data['_pronouns'], 
          grade = student_data['_grade'],
          age = student_data['_age']
        )
        student_as_class._uuid = student_data['_uuid']
        return student_as_class
    
  return False