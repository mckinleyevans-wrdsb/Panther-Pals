class calender_post:
  def __init__ (self, title, text, date, allDay=True, startTime=0, endTime=2400, eventType=None)
  self._title = title
  self._text = text
  self._date = date
  self._allDay = allDay
  if (self._allDay != True):
    self._startTime = startTime
    self._endTime = endTime
  self.eventClass = eventClass
