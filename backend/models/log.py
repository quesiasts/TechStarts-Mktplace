class Log:
  def __init__(self, description: str, datetime: str = None, id: int = None) -> None:
    self.id = id
    self.datetime = datetime    
    self.description = description