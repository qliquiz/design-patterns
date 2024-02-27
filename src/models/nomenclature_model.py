from Src.reference import reference
from Src.exceptions import exception_proxy


class nomenclature_model(reference):
    " Название номеклатуры "
    _name = None
    " Группа номенклатуры "
    _group = None
    " Единица измерения "
    _unit = None


    def __init__(self, name, group = None, unit = None):
        super().__init__(name)
        self._name = name
        self._group = group
        self._unit = unit
    
    
    @property
    def group(self):
        " Группа номенклатуры "
        return self._group
    

    @group.setter
    def group(self, value: reference):
        " Группа номенклатуры "
        exception_proxy.validate(value, reference)
        self._group = value    
    

    @property
    def unit(self):
        " Единица измерения "
        return self._unit
    

    @unit.setter
    def unit(self, value: reference):
        " Единица измерения "
        exception_proxy.validate(value, reference)
        self._unit = value