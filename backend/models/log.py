class Log:
  def __init__(self, description: str = None, id: int = None, datetime: str = None) -> None:
    self.id = id
    self.datetime = datetime    
    self.description = description