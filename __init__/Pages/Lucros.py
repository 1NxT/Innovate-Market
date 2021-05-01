from tkinter import *
class Lucros:
    def __init__(self):
        self.telalucro = Toplevel()
        self.geometry()

    def geometry(self):
        self.telalucro.title("Lucro")
        self.telalucro.geometry("1360x760")
        self.telalucro.configure(bg="DodgerBlue")
        self.telalucro.resizable(False, False)
        self.telalucro.iconbitmap('__init__\Imagens\logo.ico')
