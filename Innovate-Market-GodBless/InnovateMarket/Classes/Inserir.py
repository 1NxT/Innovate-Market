from Classes.MySql import *

class Inserir():
    def __init__(self):
        self.cursor = MySql().conectar()


    def salvar(self, tabela, valores):
        self.cursor.execute("INSERT INTO {} VALUES ({})".format(tabela, ", ".join(value for value in valores.values())))
        
