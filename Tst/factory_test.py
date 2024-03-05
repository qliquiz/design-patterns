from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.Logics.report_factory import report_factory
import unittest

# Набор автотестов для проверки работы фабричного метода
class factory_test(unittest.TestCase):
    # Проверка создания начальных рецептов
    def test_check_create_receipts(self):
        # Подготовка
        items = start_factory.create_recipes()
        # Проверки
        assert len(items) > 0     
        
    # Проверка создание начальной номенклатуры
    def test_check_create_nomenclatures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        # Прверки
        assert len(items) > 0 
        
    # Проверка создание списка единиц измерения
    def test_check_create_units(self):
        # Подготовка
        items = start_factory.create_units()
        # Проверки
        assert len(items) > 0    

    # Проверка создания списка групп
    def test_check_create_groups(self):
        # Подготовка
        items = start_factory.create_groups()
        # Действие
        # Проверки    
        assert len(items) > 0
        
    # Проверка работы класса start_factory. Метод create
    def test_check_factory_create(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory( manager.settings )
        # Действие
        result = factory.create()
        # Проверка
        if manager.settings.is_first_start == True:
            assert result == True
            assert factory.storage is not None
            assert storage.nomenclature_key() in factory.storage.data
            assert storage.recipe_key() in factory.storage.data
            assert storage.group_key() in factory.storage.data
            assert storage.unit_key() in factory.storage.data
        else:
            assert result == False


    def test_check_report_factore_create(self):
        # Подготовка
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()
        factory = report_factory()
        key = storage.unit_key()
        # Действие
        result = factory.create('csv', start.storage.data)
        # Проверка
        assert result is not None