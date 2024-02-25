from Src.reference import reference
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.exceptions import exception_proxy

# Список ингредиентов рецепта
class recipe_model(reference):
    __nomeclature:nomenclature_model = None
    __size:int = 0
    __unit:unit_model = None


    def __init__(self, _nomeclature:nomenclature_model, _size:int, _unit:unit_model):
        exception_proxy.validate(_nomeclature, reference)
        exception_proxy.validate(_unit, reference)

        self.__nomeclature = _nomeclature
        self.__size = _size
        self.__unit = _unit

        super().__init__(f'{_nomeclature.name}, {_unit.name}')


    @property
    def size(self):
        return self.__size
    

    @property
    def nomenclature(self):
        return self.__nomeclature


    @size.setter
    def size(self, value:int):
        self.__size = value
    

    @nomenclature.setter
    def nomenclature(self, value:int):
        self.__nomeclature = value


# Рецепт
class recipe(reference):
    __ingredients: list
    __description: str


    def __init__(self, _name: str, _ingredients: list[recipe_model], _description: str):
        self.__ingredients = _ingredients
        self.__description = _description
        super().__init__(_name)


    @property
    def ingredients(self):
        return self.__description


    @ingredients.setter
    def ingredients(self, value: str):
        self.__ingredients = value


    @property
    def description(self):
        return self.__description


    @description.setter
    def description(self, value: str):
        self.__description = value