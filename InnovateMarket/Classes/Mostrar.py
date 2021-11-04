import tkinter as tk
from Classes.MySql import *

class Mostrar():
    def __init__(self):

        cursor = MySql().conectar()
        self.cursor = cursor
        
    def mostrar(self, mostrar, tabela, coluna):
        
        self.cursor.execute(f"SELECT * FROM {tabela} ORDER BY {coluna} ASC")
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado