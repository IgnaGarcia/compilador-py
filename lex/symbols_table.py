class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SymbolsTable(metaclass=SingletonMeta):
    table = {}
    lastIndex = 0
    
    def append(self, symbol):
        self.table[symbol["name"]] = symbol
        self.lastIndex += 1
        
    def get(self):
        print(self.table)
