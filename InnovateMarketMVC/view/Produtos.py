from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from tkinter import messagebox
from controller.Controller import produtosControler
from view.Editar.Editar_produtos import *
from view.Adicionar.Adicionar_pro import *
from model.Config import *

class Produtos(Frame):
    def __init__(self):
        self.dicti = {}
        self.telaprodutos = Toplevel()
        self.telaprodutos.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.telaprodutos.title("Produtos")
        self.telaprodutos.geometry("1360x768")
        self.telaprodutos.configure(bg="Lightgrey")
        self.telaprodutos.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        #self.telaprodutos.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_pro(self):
        self.telaprodutos.destroy()
        return

    def clear_entry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")


    def view_tree(self):
        self.resultado = produtosControler().mostarProdutos()

        if self.resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())
            for i in self.resultado:

                self.tree_pro.insert("","end",values=i)
        else:
            print("Error!")

    def chamaPesquisar(self):
        #nome, preco, fornecedor, id

        self.dicti["nome"] = self.ent_pesquisar.get()
        self.dicti["preco"] = self.ent_pesquisar.get()
        self.dicti["id"] = self.ent_pesquisar.get()
        resultado = produtosControler().pesquisarProdutos(self.dicti)


        if resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())

            for i in resultado:
                self.tree_pro.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")

    def deleteElemento(self):
        if not self.tree_pro.focus():
            messagebox.showwarning(title="ERRO!", message="Selecione uma opção para editar", parent=self.telaprodutos)
        else:
            self.currItem = self.tree_pro.focus()
            self.values = produtosControler().valuesProdutos(
                self.tree_pro.item(self.currItem)['values'])
            self.tree_pro.delete(self.currItem)
            produtosControler().deletarProduto(self.values.id)
            self.tree_pro.bind('<ButtonRelease-1>', self.currItem)


    def edit_pro(self):
        if not self.tree_pro.focus():
            messagebox.showwarning(title="ERRO!", message="Selecione uma opção para editar", parent=self.telaprodutos)
        else:
            self.currItem = self.tree_pro.focus()
            self.values = produtosControler().valuesProdutos(self.tree_pro.item(self.currItem)['values'])
            Editar_produtos(self.values)
            return self.view_tree()


    def elementos(self):
        self.pathBg = imagespath / "produtos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.telaprodutos, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_pro_frame = Frame(self.telaprodutos, padx=2, pady=2, bg="lightgrey")
        self.tree_pro_frame.place(x=10, y=5)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pro_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pro = ttk.Treeview(self.tree_pro_frame, column=("Código de barras","Preço", "Nome"), show='headings', height=37, yscrollcommand=self.scroll.set)

        self.tree_pro.pack()

        self.scroll.config(command=self.tree_pro.yview)

        self.tree_pro.heading('#1', text="Código de barras", anchor=CENTER)
        self.tree_pro.heading('#2', text="Preço", anchor=CENTER)
        self.tree_pro.heading('#3', text="Nome", anchor=CENTER)
    
        self.view_tree()

        # ENTRYS TELA PRODUTOS
        self.ent_pesquisar = Entry(self.telaprodutos, width=35, font="Arial 18")
        self.ent_pesquisar.place(x=700, y=160)

        # BUTTONS TELA PRODUTOS
        self.img_pesquisar = imagespath / "pesquisar.png"
        self.btn_pesquisar = PhotoImage(file =self.img_pesquisar)
        self.btn_pesquisar_pro = Button(self.telaprodutos, image=self.btn_pesquisar, command=self.chamaPesquisar, relief="flat", borderwidth=0, width=105, height=50)
        self.btn_pesquisar_pro.place(x=1165, y=150)

        self.img_mostrar = imagespath / "Mostrar.png"
        self.btn_mostrar = PhotoImage(file =self.img_mostrar)
        self.btn_show = Button(self.telaprodutos, command=lambda:[self.view_tree(), self.clear_entry()], image=self.btn_mostrar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=910, y=210)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_show = Button(self.telaprodutos, command=Adicionar_pro, image=self.btn_adicionar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=910, y=330)

        self.img_editar = imagespath / "editar.png"
        self.btn_editar = PhotoImage(file =self.img_editar)
        self.btn_show = Button(self.telaprodutos, command=self.edit_pro, image=self.btn_editar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=910, y=400)

        self.img_deletar = imagespath / "deletar.png"
        self.btn_deletar = PhotoImage(file =self.img_deletar)
        self.btn_show = Button(self.telaprodutos, command=self.deleteElemento, image=self.btn_deletar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=910, y=467)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_pro = Button(self.telaprodutos, command=self.voltar_inicial_pro, image=self.btn_voltartelainicial, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pro.place(x=910, y=660)
