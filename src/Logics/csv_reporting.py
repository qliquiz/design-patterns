from Src.Logics.reporting import reporting


class csv_reporting(reporting):
    def create(self, key: str) -> str:
        data = self.data
        res = []
        elem = data[key][0]

        attrs = dir(elem) # получаем список всех атрибутов 

        for attr in attrs:
            if not (attr.startswith("_") or attr.startswith("create_")):
                res.append(attr)

        self.fields = res # запись

        res = ''
        separator = '; '
        data = self.data[key]
        headers = separator.join(self.fields)
        res += f'{headers}\n'
        
        for elem in data:
            row = ''
            for field in self.fields:
                val = getattr(elem, field)
                row += f'{val}; '
            res += f'{row[:-1]}\n'
        
        return res