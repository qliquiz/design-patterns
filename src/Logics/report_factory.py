from Src.Logics.reporting import reporting
from Src.Logics.markdown_reporting import markdown_reporting
from Src.Logics.csv_reporting import csv_reporting
from Src.exceptions import exception_proxy, argument_exception, operation_exception


class report_factory:
    __maps = {}


    def __init__(self):
        self.__build_structure()


    def __build_structure(self):
        self.__maps['csv'] = csv_reporting
        self.__maps['markdown'] = markdown_reporting


    def create(self, format:str, data) -> reporting:
        exception_proxy.validate(format, str)
        if data is None:
            raise argument_exception('Нет данных!')
        if len(data) == 0:
            raise argument_exception('Нет данных!')
        if format in self.__maps.keys():
            raise operation_exception(f'Для {format} нет обработчика!')
        
        report_type = self.__maps[format]
        result = report_type(data)

        return result