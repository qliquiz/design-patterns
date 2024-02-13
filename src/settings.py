# Создал новую ветвь check-branch

class settings:
    __first_name = ""
    __INN = ""
    __BIC = ""
    __score = ""
    __correspondent_score = ""
    __name = ""
    __type_of_ownership = ""

    # Проверка вводимых данных
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value:str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")
        
        self.__first_name = value.strip()


    @property
    def inn(self):
        return self.__INN

    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")

        if len(value) != 12:
            raise Exception("Error: ИНН должен быть 12 символов!")

        self.__INN = value.strip()


    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")

        if len(value) != 11:
            raise Exception("Error: Счёт должен быть 11 символов!")

        self.__score = value.strip()


    @property
    def correspondent_score(self):
        return self.__correspondent_score

    @correspondent_score.setter
    def correspondent_score(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")

        if len(value) != 11:
            raise Exception("Error: Корреспондентский счёт должен быть 11 символов!")

        self.__correspondent_score = value.strip()


    @property
    def biс(self):
        return self.__BIC

    @biс.setter
    def biс(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")

        if len(value) != 9:
            raise Exception("Error: БИК должен быть 9 символов!")

        self.__BIC = value.strip()


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")

        self.__name = value.strip()


    @property
    def type_of_ownership(self):
        return self.__type_of_ownership

    @type_of_ownership.setter
    def type_of_ownership(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный тип данных")

        if len(value) != 5:
            raise Exception("Error: Вид собственности должен быть 5 символов!")

        self.__type_of_ownership = value.strip()