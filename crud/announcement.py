from classes import announcement
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_announcement_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_announcement_data



##################
# Create a new announcement
# Save it to our mock data file
##################
def create(title, text):
  # Get exising file content
  all_announcement_data = get_existing_data('announcement.json')

  # Create a new announcement
  new_announcement = announcement.Announcement(
    title=title,
    text=text
  )
  new_announcement_json = dumps(new_announcement.__dict__, default=lambda o: o.__dict__)
  new_announcement_json = loads(new_announcement_json)
  
  # Add new announcement to existing content
  all_announcement_data.append(new_announcement_json)

  # Write all content to file
  file = open('./mock/announcement.json', 'w')
  file.write(str(all_announcement_data))
  file.close()

  # return uuid of new announcement
  return new_announcement._uuid



##################
# Create a new announcement
# Download the new version of mock data
##################
def create_and_download(title, text):
  # Get exising file content
  all_announcement_data = get_existing_data('announcement.json')

  # Create a new announcement
  new_announcement = announcement.Announcement(
    title=title,
    text=text
  )
  new_announcement_json = dumps(new_announcement.__dict__, default=lambda o: o.__dict__)
  new_announcement_json = loads(new_announcement_json)
  
  # Add new announcement to existing content
  all_announcement_data.append(new_announcement_json)

  # Write all content to file
  file = open('./mock/announcement.json', 'w')
  file.write(str(all_announcement_data))

  file = open('./mock/announcement.json', 'r')
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_announcement_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'announcement.json'
  tag.click()

  return new_announcement._uuid
  
  



##################
# If uuid is provided, read one announcement from file
# If no uuid is provided, read all announcements from file
##################
def read(uuid = None):
  # Fetch announcement class data
  all_announcement_data = get_existing_data('announcement.json')

  # No uuid provided - return all results
  if uuid == None:
    announcement_list = []
    for announcement_data in all_announcement_data:
      announcement_as_class = announcement.Announcement(
        title = announcement_data['_title'],
        text = announcement_data['_text']
      )
      announcement_as_class._uuid = announcement_data['_uuid']
      announcement_list.append(announcement_as_class)
    return announcement_list

  # uuid provided - search for the intended announcement object
  else:
    for announcement_data in all_announcement_data:
      if announcement_data['_uuid'] == uuid:
        announcement_as_class = announcement.Announcement(
          title = announcement_data['_title'],
          text = announcement_data['_text']
        )
        announcement_as_class._uuid = announcement_data['_uuid']
        return announcement_as_class
    
  return False