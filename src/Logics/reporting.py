from abc import abstractmethod, ABC
from Src.settings import settings


class reporting(ABC):
    __settings : settings
    __data : dict
    __fields : list


    def __init__(self, _settings:settings, _data) -> None:
        self.__settings = _settings
        self.__data = _data


    @property         
    def getData(self) -> dict:
        return self.__data


    @property
    def getFields(self) -> list:
        return self.__fields


    @abstractmethod
    def create(self, key:str) -> str:
        data = self.__data
        res = []
        elem = data[key][0]
        attrs = dir(elem) # получаем список всех атрибутов 

        for attr in attrs:
            res.append(attr)

        self.__fields = res # запись

        return ''