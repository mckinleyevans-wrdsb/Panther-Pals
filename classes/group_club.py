from classes.group import Group
from uuid import uuid4

class Group_Club(Group):
  def __init__(self, group_name, user_list, group_total, is_active = True, club_type=None):
    self._group_name = group_name
    self._user_list = user_list
    self._group_total = group_total
    self._is_active = is_active
    self._club_type = club_type
    self._uuid = str(uuid4())
