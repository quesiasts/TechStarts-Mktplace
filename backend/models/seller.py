class Seller:
    def _init_(self, name:str, phone:str, email:str, id:int=None):
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__email = email
        
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email
        
    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email
    
    