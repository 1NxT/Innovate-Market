from tkinter import *

class Fornecedor:
    def __init__(self):
        self.telaforne = Toplevel()
        self.geometry()

    def geometry(self):
        self.telaforne.title("Fornecedor")
        self.telaforne.geometry("1360x760")
        self.telaforne.configure(bg="DodgerBlue")
        self.telaforne.resizable(False, False)
        self.telaforne.iconbitmap('__init__\Imagens\logo.ico')
