import uuid
from abc import ABC
from src.argument_exception import argument_exception
from error_proxy import error_proxy


class abstruct_reference(ABC):
    __id: uuid.UUID
    __name:str = ''
    __error:error_proxy = error_proxy()

    def __init__(self, name:str = None) -> None:
        self.name = name
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
            raise argument_exception('Неверный аргумент!')
        
        if value == '':
            raise argument_exception('Некорректное наименование!')
        
        self.__name = value.strip()