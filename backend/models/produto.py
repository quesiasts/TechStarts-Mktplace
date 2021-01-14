class Produto:
  def __init__(self, id: int = None, name: str = None, description: str = None, price: float = None ) -> None:
    self.id = id
    self.name = name
    self.description = description
    self.price = price