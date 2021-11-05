from Classes.Values import *

class ValuesDB():
    def carregarValues(self, values):
        self.values = values
        return Values(values[0], values[1], values[2], values[3])