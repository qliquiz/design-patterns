import uuid
from abc import ABC
from src.argument_exception import argument_exception
from src.error_proxy import error_proxy


class abstract_reference(ABC):
    __id: uuid.UUID
    __name:str = ''
    __error:error_proxy = error_proxy()

    def __init__(self, name:str = None) -> None:
        self.__name = name
        self.__id = uuid.uuid4()

    @property
    def error(self):
        return self.__error

    @property
    def id(self):
        return self.__error

    @property
    def name(self):
        return self.__name.strip()
    
    def name(self, value:str):
        if not isinstance(value, str):
            raise argument_exception('Error: Неверный аргумент!')
        
        if value == '':
            raise argument_exception('Error: Некорректное наименование!')
        
        value = value.strip()

        if len(value) >= 50:
            raise argument_exception("Error: Неверная длина name!")
        
        self.__name = value.strip()