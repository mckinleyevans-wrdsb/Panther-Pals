import users
import uuid

#Class Group:
# - Attributes
# - name
# - list of users
# - Total numbers of users to be added to group
# - Is the group active
# - id (used from user) for staff
class Group():
  #constructor
  def __init__(self, group_name, user_list, group_total, is_active = True):
    self._group_name = group_name
    self._user_list = user_list
    self._group_total = group_total
    self._is_active = is_active
    self._uuid = uuid.uuid4()
    return self

class Classroom():
  def __init__(self, group_name, user_list, group_total, is_active = True, department):
    self._department = department
    group.__init__(self, group_name, user_list, group_total, is_active = True):
    return self

class Club():
  def __init__(self, group_name, user_list, group_total, is_active = True, club_type):
    self._club_type = club_type
    group.__init__self, group_name, user_list, group_total, is_active = True):
    return self
