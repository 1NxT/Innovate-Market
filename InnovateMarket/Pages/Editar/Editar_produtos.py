from tkinter import *
from Pages.common.Config import *

class Editar_produtos(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.edit_produtos = Toplevel()
        self.edit_produtos.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.edit_produtos.title("Produtos")
        self.edit_produtos.geometry("1360x760")
        self.edit_produtos.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.edit_produtos.iconbitmap(self.__iconImagemPath)

    def elementos(self):
        self.pathBg = imagespath / "produtos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)

        self.lblimgbg = Label(self.telaprodutos, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_pro = Button(self.edit_produtos, command=self.voltar_inicial_pro, image=self.btn_voltartelainicial, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pro.place(x=980, y=660)