from tkinter import *

class Produtos:
    def __init__(self):
        self.telaprodutos = Toplevel()
        self.geometry()

    def geometry(self):
        self.telaprodutos.title("Produtos")
        self.telaprodutos.geometry("1360x760")
        self.telaprodutos.configure(bg="DodgerBlue")
        self.telaprodutos.resizable(False, False)
        self.telaprodutos.iconbitmap('__init__\Imagens\logo.ico')
