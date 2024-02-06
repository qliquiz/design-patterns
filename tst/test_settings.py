from src.settings import settings
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