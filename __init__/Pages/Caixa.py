from tkinter import *
class Caixa:
    def __init__(self):
        self.telacaixa = Toplevel()
        self.geometry()

    def geometry(self):
        self.telacaixa.title("Caixa")
        self.telacaixa.geometry("1360x760")
        self.telacaixa.configure(bg="DodgerBlue")
        self.telacaixa.resizable(False, False)
        self.telacaixa.iconbitmap('Innovate-Market-main\__init__\Imagens\logo.ico')
