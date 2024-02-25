from Src.Models.group_model import group_model
from Src.Models.unit_model import unit_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.recipe_model import recipe_model
from Src.Models.recipe_model import recipe
from Src.settings import settings
from Src.Storage.storage import storage
from Src.exceptions import exception_proxy, argument_exception
from Src.reference import reference

# Класс для обработки данных. Начало работы приложения
class start_factory:
    __options: settings = None
    __storage: storage = None
    
    def __init__(self, _options: settings, _storage: storage = None) -> None:
        exception_proxy.validate(_options, settings)
        self.__options = _options
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
        # Фабричный метод. Создать список номенклатуры
        # Рецепты
        waffles = []
        caesar = []
        meringue = []
        # Группы
        waffles_group = group_model.create_group()
        caesar_group = group_model.create_group()
        meringue_group = group_model.create_group()
        # Вафли
        waffles.append(nomenclature_model("Мука пшеничная", waffles_group, unit_model.create_kilogram()))
        waffles.append(nomenclature_model("Сахар", waffles_group, unit_model.create_gram()))
        waffles.append(nomenclature_model("Сливочное масло", waffles_group, unit_model.create_gram()))
        waffles.append(nomenclature_model("Яйца", waffles_group, unit_model.create_one()))
        waffles.append(nomenclature_model("Ванилин", waffles_group, unit_model.create_gram()))
        # Цезарь с курицей
        caesar.append(nomenclature_model("Куриное филе", caesar_group, unit_model.create_kilogram()))
        caesar.append(nomenclature_model("Салат Романо", caesar_group, unit_model.create_gram()))
        caesar.append(nomenclature_model("Сыр Пармезан", caesar_group, unit_model.create_kilogram()))
        caesar.append(nomenclature_model("Чеснок", caesar_group, unit_model.create_one()))
        caesar.append(nomenclature_model("Белый хлеб", caesar_group, unit_model.create_kilogram()))
        caesar.append(nomenclature_model("Соль", caesar_group, unit_model.create_gram()))
        caesar.append(nomenclature_model("Чёрный перец", caesar_group, unit_model.create_gram()))
        caesar.append(nomenclature_model("Оливковое масло", caesar_group, unit_model.create_liter()))
        caesar.append(nomenclature_model("Лимонный сок", caesar_group, unit_model.create_one()))
        caesar.append(nomenclature_model("Горчица дижонская", caesar_group, unit_model.create_one()))
        caesar.append(nomenclature_model("Яйца", caesar_group, unit_model.create_one()))
        # Безе
        meringue.append(nomenclature_model("Яичный белок", meringue_group, unit_model.create_one()))
        meringue.append(nomenclature_model("Сахарная пудра", meringue_group, unit_model.create_gram()))
        meringue.append(nomenclature_model("Ванилин", meringue_group, unit_model.create_gram()))
        meringue.append(nomenclature_model("Корица", meringue_group, unit_model.create_gram()))
        meringue.append(nomenclature_model("Какао", meringue_group, unit_model.create_gram()))
        
        result = [waffles, caesar, meringue]

        return result


    @staticmethod
    def create_recipes():
        # Все ингредиенты для трёх рецептов
        nomenclatures = start_factory.create_nomenclature()
        # Создание рецептов
        recipe1 = recipe('Ваффли в ваффельнице', nomenclatures[0], 'Вкусные ваффли)')
        recipe2 = recipe('Цезарь с курицей', nomenclatures[1], 'Обалденный Цезарь с курочкой))')
        recipe3 = recipe('Безе', nomenclatures[2], 'ЛЕГЕНДАРНЫЙ РЕЦЕПТ БЕЗЕ)))')

        result = [recipe1, recipe2, recipe3]

        return result


    def create(self):
        """
        В зависимости от настроек, сформировать начальную номенклатуру
        Returns:
            _type_: _description_
        """
        result = []
        if self.__options.is_first_start == True:
            self.__options.is_first_start = False
            # Формируем и запоминаем номенклатуру
            result = start_factory.create_recipes()
            self.__save( storage.nomenclature_key(), result )
            self.__save( storage.group_key(), result )
            self.__save( storage.unit_key(), result )

        return result