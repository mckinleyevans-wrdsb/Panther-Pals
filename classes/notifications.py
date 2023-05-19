class Notification():
  def __init__ (self, title, text, description):
    self._uuid = uuid.uuid4()
    self._title = title
    self._description = description
    self._text = text
    return self

