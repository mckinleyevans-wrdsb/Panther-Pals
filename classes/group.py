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
    self.groupName = groupName
    self.userList = userList
    self.groupTotal = groupTotal
    self.isActive = isActive
    self.staff_sponsor_id = staff_id  



  