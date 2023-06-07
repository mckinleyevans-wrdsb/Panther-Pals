from classes import calendar_post
from js import Blob, document, URL
from json import dumps, loads

#####################
# Fetch all existing data from mock file
##################
def get_existing_data(filename):
  file = open(f'./mock/{filename}', 'r')
  file_data = [file.read()]
  all_calendar_post_data = [loads(idx.replace("'", '"')) for idx in file_data][0]
  file.close()
  return all_calendar_post_data

def create(event, text, date):
  # Get exising file content
  all_calendar_post_data = get_existing_data('calendar_post.json')

  # Create a new calendar
  new_calendar_post = calendar_post.Calendar_Post(
    event=event,
    text=text,
    date=date
  )
  
  new_calendar_post_json = dumps(new_calendar_post.__dict__, default=lambda o: o.__dict__)
  new_calendar_post_json = loads(new_calendar_post_json)
  
  # Add new calendar to existing content
  all_calendar_post_data.append(new_calendar_post_json)

  # Write all content to file
  file = open('./mock/calendar_post.json', 'w')
  file.write(str(all_calendar_post_data))
  file.close()

  # return uuid of new calendar
  return new_calendar_post._uuid  

def create_and_download(event, text, date):
  # Get exising file content
  all_calendar_post_data = get_existing_data('calendar_post.json')
  
  # Create a new calendar
  new_calendar_post = calendar_post.Calendar_Post(
    event=event,
    text=text,
    date=date
  )
  new_calendar_post_json = dumps(new_calendar_post.__dict__, default=lambda o: o.__dict__)
  new_calenda_postr_json = loads(new_calendar_post_json)
  
  # Add new calendar to existing content
  all_calendar_post_data.append(new_calendar_post_json)
  
  # Write all content to file
  file = open('./mock/calendar_post.json', 'w')
  file.write(str(all_calendar_post_data))
  file.close()
  
  # Download mock data file
  tag = document.createElement('a')
  blob = Blob.new([all_calendar_post_data], {type: "application/json"})
  tag.href = URL.createObjectURL(blob)
  tag.download = 'calendar_post.json'
  tag.click()
  
  # return uuid of new calendar
  return new_calendar_post._uuid  



##################
# If uuid is provided, read one calendar from file
# If no uuid is provided, read all calendars from file
##################
def read(uuid = None):
  all_calendar_post_data = get_existing_data('calendar_post.json')

  # No uuid provided - return all results
  if uuid == None:
    calendar_post_list = []
    for calendar_post_data in all_calendar_post_data:
      calendar_post_as_class = calendar_post.Calendar_Post(
        event = calendar_post_data['_event'],
        text = calendar_post_data['_text'],
        date = calendar_post_data['_date']
      )
      calendar_post_as_class._uuid = calendar_post_data['_uuid']
      calendar_post_list.append(calendar_post_as_class)
    return calendar_post_list

  # uuid provided - search for the intended calendar object
  else:
    for calendar_post_data in all_calendar_post_data:
      if calendar_post_data['_uuid'] == uuid:
        calendar_post_as_class = calendar_post.Calendar_Post(
          event = calendar_post_data['_event'],
          text = calendar_post_data['_text'],
          date = calendar_post_data['_date']
        )
        calendar_post_as_class._uuid = calendar_post_data['_uuid']
        return calendar_post_as_class
    
  return False