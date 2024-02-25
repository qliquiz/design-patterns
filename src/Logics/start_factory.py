from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.settings import settings
from Src.Storage.storage import storage
from Src.exceptions import exception_proxy, argument_exception
from Src.reference import reference

# Класс для обработки данных. Начало работы приложения
class start_factory:
    __oprions: settings = None
    __storage: storage = None
    
    def __init__(self, _options: settings, _storage: storage = None) -> None:
        exception_proxy.validate(_options, settings)
        self.__oprions = _options
        self.__storage = _storage
    
    
    def __save(self, key:str, items: list):
        """
            Сохранить данные
        Args:
            key (str): ключ доступ
            items (list): список
        """
        exception_proxy.validate(key, str)
        if self.__storage == None:
            self.__storage = storage()
        self.__storage.data[ key ] = items
        
        
    @property            
    def storage(self):
        """
        Ссылка на объект хранилище данных
        Returns:
            _type_: _description_
        """
        return self.__storage


    @staticmethod
    def create_nomenclature():
        # Фабричный метод Создать список номенклатуры
        waffles = []
        meringue = []
        caesar = []

        waffles.append(nomenclature_model("Мука пшеничная", group_model.create_group(), unit_model.create_kilogram()))
        waffles.append(nomenclature_model("Сахар", group_model.create_group(), unit_model.create_gram()))
        waffles.append(nomenclature_model("Сливочное масло", group_model.create_group(), unit_model.create_gram()))
        waffles.append(nomenclature_model("Яйца", group_model.create_group(), unit_model.create_one()))
        waffles.append(nomenclature_model("Ванилин", group_model.create_group(), unit_model.create_gram()))

        caesar.append(nomenclature_model("Куриное филе", group_model.create_group(), unit_model.create_kilogram()))
        caesar.append(nomenclature_model("Салат Романо", group_model.create_group(), unit_model.create_gram()))
        caesar.append(nomenclature_model("Сыр Пармезан", group_model.create_group(), unit_model.create_kilogram()))
        caesar.append(nomenclature_model("Чеснок", group_model.create_group(), unit_model.create_one()))
        caesar.append(nomenclature_model("Белый хлеб", group_model.create_group(), unit_model.create_kilogram()))
        caesar.append(nomenclature_model("Соль", group_model.create_group(), unit_model.create_gram()))
        caesar.append(nomenclature_model("Чёрный перец", group_model.create_group(), unit_model.create_gram()))
        caesar.append(nomenclature_model("Оливковое масло", group_model.create_group(), unit_model.create_liter()))
        caesar.append(nomenclature_model("Лимонный сок", group_model.create_group(), unit_model.create_one()))
        caesar.append(nomenclature_model("Горчица дижонская", group_model.create_group(), unit_model.create_one()))
        caesar.append(nomenclature_model("Яйца", group_model.create_group(), unit_model.create_one()))

        meringue.append(nomenclature_model("Яичный белок", group_model.create_group(), unit_model.create_one()))
        meringue.append(nomenclature_model("Сахарная пудра", group_model.create_group(), unit_model.create_gram()))
        meringue.append(nomenclature_model("Ванилин", group_model.create_group(), unit_model.create_gram()))
        meringue.append(nomenclature_model("Корица", group_model.create_group(), unit_model.create_gram()))
        meringue.append(nomenclature_model("Какао", group_model.create_group(), unit_model.create_gram()))
        
        return waffles, caesar, meringue


    def create(self):
        """
        В зависимости от настроек, сформировать начальную номенклатуру
        Returns:
            _type_: _description_
        """
        result = []
        if self.__oprions.is_first_start == True:
            self.__oprions.is_first_start = False
            # Формируем и зпоминаем номеклатуру
            result = start_factory.create_nomenclature()
            self.__save( storage.nomenclature_key(), result )

        return result