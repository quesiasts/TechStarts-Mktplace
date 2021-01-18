class Log:
  def __init__(self, description: str, date: str, hour: str, action: str, id: str = None) -> None:
    self.id = id
    self.date = date
    self.hour = hour    
    self.description = description
    self.action = action
  
  @property
  def id(self):
    return self.__id

  @property
  def description(self):
    return self.__description
  
  @property
  def date(self):
    return self.__date
  
  @property
  def hour(self):
    return self.__hour
  
  @property
  def action(self):
    return self.__action

  @id.setter
  def id(self, id):
      self.__id = id
  
  @description.setter
  def description(self, description):
    self.__description = description

  @date.setter
  def date(self, date):
    self.__date = date
  
  @hour.setter
  def hour(self, hour):
    self.__hour = hour

  @action.setter
  def action(self, action):
    self.__action = action