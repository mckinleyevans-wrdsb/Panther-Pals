from classes import announcement
from js import Blob, document, URL
from json import dumps, loads

# TODO: 
# - read & write to list
# - clean up imports
# - comment

# Create a new announcement, and save it to our mock data file
def create(title, text):
  # Get exising file content
  file = open('./mock/announcement.json', 'r')
  file_data = [file.read()]
  all_announcement_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  print(all_announcement_data)

  # Create a new announcement
  new_announcement = announcement.Announcement(title, text)
  print(new_announcement._title)
  new_announcement_json = dumps(new_announcement.__dict__, default=lambda o: o.__dict__)
  new_announcement_json = loads(new_announcement_json)
  
  # Add new announcement to existing content
  all_announcement_data.append(new_announcement_json)
  

  # write all content to file
  file = open('./mock/announcement.json', 'w')
  file.write(str(all_announcement_data))
  file.close()

  # return uuid of new announcement
  return new_announcement._uuid

###### 
# Ignore this for right now
######
def create_and_download():
  new_announcement = announcement.Announcement('Announcement1 title', 'Announcement1 text')
  file = open('./mock/announcement.json', 'a')
  json_data = dumps(new_announcement.__dict__, default=lambda o: o.__dict__).replace('\n')
  file.write(json_data)
  file.close()  

  tag = document.createElement('a')
  tag.href = './mock/announcement.json'
  tag.download = 'announcement.json'
  tag.click()


# Read one or all announcement data from mock file
def read(uuid = None):
  # Fetch announcement class data
  file = open('./mock/announcement.json', 'r')
  file_data = [file.read()]
  all_announcement_data = [loads(idx.replace("'", '"')) for idx in file_data][0]

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
      announcement_as_class = announcement.Announcement(
        title = announcement_data['_title'],
        text = announcement_data['_text']
      )
      announcement_as_class._uuid = announcement_data['_uuid']
      return announcement_as_class
    
  return False