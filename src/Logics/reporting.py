from abc import abstractmethod, ABC
from Src.settings import settings
from Src.exceptions import operation_exception


class reporting(ABC):
    __settings : settings
    __data : dict
    __fields : list


    def __init__(self, _settings:settings, _data) -> None:
        self.__settings = _settings
        self.__data = _data


    @abstractmethod
    def create(self, key:str) -> str:
        self.__fields = self.build(key, self.__data)
        return ''


    def build(key:str, data:dict) -> list:
        # Проверка данных
        if data is None or len(data) == 0:
            raise operation_exception('Error: данные пусты!')
        
        elem = data[key][0]
        result = list(filter(lambda x: not x.startswith("_") and not x.startswith("create_") , dir(elem)))
        
        return result


    def _build(self, key: str) -> list:
        return self.build(key, self.__data)