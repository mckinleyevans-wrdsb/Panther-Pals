from uuid import uuid4


#Class Group:
# - Attributes
# - name
# - list of users 
# - Total numbers of users to be added to group
# - Is the group active
# - id (used from user) for staff
class Group():
  def __init__(self, group_name, user_list, group_total, is_active = 'True'):
    self._group_name = group_name
    self._user_list = user_list
    self._group_total = group_total
    self._is_active = is_active
    self._uuid = str(uuid4())

class Classroom(Group):
  def __init__(self, group_name, user_list, group_total, is_active = 'True', department='None'):
    self._department = department
    Group.__init__(self, group_name, user_list, group_total, is_active = 'True')

class Club(Group):
  def __init__(self, group_name, user_list, group_total, is_active = 'True', club_type='None'):
    self._club_type = club_type
    Group.__init__(self, group_name, user_list, group_total, is_active = 'True')
