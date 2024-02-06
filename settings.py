class settings:
    __first_name = ""

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")
        
        self.__first_name = value.strip()