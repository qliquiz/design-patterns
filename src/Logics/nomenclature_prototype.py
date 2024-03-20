from Src.exceptions import argument_exception
from Src.errors import error_proxy
from Src.Models.nomenclature_model import nomenclature_model

from datetime import datetime

class nomenclature_prototype(error_proxy):
    __data = []

    def __init__(self, data: list) -> None:
        if len(data) == 0:
            self.error = "Некорректно передана data"
        
        self.__data = data

    def filter(self, nomenclature: nomenclature_model):
        if not isinstance(nomenclature, nomenclature_model):
            self.error = "Некорректная номенклатура"

        if not self.is_empty:
            return self.__data
        
        result = []

        for item in self.__data:
            if item.nomenclature == nomenclature:
                print("add")
                result.append(item)

        return nomenclature_prototype(result)