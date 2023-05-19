from classes import notification
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_notification_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_notification_data



##################
# Create a new notification
# Save it to our mock data file
##################
def create(title, text):
  # Get exising file content
  all_notification_data = get_existing_data('notification.json')

  # Create a new notification
  new_notification = notification.Notification(
    title=title,
    description=description
    text=text
  )
  new_notification_json = dumps(new_notification.__dict__, default=lambda o: o.__dict__)
  new_notification_json = loads(new_notification_json)
  
  # Add new notification to existing content
  all_notification_data.append(new_notification_json)

  # Write all content to file
  file = open('./mock/notification.json', 'w')
  file.write(str(all_notification_data))
  file.close()

  # return uuid of new notification
  return new_notification._uuid



##################
# Create a new notification
# Download the new version of mock data
##################
def create_and_download(title, text):
  # Get exising file content
  all_notification_data = get_existing_data('notification.json')

  # Create a new notification
  new_notification = notification.Notification(
    title=title,
    description=description
    text=text
  )
  new_notification_json = dumps(new_notification.__dict__, default=lambda o: o.__dict__)
  new_notification_json = loads(new_notification_json)
  
  # Add new notification to existing content
  all_notification_data.append(new_notification_json)

  # Write all content to file
  file = open('./mock/notification.json', 'w')
  file.write(str(all_notification_data))

  file = open('./mock/notification.json', 'r')
  print(file.read())
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_notification_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'notification.json'
  tag.click()
  
  



##################
# If uuid is provided, read one notification from file
# If no uuid is provided, read all notifications from file
##################
def read(uuid = None):
  # Fetch notification class data
  all_notification_data = get_existing_data('notification.json')

  # No uuid provided - return all results
  if uuid == None:
    notification_list = []
    for notification_ in all_notification_data:
      notification_as_class = notification.Notification(
        title = notification_['_title'],
        text = notification_['_text']
      )
      notification_as_class._uuid = notification_['_uuid']
      notification_list.append(notification_as_class)
    return notification_list

  # uuid provided - search for the intended notification object
  else:
    for notification_ in all_notification_data:
      if notification_['_uuid'] == uuid:
        notification_as_class = notification.Notification(
          title = notification_['_title'],
          text = notification_['_text']
        )
        notification_as_class._uuid = notification_['_uuid']
        return notification_as_class
    
  return False