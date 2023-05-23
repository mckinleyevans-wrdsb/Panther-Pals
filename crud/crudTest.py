from crud import announcement, notification
from uuid import UUID

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
  except:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.read() ---")
    
# ensure that our read() function behaves as expected when an UUID is provided
def test_read_with_uuid(test):
  try:
    read_one_result = eval(f"{test['class_to_test'].lower()}.read(\'{test['known_uuid']}\')")
  
    if read_one_result.__class__.__name__ != test['class_to_test']:
      raise Exception()
    print(f"Valid result from {test['class_to_test'].lower()}.read(\'{test['known_uuid'].lower()}\')")
  # Invalid result
  except:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.read(\'{test['known_uuid'].lower()}\') ---")


# ensure that our create() function behaves as expected
def test_create(test):
  params_list = (','.join([f'"{i}"' for i in test['create_params']]))
  try:
    create_result = eval(f"{test['class_to_test'].lower()}.create({params_list})")
  # create a UUID in order to check validity
    UUID(create_result, version=4)
    print(f"Valid result from {test['class_to_test'].lower()}.create({params_list})")
  except:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.create({params_list}) ---")


# ensure that our create_and_download() function behaves as expected
def test_create_and_download(test):
  params_list = (','.join([f'"{i}"' for i in test['create_params']]))
  try:
    create_result = eval(f"{test['class_to_test'].lower()}.create_and_download({params_list})")
    # create a UUID in order to check validity
    UUID(create_result, version=4)
    print(f"Valid result from {test['class_to_test'].lower()}.create_and_download({params_list})")
  except:
    print(f"--- Invalid result from {test['class_to_test'].lower()}.create_and_download({params_list}) ---")

    

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
  }]
  
  
  for test in all_tests:
    test_read(test)
    test_read_with_uuid(test)
    test_create(test)
    test_create_and_download(test)