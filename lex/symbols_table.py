from msilib.schema import tables


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SymbolsTable(metaclass=SingletonMeta):
    # Symbol: { value, name, typeOf, length }
    table = []
    lastIndex = 0
    
    def append(self, symbol):
        # Verifica si ya existe, sino esta lo agrega
        if symbol not in self.table:
            self.table.append(symbol)
            self.lastIndex += 1
        
        
    def get(self):
        print(self.table)
        return self.table
        
    def getByIndex(self, idx):
        return self.table[idx]
       
    def getByName(self, name):
        # Buscar el simbolo con ese nombre y lo retorna(o su indice)
        return self.getByIndex(self.table.index(name))
    
    def setValue(self, idx, value):
        # Agrega valor y longitud al simbolo
        self.table[idx].value = value
        self.table[idx].length = len(value)

