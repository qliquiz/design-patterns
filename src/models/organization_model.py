from src.abstract_reference import abstract_reference

class organization_model(abstract_reference):
    __INN = None
    __BIC = None
    __score = None
    __type_of_ownership = None
    __settings = None

    def __init__(self, settings, name:str = 'organization'):
        super().__init__(name)
        self.__settings = settings
        self.__convert()

    def __convert(self):
        for field in dir(self):
            if field.startswith("_") or not hasattr(self.__settings, field):
                continue
            
            value = getattr(self.__settings, field)
            setattr(self, f"_{self.__class__.__name__}__{field}", value)

    # ИНН
    @property
    def inn(self):
        return self.__INN

    # БИК
    @property
    def bic(self):
        return self.__BIC
    
    # Счёт
    @property
    def score(self):
        return self.__score

    # Вид собственности
    @property
    def type_of_ownership(self):
        return self.__type_of_ownership