class Notification():
  def __init__ (self, title, text, description):
    self._title = title
    self._description = description
    self._text = text
    self._uuid = uuid.uuid4()
    return self

