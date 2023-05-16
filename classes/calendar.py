class Calender():
  def __init__ (self, calender_posts, text, date):
    self._uuid = uuid.uuid4()
    self._calender_posts = calender_posts
    self._text = text
    self._date = date
    return self
  

