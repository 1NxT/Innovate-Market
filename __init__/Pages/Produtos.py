from tkinter import *
import tkinter.ttk as ttk
from Classes.MySql import *
from Classes.Pesquisar import *
from Classes.Mostrar import *

class Produtos(Frame):
    def __init__(self):
        self.dicti = {}
        Frame.__init__(self, master=None)
        self.telaprodutos = Toplevel()
        self.geometry()
        
        self.elementos()
        
    

    def geometry(self):
        self.telaprodutos.title("Produtos")
        self.telaprodutos.geometry("1360x760")
        self.telaprodutos.configure(bg="DodgerBlue")
        self.telaprodutos.resizable(False, False)
        self.telaprodutos.iconbitmap('__init__\Imagens\logo.ico')

    def voltar_inicial_pro(self):
        self.telaprodutos.destroy()
        return
    
    def clear_entry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")
    
    def view_tree(self):
        resultado = Mostrar().mostrar(self, "produtos", "ID")
        
        if resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())
            
            for i in resultado:
                self.tree_pro.insert("","end",values=i)
        else:
            print("Error!")
        
    
    def chamaPesquisar(self):
        #nome, preco, fornecedor, id
        
        self.dicti["nome"] = self.ent_pesquisar.get()
        self.dicti["preco"] = self.ent_pesquisar.get()
        self.dicti["fornecedor"] = self.ent_pesquisar.get()
        self.dicti["id"] = self.ent_pesquisar.get()
        resultado = Pesquisar().pesquisar(self.dicti, "produtos", "ID")

        
        if resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())
            
            for i in resultado:
                self.tree_pro.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")

    def elementos(self):
        self.btn_telainicial_pro = Button(self.telaprodutos, text="Voltar para Tela Inicial", command=self.voltar_inicial_pro, bg="firebrick")
        self.btn_telainicial_pro.place(x=1200, y=700)

        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_pro_frame = Frame(self.telaprodutos, padx=1, pady=10, bg="DodgerBlue")
        self.tree_pro_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pro_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pro = ttk.Treeview(self.tree_pro_frame, column=("Nome","Fornecedor", "Preco","Codigo de Barras"), show='headings', height=35, yscrollcommand=self.scroll.set)
        
        self.tree_pro.pack()

        self.scroll.config(command=self.tree_pro.yview)

        self.tree_pro.heading('#1', text="Nome", anchor=CENTER)
        self.tree_pro.heading('#2', text="Preco", anchor=CENTER)
        self.tree_pro.heading('#3', text="Fornecedor", anchor=CENTER)
        self.tree_pro.heading('#4', text="Codigo de Barras", anchor=CENTER)
        self.view_tree()
        
        # ENTRYS TELA PRODUTOS
        self.ent_pesquisar = Entry(self.telaprodutos)
        self.ent_pesquisar.place(x=950, y=10)
        
        # BUTTONS TELA PRODUTOS
        self.btn_pesquisar_pro = Button(self.telaprodutos, text="Pesquisar", command=self.chamaPesquisar)
        self.btn_pesquisar_pro.place(x=1100, y=10)

        self.btn_show = Button(self.telaprodutos, text="Mostrar todos", command=lambda:[self.view_tree(), self.clear_entry()])
        self.btn_show.place(x=1000,y=50)
