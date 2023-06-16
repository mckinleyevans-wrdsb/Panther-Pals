import domControl
from crud import announcement
# builds an announcement and adds it to the html


def build_announcement(title,text):
  announcement_content = f'''

  <div class = 'announcement'>
    <h4>
      {title}
    </h4>
    
    <p>
      {text}
    </p>
  </div>
  '''
  
  return announcement_content
  

# use announcement-crud.read() to get all of the current announcements
all_announcements = announcement.read()
print(all_announcements)


announcement_box_content = "<div class = 'announcement-box'>"

# loop and make an announcement for each
for one_announcement in all_announcements:
  announcement_box_content += build_announcement(
    title = one_announcement._title,
    text = one_announcement._text
  )


announcement_box_content += '</div>'

  
# build announcement box
domControl.attach_content_to_element('pyscript-announcements', domControl.build_element(
  type='div',
  class_name='announcement-box',
  id='announcement', 
  content=announcement_box_content,))
  