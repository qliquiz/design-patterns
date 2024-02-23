from Src.Models.unit_model import unit_model
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
import unittest


class factory_test(unittest.TestCase):
    def test_check_create_factory(self):
        #Подготовка
        unit = unit_model.create_kilogram()
        #Проверка
        assert unit is not None


    def test_check_create_nomeclature(self):
        #Подготовка
        items = start_factory.create_nomenclature()
        #Проверка
        assert len(items) > 0


    def test_check_create_method(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        result = factory.create()

        if manager.settings.is_first_start == True:
            assert len(result) > 0
            assert factory.storage is not None
            assert storage.nomenclature_key() in factory.storage.data
            assert storage.unit_key() in factory.storage.data
            assert storage.group_key() in factory.storage.data

        # assert len(result) == 0