import tkinter as tk
from Classes.MySql import *
from Pages.SegundaTela import *

class Logar(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        cursor = MySql().conectar()
        self.cursor = cursor


    def login(self, user, password):
        

        self.cursor.execute("SELECT * FROM usuarios WHERE login = ?", (user, ))
        resultado1 = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM usuarios WHERE senha = ?", (password, ))
        resultado2 = self.cursor.fetchone()

        
        if resultado1 and resultado2 != None:
            SegundaTela()
        else:
            print("Ta troll!")        
