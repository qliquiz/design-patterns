import os
import json
import uuid
from src.settings import settings

class settings_manager(object) :
    __file_path = "src/settings.json"
    try:
        file =  open(__file_path)
        __file_name = json.load(file)
    except FileNotFoundError:
        print("Файл не найден.")

    __unique_number = None
    __data = {}
    
    # __settings = settings()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance
    
    def convert(self):
        if len(self.__data) == 0:
            raise Exception("ERROR: Невозможно создать объект settings.py")
        
        new_settings = settings()

        # fields = dir(self.__settings.__class__)
        # print(fields)
        
        for field in self.__data: # по циклу присваиваем полям их значения
            value = self.__data[field]
            setattr(new_settings, field, value)
        
        # print(self.__settings.first_name)
        return new_settings
    
    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()
    
    def open(self, file_name: str) -> bool:
        if not isinstance(file_name, str):
            raise Exception("ERROR: Неверный аргумент!")
        
        if file_name == "":
            raise Exception("ERROR: Введите имя файла!")
        
        self.__file_name = file_name.strip()

        try:
            self.__open()
        except:
            return False

        return True
    
    @property
    def data(self):
        return self.__data
    
    @property
    def number(self)-> str:
        return str(self.__unique_number.hex)
    
    def __open(self):
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self.__file_name)
        if not os.path.exists(settings_file):
            raise Exception("ERROR")

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)
    
    file.close()