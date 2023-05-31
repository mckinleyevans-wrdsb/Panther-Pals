from classes import user
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_user_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_user_data



##################
# Create a new user
# Save it to our mock data file
##################
def create(name, pronouns):
  # Get exising file content
  all_user_data = get_existing_data('user.json')

  # Create a new user
  new_user = user.User(
    name = name,
    pronouns = pronouns
  )
  new_user_json = dumps(new_user.__dict__, default=lambda o: o.__dict__)
  new_user_json = loads(new_user_json)
  
  # Add new user to existing content
  all_user_data.append(new_user_json)

  # Write all content to file
  file = open('./mock/user.json', 'w')
  file.write(str(all_user_data))
  file.close()

  # return uuid of new user
  return new_user._uuid



##################
# Create a new user
# Download the new version of mock data
##################
def create_and_download(name, pronouns):
  # Get exising file content
  all_user_data = get_existing_data('user.json')
  # Create a new user
  new_user = user.User(
    name = name,
    pronouns = pronouns
  )
  new_user_json = dumps(new_user.__dict__, default=lambda o: o.__dict__)
  new_user_json = loads(new_user_json)
  
  # Add new user to existing content
  all_user_data.append(new_user_json)
  # Write all content to file
  file = open('./mock/user.json', 'w')
  file.write(str(all_user_data))

  file = open('./mock/user.json', 'r')
  file.close()
  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_user_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'user.json'
  tag.click()
  
  return new_user._uuid



##################
# If uuid is provided, read one user from file
# If no uuid is provided, read all users from file
##################
def read(uuid = None):
  # Fetch user class data
  all_user_data = get_existing_data('user.json')
  # No uuid provided - return all results
  if uuid == None:
    user_list = []
    for user_data in all_user_data:
      user_as_class = user.User(
        name = user_data['_name'],
        pronouns = user_data['_pronouns']
      )
      user_as_class._uuid = user_data['_uuid']
      user_list.append(user_as_class)
    return user_list

  # uuid provided - search for the intended user object
  else:
    for user_data in all_user_data:
      if user_data['_uuid'] == uuid:
        user_as_class = user.User(
          name = user_data['_name'],
          pronouns = user_data['_pronouns']
        )
        user_as_class._uuid = user_data['_uuid']
        return user_as_class
    
  return False