from uuid import uuid4
from classes.group import Group
###
class Group_Classroom(Group):
  def __init__(self, group_name, user_list, group_total, is_active = True, department=None):
    self._group_name = group_name
    self._user_list = user_list
    self._group_total = group_total
    self._is_active = is_active
    self._department = department
    self._uuid = str(uuid4())