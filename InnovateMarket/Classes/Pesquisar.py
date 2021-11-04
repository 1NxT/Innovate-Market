import tkinter as tk
from Classes.MySql import *


class Pesquisar():
    def __init__(self):
        cursor = MySql().conectar()
        self.cursor = cursor
        
    def pesquisar(self, pesquisa, tabela, coluna):
        keys = list(pesquisa)
        if tabela == "fornecedor":
            self.cursor.execute(f"SELECT * FROM {tabela} WHERE {keys[0]} LIKE '%{pesquisa[keys[0]]}%' OR {keys[1]} LIKE '%{pesquisa[keys[1]]}%' OR {keys[2]} LIKE '%{pesquisa[keys[2]]}%' OR {keys[3]} LIKE '%{pesquisa[keys[3]]}%' OR {keys[4]} LIKE '%{pesquisa[keys[4]]}%' ORDER BY {coluna}")
        else:
            self.cursor.execute(f"SELECT * FROM {tabela} WHERE {keys[0]} LIKE '%{pesquisa[keys[0]]}%' OR {keys[1]} LIKE '%{pesquisa[keys[1]]}%' OR {keys[2]} LIKE '%{pesquisa[keys[2]]}%' OR {keys[3]} LIKE '%{pesquisa[keys[3]]}%' ORDER BY {coluna}")  
        
        resultado = self.cursor.fetchall()  
        self.cursor.close()
   
        return resultado  
        
        
            
