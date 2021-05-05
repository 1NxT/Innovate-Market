import tkinter as tk
from Classes.MySql import *


class Pesquisar():
    def __init__(self):
        cursor = MySql().conectar()
        self.cursor = cursor
        
    def pesquisar(self, pesquisa, tabela, coluna):
        
        self.cursor.execute(f"SELECT * FROM {tabela} WHERE nome_produto LIKE '%{str(pesquisa)}%' OR fornecedor LIKE '%{str(pesquisa)}%' OR preco LIKE '%{str(pesquisa)}%' OR id_produto LIKE '%{str(pesquisa)}%' ORDER BY {coluna}")  
        resultado = self.cursor.fetchall()     
        return resultado  
        
        
            