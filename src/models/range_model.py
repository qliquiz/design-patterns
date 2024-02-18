from src.abstract_reference import abstract_reference

class range_model(abstract_reference):
    __base : str
    __num : int
    __coef : int


    def __init__(self, base:str = None, num: int = 1, coef: int = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__base = base
        self.__num = num
        self.__coef = coef


    @property
    def to_base(self):
        num = self.num * self.coef
        return range_model(base = self.base.base, num = num, coef = self.base.coef, name = self.base.name)


    @property
    def num(self):
        return self.__num


    @num.setter
    def num(self, value: int):
        self.__num = value


    @property
    def base(self):
        return self.__base


    @property
    def coef(self):
        return self.__coef


    def __str__(self):
        return f"{self.num} {self.name}"