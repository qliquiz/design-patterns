import unittest
from src.settings_manager import settings_manager
from src.models.organization_model import organization_model
from src.models.range_model import range_model
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model

class test_models(unittest.TestCase):
    def test_check_organization_convert(self):
        manager = settings_manager()
        manager.open("settings.json")
        settings = manager.settings

        organization = organization_model(settings)
        flag = True

        for i in dir(organization):
            if i.startswith("_") or not hasattr(settings, i):
                continue
            
            if getattr(settings, i) != getattr(organization, i):
                flag = False
                break

        assert flag == False


    def test_nomenclature_group(self):
        group = nomenclature_group_model('Группа 1')

        assert bool(group) == True


    def test_nomenclature(self):
        nom = nomenclature_model("Номенклатура 1", 'супер номенклатура', nomenclature_group_model('группа'), range_model(name='unit'))

        assert bool(nom) == True