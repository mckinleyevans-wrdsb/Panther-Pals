from datetime import datetime

class announcement():
  def __init__ (self, id, title, text)
  self._id = id
  self._title = title
  self._text = text
  return self

class sports_announcement(announcement):
  def __init__(self, id, title, text, sport)
  self._sport = sport
  announcement.__init__(self, id, title, text)
  return self

class guidence_announcement(announcement):
  def __init__(self, id, title, text, audience)
  self._audience = audience
  announcement.__init__(self, id, title, text)
  return self