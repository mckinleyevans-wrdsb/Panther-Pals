from uuid import uuid4

class Calendar():
  def __init__ (self, calendar_posts, event):
    self._uuid = str(uuid4())
    self._calendar_post = calendar_post
    self._event = event
    

class Calendar_post(Calendar):
  def __init__(self, event, text, date):
    self._text = text
    self._date = date
    return self
    
  

