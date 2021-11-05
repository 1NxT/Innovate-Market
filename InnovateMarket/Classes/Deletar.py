from Classes.MySql import *

class Deletar():
    def __init__(self):
        self.cursor = MySql().conectar()

    def deletar(self, tabela: str, coluna: str, valor: int):
        self.cursor.execute(f"DELETE FROM {tabela} WHERE {coluna} = {valor};")
        self.cursor.execute("commit;")
    
        
        
