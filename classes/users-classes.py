class user:
 def __init__(self, id, name, pronouns, isTeacher=False, grade=9, age=None adminStatus=1)
  self._id = id
  self._name = name
  self._pronouns
  self._isTeacher = isTeacher
  if (self._isTeacher == False):
    self._grade = grade
    self._age = age
  self._adminStatus = adminStatus