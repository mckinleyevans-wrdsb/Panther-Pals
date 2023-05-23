from classes import group
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_group_club_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_group_club_data



##################
# Create a new group
# Save it to our mock data file
##################
def create(group_name, user_list, group_total, is_active = True, club_type):
  # Get exising file content
  all_group_club_data = get_existing_data('group_club.json')
  
  # Create a new group
  new_group_club = group_club.Group_club(
    group_name=group_name,
    user_list=user_list,
    group_total=group_total,
    is_active=is_active,
    club_type=club_type,
  )
  new_group_club_json = dumps(new_group_club.__dict__, default=lambda o: o.__dict__)
  new_group_club_json = loads(new_group_club_json)
  
  # Add new group to existing content
  all_group_club_data.append(new_group_club_json)

  # Write all content to file
  file = open('./mock/group_club.json', 'w')
  file.write(str(all_group_club_data))
  file.close()
  
  # return uuid of new group
  return new_group_club._uuid



##################
# Create a new group
# Download the new version of mock data
##################
def create_and_download(group_name, user_list, group_total, is_active = True, club_type):
  # Get exising file content
  all_group_club_data = get_existing_data('group_club.json')
  
  # Create a new group
  new_group = group.Group(
    group_name=group_name,
    user_list=user_list,
    group_total=group_total,
    is_active=is_active,
    club_type=club_type,
  )
  new_group_club_json = dumps(new_group_club.__dict__, default=lambda o: o.__dict__)
  new_group_club_json = loads(new_group_club_json)
  
  # Add new group to existing content
  all_group_club_data.append(new_group_club_json)

  # Write all content to file
  file = open('./mock/group_club.json', 'w')
  file.write(str(all_group_club_data))

  file = open('./mock/group_club.json', 'r')
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_group_club_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'group_club.json'
  tag.click()
  
  



##################
# If uuid is provided, get one group from file
# If no uuid is provided, read all groups from file
##################
def read(uuid = None):
  # Fetch group class data
  all_group_club_data = get_existing_data('group_club.json')

  # No uuid provided - return all results
  if uuid == None: group_club_as_class
    group_club_list = []
    for group_club_data in all_group_club_data:
      group_club_as_class = group_club.Group_club(
        group_name = group_club_data['_group_name'],
        user_list = group_club_data['_user_list'],
        group_total = group_club_data['_group_total']
        is_active = group_club_data['_is_active']
        club_type = group_club_data['_club_type']
      )
      group_club_as_class._uuid = group_club_data['_uuid']
      group_club_list.append(group_club_as_class)
    return group_club_list

  # uuid provided - search for the intended group object
  else:
    for group_club_data in all_group_club_data:
      if group_club_data['_uuid'] == uuid:
        group_club_as_class = group_club.Group_club(
          group_name = group_club_data['_group_name'],
          user_list = group_club_data['_user_list'],
          group_total = group_club_data['_group_total']
          is_active = group_club_data['_is_active']
          club_type = group_club_data['_club_type']
        )
        group_club_as_class._uuid = group_club_data['_uuid']
        return group_club_as_class
    
  return False