from tkinter import *
import tkinter.ttk as ttk
from typing import ValuesView
from controller.Controller import *

from model.Config import *

class Editar_Pedi():
    def __init__(self, values):
        self.values = values
        self.id = self.values.ID
        self.edit_pedi = Toplevel()
        self.edit_pedi.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

        # Clear Entrys
        self.ent_cod.delete(0, END)
        self.ent_preco.delete(0, END)
        self.ent_nome.delete(0, END)
        # Insert values on Entrys
        self.ent_cod.insert(0, self.values.ID)
        self.ent_preco.insert(0, self.values.valores)
        self.ent_nome.insert(0, self.values.produtos)

    def geometry(self):
        self.edit_pedi.title("Produtos")
        self.edit_pedi.geometry("1360x768")
        self.edit_pedi.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.edit_pedi.iconbitmap(self.__iconImagemPath)

    def view_tree(self):
        resultado = pedidosControler().mostarPedido()

        if resultado != None:
            self.tree_pedi.delete(*self.tree_pedi.get_children())

            for i in resultado:
                self.tree_pedi.insert("", "end", values=i)
        else:
            print("Error!")
            
    def updatePedido(self):
        self.values.ID = self.ent_cod.get()
        self.values.produtos = self.ent_nome.get()
        self.values.valores = self.ent_preco.get()
        
        pedidosControler().atualizarPedidos(self.values, self.id)
        self.view_tree()
        self.edit_pedi.destroy()
        return
    
    def elementos(self):
        self.pathBg = imagespath / "editPedidos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.edit_pedi, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "Salvar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_pro = Button(self.edit_pedi, command=self.updatePedido, image=self.btn_voltartelainicial, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pro.place(x=980, y=660)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_pedi_frame = Frame(self.edit_pedi, padx=0, pady=1, bg="lightgrey")
        self.tree_pedi_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pedi_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pedi = ttk.Treeview(self.tree_pedi_frame, column=("1","2","3","4"), show='headings', height=35, yscrollcommand=self.scroll.set)
        self.tree_pedi.pack()

        self.scroll.config(command=self.tree_pedi.yview)

        self.tree_pedi.heading('#1', text="Numero do Pedido", anchor=CENTER)
        self.tree_pedi.heading('#2', text="Nome do produto", anchor=CENTER)
        self.tree_pedi.heading('#3', text="Data", anchor=CENTER)
        self.tree_pedi.heading('#4', text="Valores", anchor=CENTER)

        self.view_tree()

        # self.tree_pro.bind("<ButtonRelease-1>")

        #Entrys
        self.ent_cod = Entry(self.edit_pedi, width=25, font="Arial 18")
        self.ent_cod.place(x=886, y=160)

        self.ent_preco = Entry(self.edit_pedi, width=25, font="Arial 18")
        self.ent_preco.place(x=886, y=280)

        self.ent_nome = Entry(self.edit_pedi, width=25, font="Arial 18")
        self.ent_nome.place(x=886, y=400)

