class User:
 def __init__(self, name, pronouns):
    self._uuid = uuid.uuid4()
    self._name = name
    self._pronouns = pronouns
    return self

class Teacher(User):
  def __init__(self, name, pronouns, department):
    self._department = department
    User.__init__(self, name, pronouns)
    return self

class Student(User):
  def __init__(self, name, pronouns, grade, age):
    self._grade = grade
    self._age = age
    User.__init__(self, name, pronouns)
    return self