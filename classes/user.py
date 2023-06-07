from uuid import uuid4
#
class User:
 def __init__ (self, name, pronouns):
    self._uuid = str(uuid4())
    self._name = name
    self._pronouns = pronouns

class Student(User):
  def __init__(self, name, pronouns, grade, age):
    self._grade = grade
    self._age = age
    User.__init__(self, name, pronouns)
    return self