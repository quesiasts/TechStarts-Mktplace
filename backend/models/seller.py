class Seller:
  def __init__(self, name: str, email: str, phone: str , id: int = None) -> None:
    self.id = id
    self.name = name
    self.email = email
    self.phone = phone
    
    