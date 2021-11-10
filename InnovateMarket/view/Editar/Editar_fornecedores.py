from tkinter import *
import tkinter.ttk as ttk
from typing import ValuesView
from controller.Controller import *
from model.Config import *


class Editar_fornecedor():
    def __init__(self, values):
        self.values = values
        self.id = self.values.cnpj
        self.edit_forne = Toplevel()
        self.edit_forne.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

        # Clear Entrys
        self.ent_cnpj.delete(0, END)
        self.ent_nome.delete(0, END)

        # Insert values on Entrys
        self.ent_cnpj.insert(0, self.values.cnpj)
        self.ent_nome.insert(0, self.values.nome)
        self.ent_telefone.insert(0, self.values.telefone)
        self.ent_email.insert(0, self.values.email)


    def geometry(self):
        self.edit_forne.title("Edite seu fornecedor")
        self.edit_forne.geometry("1360x768")
        self.edit_forne.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.edit_forne.iconbitmap(self.__iconImagemPath)


    def mostrarDados(self):
        resultado = fornecedorControler().mostarFornecedor()
        print(resultado)
        if resultado != None:
            self.tree_forne.delete(*self.tree_forne.get_children())

            for i in resultado:
                self.tree_forne.insert("", "end", values=i)
        else:
            print("Error!")

    def atualizarFonecedor(self):
        self.values.nome = self.ent_nome.get()
        self.values.cnpj = self.ent_cnpj.get()
        self.values.telefone = self.ent_telefone.get()
        self.values.email = self.ent_email.get()
        print(self.id)
        fornecedorControler().atualizarFornecedor(self.values, self.id)
        self.mostrarDados()
        self.edit_forne.destroy()
        return

    def elementos(self):
        self.pathBg = imagespath / "editFornecedores_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.edit_forne, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_forne_frame = Frame(self.edit_forne, padx=1, pady=1, bg="lightgrey")
        self.tree_forne_frame.place(x=10, y=5)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_forne_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_forne = ttk.Treeview(self.tree_forne_frame, column=("CNPJ","Nome", "Telefone", "Email"), show='headings', height=43, yscrollcommand=self.scroll.set)

        self.tree_forne.pack()

        self.scroll.config(command=self.tree_forne.yview)

        self.tree_forne.heading('#1', text="CNPJ", anchor=CENTER)
        self.tree_forne.heading('#2', text="Nome", anchor=CENTER)
        self.tree_forne.heading('#3', text="Telefone", anchor=CENTER)
        self.tree_forne.heading('#4', text="Email", anchor=CENTER)
        self.mostrarDados()

        # self.tree_pro.bind("<ButtonRelease-1>")

        #Entrys

        self.ent_nome = Entry(self.edit_forne, bg="lightgrey", width=25, font="Arial 22")
        self.ent_nome.place(x=865, y=200)

        self.ent_cnpj = Entry(self.edit_forne, bg="lightgrey", width=25, font="Arial 22")
        self.ent_cnpj.place(x=865, y=320)

        self.ent_telefone = Entry(self.edit_forne, bg="lightgrey", width=25, font="Arial 22")
        self.ent_telefone.place(x=865, y=445)

        self.ent_email = Entry(self.edit_forne, bg="lightgrey", width=25, font="Arial 22")
        self.ent_email.place(x=865, y=560)

        self.btn_salvarPath = imagespath / "Salvar.png"
        self.btn_salvar = PhotoImage(file=self.btn_salvarPath)
        self.btn_salvar_fornecedor = Button(self.edit_forne, command=self.atualizarFonecedor, image=self.btn_salvar, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_salvar_fornecedor.place(x=980, y=668)