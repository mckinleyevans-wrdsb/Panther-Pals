from uuid import uuid4

class User:
 def __init__ (self, name, pronouns):
    self._uuid = str(uuid4())
    self._name = name
    self._pronouns = pronouns