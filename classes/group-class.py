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
  def __init__(self, group_name, user_list, group_total, is_active = True, staff_id)
    self._group_name = group_nameame
    self._user_list = user_list
    self._group_total = group_total
    self._is_active = is_active
    self._staff_sponsor_id = staff_id  
    return self

class classroom:
  def __init__(self, group_name, user_list, group_total, is_active = True, staff_id, department)
  self._department = department
  group.__init__(self, group_name, user_list, group_total, is_active = True, staff_id)
  return self

class club:
  def __init__(self, group_name, user_list, group_total, is_active = True, staff_id, club_type)
  self._club_type = club_type
  group.__init__self, group_name, user_list, group_total, is_active = True, staff_id)
  return self