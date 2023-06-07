from uuid import uuid4
from classes.user import User
  
class Teacher(User):
  def __init__(self, name, pronouns, department):
    self._name = name
    self._pronouns = pronouns
    self._department = department
    self._uuid = str(uuid4())
  