from Src.Logics.reporting import reporting


class csv_reporting(reporting):
    def create(self, key: str) -> str:
        super().create(key)
        res = ''
        separator = '; '
        data = self.getData[key]
        headers = separator.join(self.getFields)
        res += f'{headers}\n'
        
        for elem in data:
            row = ''
            for field in self.getFields:
                val = getattr(elem, field)
                row += f'{val}; '
            res += f'{row[:-1]}\n'
        
        return res