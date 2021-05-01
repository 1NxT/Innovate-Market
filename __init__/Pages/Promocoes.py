from tkinter import *

class Promocoes:
    def __init__(self):
        self.telap = Toplevel()
        self.geometry()

    def geometry(self):
        self.telap.title("Promoçoes")
        self.telap.geometry("1360x760")
        self.telap.configure(bg="DodgerBlue")
        self.telap.resizable(False, False)
        self.telap,iconbitmap('__init__\Imagens\logo.ico')
