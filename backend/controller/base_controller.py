from .log_controller import LogController
log = LogController()

class BaseController:
  def __init__(self, dao, type_entity):
    self.__dao = dao
    self.type_entity = type_entity

  def create(self, model: object) -> None:    
    self.__dao.create(model)
    log.create(f"{model.name} criado(a)")
      

  def read_all(self) -> list:
    result = self.__dao.read_all()
    log.create(f"{self.type_entity} listados")
    return result
        
  
  def read_by_id(self, id:int) -> object:
    result = self.__dao.read_by_id(id)
    log.create(f"{self.type_entity} lido")
    return result   
      

  def update(self, model: object) -> None:    
    self.__dao.update(model)
    log.create(f"{model.name} atualizado(a)")
      

  def delete(self, id:int):
    self.__dao.delete(id)
    log.create(f"{self.type_entity} deletado(a)")
   
