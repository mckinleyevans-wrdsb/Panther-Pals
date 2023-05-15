#Class Group:
# - Attributes
# - name
# - grade
# - userList
class group:
  def __init__(self, name, grade, userIDs)
  self._name = name
  self._grade = grade
  self._userIDs = userIDs
  return self

class classroom:
  def __init__(self, name, grade, userIDs, teacher)
  self._teacher = teacher
  group.__init__(self, name, grade, userIDs)
  return self

class club:
  def __init__(self, name, grade, userIDs, teacher)
  self._teacher = teacher
  group.__init__(self, name, grade, userIDs)
  return self