from tkinter import *
class Gerenciar :
    def __init__(self):
        self.telageren = Toplevel()
        self.geometry()

    def geometry(self):
        self.telageren.title("Gerenciar Usuarios ")
        self.telageren.geometry("1360x760")
        self.telageren.configure(bg="DodgerBlue")
        self.telageren.resizable(False, False)
        self.telageren.iconbitmap('__init__\Imagens\logo.ico')
