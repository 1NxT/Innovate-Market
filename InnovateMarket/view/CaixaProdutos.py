from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from tkinter import messagebox
from controller.Controller import produtosControler
from model.Config import *


class CaixaProdutos():
    def __init__(self):
        self.dicti = {}
        self.telapesquisarprodutos = Toplevel()
        self.telapesquisarprodutos.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.telapesquisarprodutos.title("Produtos")
        self.telapesquisarprodutos.geometry("1360x768")
        self.telapesquisarprodutos.configure(bg="Lightgrey")
        self.telapesquisarprodutos.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.telapesquisarprodutos.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_CaixaPro(self):
        self.telapesquisarprodutos.destroy()
        return

    def clearEntry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")

    def mostrarDados(self):
        self.resultado = produtosControler().mostarProdutos()

        if self.resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())
            for i in self.resultado:

                self.tree_pro.insert("", "end", values=i)
        else:
            print("Error!")

    def chamaPesquisar(self):
        #nome, preco, fornecedor, id

        self.dicti["nome"] = self.ent_pesquisar.get()
        self.dicti["preco"] = self.ent_pesquisar.get()
        self.dicti["fornecedor"] = self.ent_pesquisar.get()
        self.dicti["id"] = self.ent_pesquisar.get()
        resultado = produtosControler().pesquisarProdutos(self.dicti)

        if resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())

            for i in resultado:
                self.tree_pro.insert("", "end", values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")

    def elementos(self):
        self.pathBg = imagespath / "produtos_bg.png"
        self.__bg = PhotoImage(file=self.pathBg)
        self.lblimgbg = Label(self.telapesquisarprodutos, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_pro_frame = Frame(
            self.telapesquisarprodutos, padx=0, pady=1, bg="lightgrey")
        self.tree_pro_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pro_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pro = ttk.Treeview(self.tree_pro_frame, column=(
            "Código de barras", "Preço", "Nome", "Fornecedor"), show='headings', height=37, yscrollcommand=self.scroll.set)

        self.tree_pro.pack()

        self.scroll.config(command=self.tree_pro.yview)

        self.tree_pro.heading('#1', text="Código de barras", anchor=CENTER)
        self.tree_pro.heading('#2', text="Preço", anchor=CENTER)
        self.tree_pro.heading('#3', text="Nome", anchor=CENTER)
        self.tree_pro.heading('#4', text="Fornecedor", anchor=CENTER)
        self.mostrarDados()

        # ENTRYS TELA PRODUTOS
        self.ent_pesquisar = Entry(
            self.telapesquisarprodutos, bg="lightgrey", width=25, font="Arial 18")
        self.ent_pesquisar.place(x=886, y=160)

        # BUTTONS TELA PRODUTOS
        self.img_pesquisar = imagespath / "pesquisar.png"
        self.btn_pesquisar = PhotoImage(file=self.img_pesquisar)
        self.btn_pesquisar_pro = Button(self.telapesquisarprodutos, image=self.btn_pesquisar,
                                        command=self.chamaPesquisar, relief="flat", borderwidth=0, width=110, height=50)
        self.btn_pesquisar_pro.place(x=1225, y=150)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file=self.btn_telainicial)
        self.btn_telainicial_pro = Button(self.telapesquisarprodutos, command=self.voltar_inicial_CaixaPro,
                                          image=self.btn_voltartelainicial, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pro.place(x=980, y=660)