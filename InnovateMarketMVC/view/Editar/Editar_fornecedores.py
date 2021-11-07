from tkinter import *
import tkinter.ttk as ttk
from typing import ValuesView
from controller.Controller import *

from model.Config import *


class Editar_fornecedor(Frame):
    def __init__(self, values):
        self.values = values
        self.id = self.values.cnpj
        Frame.__init__(self, master=None)
        self.edit_forne = Toplevel()
        self.edit_forne.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

        # Clear Entrys
        self.ent_cod.delete(0, END)
        self.ent_nome.delete(0, END)

        # Insert values on Entrys
        self.ent_cod.insert(0, self.values.cnpj)
        self.ent_nome.insert(0, self.values.nome)
        self.ent_telefone.insert(0, self.values.telefone)
        self.ent_email.insert(0, self.values.email)


    def geometry(self):
        self.edit_forne.title("Edite seu fornecedor")
        self.edit_forne.geometry("1360x768")
        self.edit_forne.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.edit_forne.iconbitmap(self.__iconImagemPath)


    def view_tree(self):
        resultado = fornecedorControler().mostarFornecedor()
        print(resultado)
        if resultado != None:
            self.tree_forne.delete(*self.tree_forne.get_children())

            for i in resultado:
                self.tree_forne.insert("", "end", values=i)
        else:
            print("Error!")

    def updateFornecedor(self):
        self.values.nome = self.ent_nome.get()
        self.values.cnpj = self.ent_cod.get()
        self.values.telefone = self.ent_telefone.get()
        self.values.email = self.ent_email.get()
        fornecedorControler().atualizarFornecedor(self.values, self.id)
        self.edit_forne.destroy()
        return

    def elementos(self):
        self.pathBg = imagespath / "fornecedor_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.edit_forne, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_salvarPath = imagespath / "Salvar.png"
        self.btn_salvar = PhotoImage(file=self.btn_salvarPath)
        self.btn_salvar_fornecedor = Button(self.edit_forne, command=self.updateFornecedor, image=self.btn_salvar, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_salvar_fornecedor.place(x=980, y=660)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_forne_frame = Frame(self.edit_forne, padx=0, pady=1, bg="lightgrey")
        self.tree_forne_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_forne_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_forne = ttk.Treeview(self.tree_forne_frame, column=("Código de barras","Preço", "Nome","Fornecedor"), show='headings', height=37, yscrollcommand=self.scroll.set)

        self.tree_forne.pack()

        self.scroll.config(command=self.tree_forne.yview)

        self.tree_forne.heading('#1', text="Nome", anchor=CENTER)
        self.tree_forne.heading('#2', text="CNPJ", anchor=CENTER)
        self.tree_forne.heading('#3', text="Telefone", anchor=CENTER)
        self.tree_forne.heading('#4', text="Email", anchor=CENTER)
        self.view_tree()

        # self.tree_pro.bind("<ButtonRelease-1>")

        #Entrys
        self.ent_cod = Entry(self.edit_forne, width=25, font="Arial 18")
        self.ent_cod.place(x=886, y=160)

        self.ent_nome = Entry(self.edit_forne, width=25, font="Arial 18")
        self.ent_nome.place(x=886, y=400)

        self.ent_telefone = Entry(self.edit_forne, width=25, font="Arial 18")
        self.ent_telefone.place(x=886, y=280)

        self.ent_email = Entry(self.edit_forne, width=25, font="Arial 18")
        self.ent_email.place(x=886, y=520)

        
