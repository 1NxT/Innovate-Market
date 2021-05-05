import tkinter as tk
from Classes.MySql import *
from Pages.SegundaTela import *

class Logar(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        cursor = MySql().conectar()
        self.cursor = cursor


    def login(self, user, password):
        

        self.cursor.execute("SELECT * FROM usuarios WHERE login = ? AND senha = ?", (user, password, ))
        resultado1 = self.cursor.fetchone()

        return resultado1   
