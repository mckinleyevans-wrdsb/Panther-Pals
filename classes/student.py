from classes.user import User
from uuid import uuid4

class Student(User):
  def __init__(self, name, pronouns, grade, age):
    self._name = name
    self._pronouns = pronouns
    self._grade = grade
    self._age = age
    self._uuid = str(uuid4())