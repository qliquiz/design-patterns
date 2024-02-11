class settings:
    __first_name = ""

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value:str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")
        
        self.__first_name = value.strip()

    """ def check_INN(self, INN):
        if len(INN) != 12:
            raise Exception("Количество символов должно быть 12") """