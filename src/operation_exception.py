from src.settings_manager import settings_manager


class operation_exception(Exception):
    __inner_error: settings_manager = settings_manager()

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.__inner_error.set_error(self)

    def error(self):
        return self.__inner_error