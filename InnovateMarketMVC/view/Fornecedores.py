from tkinter import *
import tkinter.ttk as ttk
from controller.Controller import pesquisarControler
from controller.Controller import mostarControler
from model.Config import *

class Fornecedor:
    def __init__(self):
        self.dicti = {}
        self.telaforne = Toplevel()
        self.telaforne.attributes("-fullscreen", True)
        self.geometry()
        
        self.elementos()

    def geometry(self):
        self.telaforne.title("Fornecedor")
        self.telaforne.geometry("1360x760")
        self.telaforne.configure(bg="DodgerBlue")
        self.telaforne.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        #self.telaforne.iconbitmap(self.__iconImagemPath)
        
    def voltar_inicial_forne(self):
        self.telaforne.destroy()
        return
    
    def clear_entry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")
    
    def view_tree(self):
        resultado = mostarControler().mostarFornecedor()
        
        if resultado != None:
            self.tree_forne.delete(*self.tree_forne.get_children())
            
            for i in resultado:
                self.tree_forne.insert("","end",values=i)
        else:
            print("Error!")
        
    def chamaPesquisar(self):
        self.dicti["nome"] = self.ent_pesquisar.get()
        self.dicti["CNPJ"] = self.ent_pesquisar.get()
        self.dicti["telefone"] = self.ent_pesquisar.get()
        self.dicti["endereco"] = self.ent_pesquisar.get()
        self.dicti["produto_fornecido"] = self.ent_pesquisar.get()
        resultado = pesquisarControler().pesquisarFornecedor(self.dicti)

        if resultado != None:
            self.tree_forne.delete(*self.tree_forne.get_children())
            for i in resultado:
                self.tree_forne.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")
    
    def elementos(self):
        self.pathBg = imagespath / "fornecedor_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)

        self.lblimgbg = Label(self.telaforne, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_for = Button(self.telaforne, command=self.voltar_inicial_forne, image=self.btn_voltartelainicial, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_for.place(x=1075, y=665)
        
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_forne_frame = Frame(self.telaforne, padx=0, pady=0.5, bg="lightgrey")
        self.tree_forne_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_forne_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_forne = ttk.Treeview(self.tree_forne_frame, column=("1","2","3","4","5"), show='headings', height=37, yscrollcommand=self.scroll.set)
        self.tree_forne.pack()

        self.scroll.config(command=self.tree_forne.yview)

        self.tree_forne.heading('#1', text="Nome", anchor=CENTER)
        self.tree_forne.heading('#2', text="CNPJ", anchor=CENTER)
        self.tree_forne.heading('#3', text="Telefone", anchor=CENTER)
        self.tree_forne.heading('#4', text="Endereco", anchor=CENTER)
        self.tree_forne.heading('#5',text="Produto Fornecido", anchor=CENTER)
        self.view_tree()

        self.ent_pesquisar = Entry(self.telaforne, width=16, font="Arial 18")
        self.ent_pesquisar.place(x=1040, y=158)

        self.img_pesquisar = imagespath / "pesquisar.png"
        self.btn_pesquisar = PhotoImage(file =self.img_pesquisar)
        self.btn_pesquisar_pedi = Button(self.telaforne, image=self.btn_pesquisar, command=self.chamaPesquisar, relief="flat", borderwidth=0, width=110, height=50)
        self.btn_pesquisar_pedi.place(x=1255, y=150)

        self.img_mostrar = imagespath / "Mostrar.png"
        self.btn_mostrar = PhotoImage(file =self.img_mostrar)
        self.btn_show = Button(self.telaforne, command=lambda:[self.view_tree(), self.clear_entry()], image=self.btn_mostrar, relief="flat", borderwidth=0, bg="Gainsboro")
        self.btn_show.place(x=1075, y=215)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_show = Button(self.telaforne, command=lambda:[self.view_tree()], image=self.btn_adicionar, relief="flat", borderwidth=0, bg="Gainsboro")
        self.btn_show.place(x=1075, y=340)

        self.img_editar = imagespath / "editar.png"
        self.btn_editar = PhotoImage(file =self.img_editar)
        self.btn_show = Button(self.telaforne, command=lambda:[self.view_tree()], image=self.btn_editar, relief="flat", borderwidth=0, bg="Gainsboro")
        self.btn_show.place(x=1075, y=410)

        self.img_deletar = imagespath / "deletar.png"
        self.btn_deletar = PhotoImage(file =self.img_deletar)
        self.btn_show = Button(self.telaforne, command=lambda:[self.view_tree()], image=self.btn_deletar, relief="flat", borderwidth=0, bg="Gainsboro")
        self.btn_show.place(x=1075, y=477)
