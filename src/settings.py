from Src.exceptions import exception_proxy

# Класс для описания настроек
class settings():
    _inn = 0
    _short_name = ""
    _first_start = True
    _report_format = ''
    
    @property
    def inn(self):
        """
            ИНН
        Returns:
            int: 
        """
        return self._inn

    @inn.setter
    def inn(self, value: int):
        exception_proxy.validate(value, int)
        self._inn = value


    @property     
    def short_name(self):
        """
            Короткое наименование организации
        Returns:
            str:
        """
        return self._short_name
    
    @short_name.setter
    def short_name(self, value:str):
        exception_proxy.validate(value, str)
        self._short_name = value


    @property
    def is_first_start(self):
        return self._first_start


    @is_first_start.setter
    def is_first_start(self, value:bool):
        self._first_start = value


    @property
    def report_format(self):
        return self._report_format


    @report_format.setter
    def report_format(self, value:str):
        self._report_format = value