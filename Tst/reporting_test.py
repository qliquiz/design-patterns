import unittest
from Src.Models.unit_model import unit_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.settings_manager import settings_manager


class reporting_test(unittest.TestCase):
    # Проверка формирования отчета
    def test_check_create_csv(self):
        # Подготовка
        data = {}
        list = []

        item = unit_model.create_ml()
        key = storage.group_key()

        list.append(item)
        data[key] = list

        manager = settings_manager()
        create_csv = csv_reporting(manager.settings, data)
        # Действие
        res = create_csv.create(key)
        # Проверка
        assert len(res) > 0