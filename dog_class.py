class Dog:
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
  def __repr__(self):
    return f"{self.name} - {self.breed}"
  def __str__(self):
    return str(self.__repr__())
