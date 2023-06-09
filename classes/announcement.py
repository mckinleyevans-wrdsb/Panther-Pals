from uuid import uuid4
#
class Announcement():
  def __init__ (self, title, text):
    self._uuid = str(uuid4())
    self._title = title

    self._text = text 
    return self


class Sports_announcement(Announcement):
  def __init__(self, title, text, sport):
    self._sport = sport
    Announcement.__init__(self, title, text)
    return self
    

class Guidance_announcement(Announcement):
  def __init__(self, title, text, audience):
    self._audience = audience
    Announcement.__init__(self, title, text)
    return self
  