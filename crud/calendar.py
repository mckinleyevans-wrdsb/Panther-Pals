from classes import calendar
from js import Blob, document, URL
from json import dumps, loads

##################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_calendar_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_calendar_data



##################
# Create a new calendar
# Save it to our mock data file
##################
def create(title, text):
  # Get exising file content
  all_calendar_data = get_existing_data('calendar.json')

  # Create a new calendar
  new_calendar = calendar.Calendar(
    calendar_post = calendar_post,
    event = event
  )
  new_calendar_json = dumps(new_calendar.__dict__, default=lambda o: o.__dict__)
  new_calendar_json = loads(new_calendar_json)
  
  # Add new calendar to existing content
  all_calendar_data.append(new_calendar_json)

  # Write all content to file
  file = open('./mock/calendar.json', 'w')
  file.write(str(all_calendar_data))
  file.close()

  # return uuid of new calendar
  return new_calendar._uuid



##################
# Create a new calendar
# Download the new version of mock data
##################
def create_and_download(title, text):
  # Get exising file content
  all_calendar_data = get_existing_data('calendar.json')

  # Create a new calendar
  new_calendar = calendar.Calendar(
    calendar_post = caledar_post,
    event = event
  )
  new_calendar_json = dumps(new_calendar.__dict__, default=lambda o: o.__dict__)
  new_calendar_json = loads(new_calendar_json)
  
  # Add new calendar to existing content
  all_calendar_data.append(new_calendar_json)

  # Write all content to file
  file = open('./mock/calendar.json', 'w')
  file.write(str(all_calendar_data))

  file = open('./mock/calendar.json', 'r')
  file.close()

  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_calendar_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'calendar.json'
  tag.click()
  
  



##################
# If uuid is provided, read one calendar from file
# If no uuid is provided, read all calendars from file
##################
def read(uuid = None):
  # Fetch calendar class data
  all_calendar_data = get_existing_data('calendar.json')

  # No uuid provided - return all results
  if uuid == None:
    calendar_list = []
    for calendar_data in all_calendar_data:
      calendar_as_class = calendar.Calendar(
        calendar_post = calendar_data['_calendar_post'],
        event = calendar_data['_event']
      )
      calendar_as_class._uuid = calendar_data['_uuid']
      calendar_list.append(calendar_as_class)
    return calendar_list

  # uuid provided - search for the intended calendar object
  else:
    for calendar_data in all_calendar_data:
      if calendar_data['_uuid'] == uuid:
        calendar_as_class = calendar.Calendar(
          calendar_post = calendar_data['_calendar_post'],
          event = calendar_data['_event']
        )
        calendar_as_class._uuid = calendar_data['_uuid']
        return calendar_as_class
    
  return False