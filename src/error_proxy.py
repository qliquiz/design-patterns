class error_proxy:
    __error_text = ''
    __error_source = ''
    __is_error = ''

    def __init__(self, error_text:str = '', error_source:str = '') -> None:
        self.error_source = error_source
        self.error_text = error_text

    @property
    def error_text(self):
        return self.__error_text
    
    @error_text.setter
    def error_text(self, value:str):
        if not isinstance(value, str): raise Exception('Error: Некорректно передан аргумент!')
        
        value = value.strip()

        if value.strip() == '':
            self.__is_error = False
            return

        self.__error_text = value.strip()
        self.__is_error = True


    @property
    def error_source(self):
        return self.__error_source
    
    @error_source.setter
    def error_source(self, value:str):
        if not isinstance(value, str): raise Exception('Error: Некорректно передан аргумент!')
        
        value = value.strip()
        
        if value.strip() == '':
            return

        self.__error_source = value.strip()


    @property
    def is_error(self):
        return self.__is_error


    def set_error(self, exception:Exception):
        if not isinstance(exception, Exception):
            self.error_text = 'Error: Некорректно переданы параметры!'
            self.error_source = 'set_error'
            return

        if exception is not None:    
            self.error_text = f'Error: {str(exception)}'
            self.error_source = f'Exception: {type(exception)}'
        else: self.error_text = ''
        