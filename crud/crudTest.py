# For each new class of mock data:

# 1) Add a record to the `all_tests` list at the bottom of this list
#   - class_to_test is the class name, capitalized
#   - known_uuid is the uuid of a record in mock/<classname>.json
#   - create_params is a list of input params when creating the class instance

# 2) Update index.html to load:
#   ,'./classes/<classname>.py'
#   ,'./crud/<classname>.py'
#   ,'./mock/<classname>.json'

# 3) After running the create_and_download() function one time, use the downloaded file to update <classname>.json.  Use the uuid from this file to update create_params



from uuid import UUID
from crud import announcement, notification, user, group, calendar, calendar_post

DO_TESTS = True

# ensure that our read() function behaves as expected when no UUID is provided
def test_read(test):
  try:
    read_all_result = eval(f"{test['class_to_test'].lower()}.read()")
  
    for one_result in read_all_result:
      if one_result.__class__.__name__ != test['class_to_test']:
        raise Exception()
    # Valid results
    print(f"Valid result from {test['class_to_test'].lower()}.read()")
  # Invalid result
  except Exception as e:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.read() ---", e)
    
# ensure that our read() function behaves as expected when an UUID is provided
def test_read_with_uuid(test):
  try:
    read_one_result = eval(f"{test['class_to_test'].lower()}.read(\'{test['known_uuid']}\')")
  
    if read_one_result.__class__.__name__ != test['class_to_test']:
      raise Exception()
    print(f"Valid result from {test['class_to_test'].lower()}.read(\'{test['known_uuid'].lower()}\')")
  # Invalid result
  except Exception as e:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.read(\'{test['known_uuid'].lower()}\') ---", e)


# ensure that our create() function behaves as expected
def test_create(test):
  params_list = (','.join([f'"{i}"' for i in test['create_params']]))
  try:
    create_result = eval(f"{test['class_to_test'].lower()}.create({params_list})")
  # create a UUID in order to check validity
    UUID(create_result, version=4)
    print(f"Valid result from {test['class_to_test'].lower()}.create({params_list})")
  except Exception as e:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.create({params_list}) ---", e)


# ensure that our create_and_download() function behaves as expected
def test_create_and_download(test):
  params_list = (','.join([f'"{i}"' for i in test['create_params']]))
  try:
    create_result = eval(f"{test['class_to_test'].lower()}.create_and_download({params_list})")
    # create a UUID in order to check validity
    UUID(create_result, version=4)
    print(f"Valid result from {test['class_to_test'].lower()}.create_and_download({params_list})")
  except Exception as e:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.create_and_download({params_list}) ---", e)

    

# #print(notification.create('some title','some description', 'some text'))
# #print(notification.create_and_download('some title', 'some description', 'some text'))
# #print(notification.read('a43f8af0-b8ed-46fc-b771-a66913b6b250'))
# #print(notification.read())


if DO_TESTS:
  all_tests = [{
    'class_to_test': 'Announcement',
    'known_uuid': '9433d0a4-cb9a-450b-8278-a1bfd87fc2a3',
    'create_params': ['some title', 'some text']
  }, {
    'class_to_test': 'Notification',
    'known_uuid': 'a43f8af0-b8ed-46fc-b771-a66913b6b250',
    'create_params': ['some title', 'some description', 'some text']
  }, {
    'class_to_test': 'User',
    'known_uuid': 'a43f8af0-b8ed-46fc-b771-a66913b6b250',
    'create_params': ['some name', 'some pronoun']
  }, {
    'class_to_test': 'Group',
    'known_uuid': '9433d0a4-cb9a-450b-8278-a1bfd87fc2a3',
    'create_params': ['Group Name', 'List of users', 'Number of people in group', 'True']
  }, {
    'class_to_test': 'Calendar_Post',
    'known_uuid': '919e48a0-217b-49cb-9eb6-ee5b9e8e306f',
    'create_params': ['Some event','Some text','2023-06-30']
  }, {
    'class_to_test': 'Calendar',
    'known_uuid': '5db4eade-ddaa-4e0c-ad55-0d85c2f53068',
    'create_params': ['[919e48a0-217b-49cb-9eb6-ee5b9e8e306f]','Some Event']
  }]
  
  
  for test in all_tests:
    test_read(test)
    test_read_with_uuid(test)
    test_create(test)
    test_create_and_download(test)
