"""from src.settings import settings
from src.settings_manager import settings_manager
import unittest

class test_settings(unittest.TestCase):
    #Проверка корректности заполнения поля
    def test_check_first_name(self):
        #Подготовка
        item = settings()
        #Действие
        item.first_name = "a "
        #Проверка
        assert item.first_name == "a"

    def test_check_open_settings(self):
        manager = settings_manager()

        result = manager.open("settings.json")

        assert result == True

    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        print(str(manager1.number))
        print(str(manager2.number))

        assert manager1.number == manager2.number

    def test_check_manager_convert(self):
        manager = settings_manager()
        manager.open("settings.json")

        manager.convert()
"""
from settings import settings
from settings_manager import  settings_manager
import unittest


class test_settings(unittest.TestCase):
    
    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        print(str(manager1.number))
        print(str(manager2.number))
    
        assert manager1.number == manager2.number
    
    def test_check_first_name(self):
        item = settings()
        
        item.first_name = "a  "
        
        assert item.first_name == "a"
        
    def test_check_manager_convert(self):
        manager = settings_manager()
        manager.open("settings.json")

        manager.convert()       
        
    def test_check_open_settings(self):
        manager = settings_manager()
        
        result = manager.open("settings.json")
        
        print(manager.data)
        assert result == True