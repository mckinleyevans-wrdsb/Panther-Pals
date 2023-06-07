from uuid import uuid4

class Calendar():
  def __init__ (self, calendar_posts, event):
    self._uuid = str(uuid4())
    self._calendar_posts = calendar_posts
    self._event = event