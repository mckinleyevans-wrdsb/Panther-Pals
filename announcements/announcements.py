import domControl

# builds an announcement and adds it to the html
def build_announcement():

  announcement_content = '''
  <div class = 'announcement'>
    <h4>
      Announcement Title
    </h4>
    
    <p>
      This is the announcement description.
    </p>
  </div>
  '''
  
  return announcement_content
  

# amount of announcements currently
num_of_announcements = 5

announcement_box_content = "<div class = 'announcement-box'>"

# loop and make an announcement for each
for i in range(num_of_announcements):

  announcement_box_content += build_announcement()
  
# build announcement box
domControl.attach_content_to_element('pyscript-announcements', domControl.build_element(
  type='div',
  class_name='announcement-box',
  id='announcement', 
  content=announcement_box_content,))
  

#announcement = input('What announcment do you want to make')

