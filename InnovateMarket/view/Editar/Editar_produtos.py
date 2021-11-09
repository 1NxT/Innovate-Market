from tkinter import *
import tkinter.ttk as ttk
from typing import ValuesView
from view.Produtos import *
from controller.Controller import produtosControler

from model.Config import *

class Editar_produtos():
    def __init__(self, values):
        self.values = values
        self.id = self.values.id
        self.edit_produtos = Toplevel()
        self.edit_produtos.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

        # Clear Entrys
        self.ent_cod.delete(0, END)
        self.ent_preco.delete(0, END)
        self.ent_nome.delete(0, END)

        # Insert values on Entrys
        self.ent_cod.insert(0, self.values.id)
        self.ent_preco.insert(0, self.values.preco)
        self.ent_nome.insert(0, self.values.nome)


    def geometry(self):
        self.edit_produtos.title("Edite seu produto")
        self.edit_produtos.geometry("1360x768")
        self.edit_produtos.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.edit_produtos.iconbitmap(self.__iconImagemPath)

    def updateProduto(self):
        self.values.id = self.ent_cod.get()
        self.values.preco = self.ent_preco.get()
        self.values.id = self.ent_cod.get()
        print(self.values.id)
        produtosControler().atualizarProdutos(self.values, self.id)
        self.mostrarDados()
        self.edit_produtos.destroy()
        return 

    def mostrarDados(self):
        self.resultado = produtosControler().mostarProdutos()

        if self.resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())
            for i in self.resultado:

                self.tree_pro.insert("","end",values=i)
        else:
            print("Error!")

    def elementos(self):
        self.pathBg = imagespath / "editProdutos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.edit_produtos, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_pro_frame = Frame(self.edit_produtos, padx=2, pady=2, bg="lightgrey")
        self.tree_pro_frame.place(x=20, y=5)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pro_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pro = ttk.Treeview(self.tree_pro_frame, column=("Código de barras","Preço", "Nome"), show='headings', height=37, yscrollcommand=self.scroll.set)

        self.tree_pro.pack()

        self.scroll.config(command=self.tree_pro.yview)

        self.tree_pro.heading('#1', text="Código de barras", anchor=CENTER)
        self.tree_pro.heading('#2', text="Preço", anchor=CENTER)
        self.tree_pro.heading('#3', text="Nome", anchor=CENTER)

        self.mostrarDados()

        # self.tree_pro.bind("<ButtonRelease-1>")

        #Entrys
        self.ent_cod = Entry(self.edit_produtos, bg="lightgrey", width=25, font="Arial 18")
        self.ent_cod.place(x=710, y=230)

        self.ent_preco = Entry(self.edit_produtos, bg="lightgrey", width=25, font="Arial 18")
        self.ent_preco.place(x=710, y=350)

        self.ent_nome = Entry(self.edit_produtos, bg="lightgrey", width=25, font="Arial 18")
        self.ent_nome.place(x=710, y=470)

        self.btn_salvarPath = imagespath / "Salvar.png"
        self.btn_salvar = PhotoImage(file=self.btn_salvarPath)
        self.btn_salvar_pro = Button(self.edit_produtos, command=self.updateProduto, image=self.btn_salvar, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_salvar_pro.place(x=980, y=660)

