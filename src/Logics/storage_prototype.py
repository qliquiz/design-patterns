from Src.Models.storage_model import storage_model
from Src.Models.receipe_model import receipe_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.exceptions import argument_exception
from Src.errors import error_proxy
from datetime import datetime


#
# Прототип для обработки складских транзакций
#
class storage_prototype(error_proxy):
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) <= 0:
            self.error = "Некорректно переданы параметры!"
        
        self.__data = data

    def date_filter( self,start_period: datetime, stop_period: datetime  ):
        """
            Отфильтровать по периоду
        Args:
            data (list): список складских транзакций
            start_period (datetime): начало
            stop_period (datetime): окончание

        Returns:
            storage_prototype: _description_
        """
        if len(self.__data) <= 0:
            self.error = "Некорректно переданы параметры!"
            
        if start_period > stop_period:
            self.error = "Некорректный период!"
        
        
        if not self.is_empty:
            return self.__data
        
        result = []
        for item in self.__data:
            if item.period > start_period and item.period <= stop_period:
                result.append(item)
                
        return   storage_prototype( result )
    
    def nomenclature_filter(self, nomenclature: nomenclature_model):
        if not isinstance(nomenclature, nomenclature_model):
            self.error = "Некорректная номенклатура!"
        if not self.is_empty:
            return self.__data
        
        result = []
        for item in self.__data:
            if item.nomenclature.name == nomenclature.name:
                result.append(item)

        return storage_prototype(result)
    
    def recipe_filter(self, recipe: receipe_model):
        if not isinstance(recipe, receipe_model):
            self.error = "Некорректный рецепт!"
        if not self.is_empty:
            return self.__data
        
        result = []
        rows = set([row.name for row in recipe.rows])
        for item in self.__data:
            if item.nomenclature.name in rows:
                result.append(item)

        return storage_prototype(result)
    
    def storage_filter(self, storage: storage_model):
        if not isinstance(storage, storage_model):
            self.error = "Некорректный склад!"
        if not self.is_empty:
            return self.__data
        
        result = []
        for item in self.__data:
            if item.storage.name == storage.name:
                result.append(item)

        return storage_prototype(result)
    
    @property
    def data(self):
        return self.__data