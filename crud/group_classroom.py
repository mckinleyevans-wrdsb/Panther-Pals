from classes import group_classroom
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_group_classroom_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_group_classroom_data



##################
# Create a new group
# Save it to our mock data file
##################
def create(group_name, user_list, group_total, is_active = True, department=None):
  # Get exising file content
  all_group_classroom_data = get_existing_data('group_classroom.json')
  # Create a new group
  new_group_classroom = group_classroom.Group_Classroom(
    group_name=group_name,
    user_list=user_list,
    group_total=group_total,
    is_active=is_active,
    department=department
  )
  new_group_classroom_json = dumps(new_group_classroom.__dict__, default=lambda o: o.__dict__)
  new_group_classroom_json = loads(new_group_classroom_json)
  
  # Add new group to existing content
  all_group_classroom_data.append(new_group_classroom_json)

  # Write all content to file
  file = open('./mock/group_classroom.json', 'w')
  file.write(str(all_group_classroom_data))
  file.close()
  
  # return uuid of new group
  return new_group_classroom._uuid



##################
# Create a new group
# Download the new version of mock data
##################
def create_and_download(group_name, user_list, group_total, is_active = True, department=None):
  # Get exising file content
  all_group_classroom_data = get_existing_data('group_classroom.json')
  
  # Create a new group
  new_group_classroom = group_classroom.Group_Classroom(
    group_name=group_name,
    user_list=user_list,
    group_total=group_total,
    is_active=is_active,
    department=department,
  )
  new_group_classroom_json = dumps(new_group_classroom.__dict__, default=lambda o: o.__dict__)
  new_group_classroom_json = loads(new_group_classroom_json)
  
  # Add new group to existing content
  all_group_classroom_data.append(new_group_classroom_json)

  # Write all content to file
  file = open('./mock/group_classroom.json', 'w')
  file.write(str(all_group_classroom_data))

  file = open('./mock/group_classroom.json', 'r')
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_group_classroom_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'group_classroom.json'
  tag.click()

  return new_group_classroom._uuid
  
  



##################
# If uuid is provided, get one group from file
# If no uuid is provided, read all groups from file
##################
def read(uuid = None):
  # Fetch group class data
  all_group_classroom_data = get_existing_data('group_classroom.json')

  # No uuid provided - return all results
  if uuid == None:
    group_classroom_list = []
    for group_classroom_data in all_group_classroom_data:
      group_classroom_as_class = group_classroom.Group_Classroom(
        group_name = group_classroom_data['_group_name'],
        user_list = group_classroom_data['_user_list'],
        group_total = group_classroom_data['_group_total'],
        is_active = group_classroom_data['_is_active'],
        department = group_classroom_data['_department']
      )
      group_classroom_as_class._uuid = group_classroom_data['_uuid']
      group_classroom_list.append(group_classroom_as_class)
    return group_classroom_list

  # uuid provided - search for the intended group object
  else:
    for group_classroom_data in all_group_classroom_data:
      if group_classroom_data['_uuid'] == uuid:
        group_classroom_as_class = group_classroom.Group_Classroom(
          group_name = group_classroom_data['_group_name'],
          user_list = group_classroom_data['_user_list'],
          group_total = group_classroom_data['_group_total'],
          is_active = group_classroom_data['_is_active'],
          department = group_classroom_data['_department']
        )
        group_classroom_as_class._uuid = group_classroom_data['_uuid']
        return group_classroom_as_class
    
  return False