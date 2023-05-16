<<<<<<< HEAD
class User:
 def __init__(self, id, name, pronouns):
    self._id = id
    self._name = name
    self._pronouns = pronouns
=======
class user:
 def __init__(self, id, name, pronouns)
  self._id = id
  self._name = name
  self._pronouns = pronouns
>>>>>>> a97f0261d8e894b5ec1432214757369ad84603b7
  return self

class Teacher(user):
  def __init__(self, id, name, pronouns, department):
    self._department = department
  user.__init__(self, id, name, pronouns)
  return self

class Student(user):
  def __init__(self, id, name, pronouns, grade, age):
    self._grade = grade
    self._age = age
  user.__init__(self, id, name, pronouns)
  return self