from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.settings import settings


class start_factory:
    __options:settings = None

    
    def __init__(self, options:settings) -> None:
        self.__options = options


    @staticmethod
    def create_nomenclature():
        result = []

        item1 = nomenclature_model()
        item1.group = group_model.create_group()
        item1.unit = unit_model.create_kilogram()

        result.append(item1)

        return result


    def create(self):
        if self.__options.is_first_start == True:
            self.__options.is_first_start = False
            return start_factory.create_nomenclature()
        else:
            items = []
            return items