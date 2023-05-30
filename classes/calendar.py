from uuid import uuid4

class Calender():
  def __init__ (self, calender_post, event):
    self._uuid = str(uuid4())
    self._calender_post = calender_post
    self._event = event
  

