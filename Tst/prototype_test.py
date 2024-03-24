from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.start_factory import start_factory
import unittest
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from datetime import datetime

class prototype_test(unittest.TestCase):
    def test_check_prototype(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]
        
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
        stop_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
        prototype = storage_prototype( data)
        
        
        # Дейтсвие
        result = prototype.date_filter(   start_date, stop_date ) 
        
        # Проверка
        # assert isinstance(result, storage_prototype)
        # assert prototype.is_empty

    def test_check_nomenclature_prototype(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        key = storage.storage_transaction_key()
        data = start.storage.data[ key ]

        nomenclature_key = storage.nomenclature_key()
        nomenclature_data = start.storage.data[nomenclature_key][1]
        prototype = storage_prototype(data)


        # Действие
        result = prototype.nomenclature_filter(nomenclature_data)

        # Проверка
        assert isinstance(result, storage_prototype)
        assert prototype.is_empty