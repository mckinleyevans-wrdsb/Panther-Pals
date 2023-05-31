from uuid import uuid4
from calendar import Calendar

class Calendar_Post(Calendar):
  def __init__(self, event, text, date):
    self._uuid = str(uuid4())
    self._event = event
    self._text = text
    self._date = date

    
  

