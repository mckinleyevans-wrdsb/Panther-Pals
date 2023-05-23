from classes import group
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_group_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_group_data


##################
# Create a new group
# Save it to our mock data file
##################
def create(group_name, user_list, group_total, is_active = True):
  # Get exising file content
  all_group_data = get_existing_data('group.json')
  
  # Create a new group
  new_group = group.Group(
    group_name=group_name,
    user_list=user_list,
    group_total=group_total,
    is_active=is_active,
  )
  new_group_json = dumps(new_group.__dict__, default=lambda o: o.__dict__)
  new_group_json = loads(new_group_json)
  
  # Add new group to existing content
  all_group_data.append(new_group_json)

  # Write all content to file
  file = open('./mock/group.json', 'w')
  file.write(str(all_group_data))
  file.close()
  
  # return uuid of new group
  return new_group._uuid



##################
# Create a new group
# Download the new version of mock data
##################
def create_and_download(group_name, user_list, group_total, is_active = True):
  # Get exising file content
  all_group_data = get_existing_data('group.json')
  
  # Create a new group
  new_group = group.Group(
    group_name=group_name,
    user_list=user_list,
    group_total=group_total,
    is_active=is_active,
  )
  new_group_json = dumps(new_group.__dict__, default=lambda o: o.__dict__)
  new_group_json = loads(new_group_json)
  
  # Add new group to existing content
  all_group_data.append(new_group_json)

  # Write all content to file
  file = open('./mock/group.json', 'w')
  file.write(str(all_group_data))

  file = open('./mock/group.json', 'r')
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_group_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'group.json'
  tag.click()
  
  



##################
# If uuid is provided, get one group from file
# If no uuid is provided, read all groups from file
##################
def read(uuid = None):
  # Fetch group class data
  all_group_data = get_existing_data('group.json')

  # No uuid provided - return all results
  if uuid == None: group_as_class
    group_list = []
    for group_data in all_group_data:
      group_as_class = group.Group(
        group_name = group_data['_group_name'],
        user_list = group_data['_user_list'],
        group_total = group_data['_group_total']
        is_active = group_data['_is_active']
      )
      group_as_class._uuid = group_data['_uuid']
      group_list.append(group_as_class)
    return group_list

  # uuid provided - search for the intended group object
  else:
    for group_data in all_group_data:
      if group_data['_uuid'] == uuid:
        group_as_class = group.Group(
          group_name = group_data['_group_name'],
          user_list = group_data['_user_list'],
          group_total = group_data['_group_total']
          is_active = group_data['_is_active']
        )
        group_as_class._uuid = group_data['_uuid']
        return group_as_class
    
  return False