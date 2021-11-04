from Classes.MySql import *

class Deletar():
    def __init__(self):
        self.cursor = MySql().conectar()

    def deletar(self, tabela: str, coluna: str, valor: int):
        print(tabela, coluna, valor)
        self.cursor.execute("DELETE FROM produtos WHERE ID = 1;")
        self.cursor.execute("commit;")
    
        
        
