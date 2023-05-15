import users

#Class Group:
# - Attributes
# - name
# - list of users
# - Total numbers of users to be added to group
# - Is the group active
# - id (used from user) for staff
class group():
  #constructor
  def __init__(self, groupName, userList, grouptTotal, isActive = True, staff_id)
    self._groupName = groupName
    self._userList = userList
    self._groupTotal = groupTotal
    self._isActive = isActive
    self._staff_sponsor_id = staff_id  
    return self

class classroom:
  def __init__(self, groupName, userList, grouptTotal, isActive = True, staff_id, department)
  self._department = department
  group.__init__(self, groupName, userList, grouptTotal, isActive = True, staff_id)
  return self

class club:
  def __init__(self, groupName, userList, grouptTotal, isActive = True, staff_id, clubType)
  self._clubType = clubType
  group.__init__(self, groupName, userList, grouptTotal, isActive = True, staff_id)
  return self