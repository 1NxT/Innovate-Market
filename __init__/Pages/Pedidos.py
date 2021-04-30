from tkinter import *
class Pedidos:
    def __init__(self):
        self.telapedi = Toplevel()
        self.geometry()

    def geometry(self):
        self.telapedi.title("Pedidos")
        self.telapedi.geometry("1360x760")
        self.telapedi.configure(bg="DodgerBlue")
        self.telapedi.resizable(False, False)
        self.telapedi.iconbitmap('Innovate-Market-main\__init__\Imagens\logo.ico')