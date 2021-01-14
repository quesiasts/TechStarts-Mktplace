class BaseController:
  def __init__(self, dao):
    self.__dao = dao

  def create(self, model: object ) -> None:
    return self.__dao.create(model)
      

  def read_all(self) -> list:
    return self.__dao.read_all()    
        
  
  def read_by_id(self, id:int) -> object:
    return self.__dao.read_by_id(id)    
      

  def update(self, model: object) -> None:
    self.__dao.update(model)
      

  def delete(self, id:int):
    self.__dao.delete(id)
   
