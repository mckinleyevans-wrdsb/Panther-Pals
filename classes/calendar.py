from uuid import uuid4

class Calendar():
  def __init__ (self, calendar_post, event):
    self._uuid = str(uuid4())
    self._calendar_post = calendar_post
    self._event = event
  

