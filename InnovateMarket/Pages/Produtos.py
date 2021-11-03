from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from Classes.MySql import *
from Classes.Pesquisar import *
from Classes.Mostrar import *
from Pages.common.Config import *

class Produtos(Frame):
    def __init__(self):
        self.dicti = {}
        Frame.__init__(self, master=None)
        self.telaprodutos = Toplevel()
        self.telaprodutos.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()
        
    def geometry(self):
        self.telaprodutos.title("Produtos")
        self.telaprodutos.geometry("1360x760")
        self.telaprodutos.configure(bg="DodgerBlue")
        self.telaprodutos.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.telaprodutos.iconbitmap(self.__iconImagemPath)

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
        self.pathBg = imagespath / "produtos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)

        self.lblimgbg = Label(self.telaprodutos, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_pro = Button(self.telaprodutos, command=self.voltar_inicial_pro, image=self.btn_voltartelainicial, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pro.place(x=1000, y=660)

        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_pro_frame = Frame(self.telaprodutos, padx=0, pady=0, bg="lightgrey")
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
        self.ent_pesquisar = Entry(self.telaprodutos, width=25, font="Arial 18")
        self.ent_pesquisar.place(x=886, y=130)
        
        # BUTTONS TELA PRODUTOS
        self.img_pesquisar = imagespath / "pesquisar.png"
        self.btn_pesquisar = PhotoImage(file =self.img_pesquisar)
        self.btn_pesquisar_pro = Button(self.telaprodutos, image=self.btn_pesquisar, command=self.chamaPesquisar, relief="flat", borderwidth=0, width=110, height=50)
        self.btn_pesquisar_pro.place(x=1225, y=120)

        self.img_mostrar = imagespath / "Mostrar.png"
        self.btn_mostrar = PhotoImage(file =self.img_mostrar)
        self.btn_show = Button(self.telaprodutos, command=lambda:[self.view_tree(), self.clear_entry()], image=self.btn_mostrar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=980, y=180)
