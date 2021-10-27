from tkinter import *
import tkinter.ttk as ttk
from Classes.MySql import *
from Classes.Config import *
from Classes.Pesquisar import *
from Classes.Mostrar import *


class Fornecedor:
    def __init__(self):
        self.dicti = {}
        self.telaforne = Toplevel()
        self.geometry()
        
        self.elementos()

    def geometry(self):
        self.telaforne.title("Fornecedor")
        self.telaforne.geometry("1360x760")
        self.telaforne.configure(bg="DodgerBlue")
        self.telaforne.resizable(False, False)
        self.__iconImagemPath = Config().images() / "logo.ico"
        self.telaforne.iconbitmap(self.__iconImagemPath)
        
    def voltar_inicial_forne(self):
        self.telaforne.destroy()
        return
    
    def clear_entry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")
    
    def view_tree(self):
        resultado = Mostrar().mostrar(self, "fornecedor", "nome")
        
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
        
        resultado = Pesquisar().pesquisar(self.dicti, "fornecedor", "nome")

        if resultado != None:
            self.tree_forne.delete(*self.tree_forne.get_children())
            for i in resultado:
                self.tree_forne.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")
    
    def elementos(self):
        self.btn_telainicial_forne = Button(self.telaforne, text="Voltar Para Tela Inicial", command=self.voltar_inicial_forne, bg="red")
        self.btn_telainicial_forne.place(x=1100, y=700)
        
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_forne_frame = Frame(self.telaforne, padx=1, pady=5, bg="DodgerBlue")
        self.tree_forne_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_forne_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_forne = ttk.Treeview(self.tree_forne_frame, column=("1","2","3","4","5"), show='headings', height=35, yscrollcommand=self.scroll.set)
        self.tree_forne.pack()

        self.scroll.config(command=self.tree_forne.yview)

        self.tree_forne.heading('#1', text="Nome", anchor=CENTER)
        self.tree_forne.heading('#2', text="CNPJ", anchor=CENTER)
        self.tree_forne.heading('#3', text="Telefone", anchor=CENTER)
        self.tree_forne.heading('#4', text="Endereco", anchor=CENTER)
        self.tree_forne.heading('#5',text="Produto Fornecido", anchor=CENTER)
        self.view_tree()

        self.ent_pesquisar = Entry(self.telaforne)
        self.ent_pesquisar.place(x=1100, y=20)

        self.btn_pesquisar_pedi = Button(self.telaforne, text="Pesquisar", command=self.chamaPesquisar)
        self.btn_pesquisar_pedi.place(x=1000, y=20)

        self.btn_show = Button(self.telaforne, text="Mostrar todos", command=lambda:[self.view_tree(), self.clear_entry()])
        self.btn_show.place(x=1200,y=100)
