from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception


class csv_reporting(reporting):
    def create(self, key: str):
        super().create(key)
        result = ''
        separator = '; '
        data = self.data[key]
        
        # Проверка данных
        if data is None or len(data) == 0:
            raise operation_exception('Error: данные пусты!')
        
        # Заголовоки
        headers = separator.join(self.fields)
        result += f'{headers}\n'
        
        # Действие
        for elem in data:
            row = ''

            for field in self.fields:
                value = getattr(elem, field)
                row += f'{value}; '

            result += f'{row[:-1]}\n'
        
        return result