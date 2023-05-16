from datetime import datetime

class Announcement():
  def __init__ (self, uuid, title, text):
    self._title = title
    self._text = text
  def staff_id (self, uuid):
    uuid.uuid4()
  return self

class Sports_announcement(announcement):
  def __init__(self, id, title, text, sport):
    self._sport = sport
  announcement.__init__(self, id, title, text)

class Guidence_announcement(announcement):
  def __init__(self, id, title, text, audience):
    self._audience = audience
  announcement.__init__(self, id, title, text)
  