#from Pages.Adicionar.Adicionar_pedi import *
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from controller.Controller import pedidosControler
from view.Adicionar.Adicionar_pedi import *
from view.Editar.Editar_pedidos import *
from model.Config import *

class Pedidos:
    def __init__(self):
        self.telapedi = Toplevel()
        self.telapedi.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.telapedi.title("Pedidos")
        self.telapedi.geometry("1360x768")
        self.telapedi.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.telapedi.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_pedi(self):
            self.telapedi.destroy()
            return
        
    def clearEntry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")
        
    def mostrarDados(self):
        resultado = pedidosControler().mostarPedido()
        
        if resultado != None:
            self.tree_pedi.delete(*self.tree_pedi.get_children())
            
            for i in resultado:
                self.tree_pedi.insert("","end",values=i)
        else:
            print("Error!")
    
    # Função para procurar por dados na Treeview        
    def chamaPesquisar(self):
        resultado = pedidosControler().pesquisarPedido(self.ent_pesquisar.get())

        if resultado != None:
            self.tree_pedi.delete(*self.tree_pedi.get_children())
            
            for i in resultado:
                self.tree_pedi.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")

    def editar_pedido(self):
        if not self.tree_pedi.focus():
            messagebox.showwarning(title="ERRO!", message="Selecione uma opção para editar", parent=self.telapedi)
        else:
            self.currItem = self.tree_pedi.focus()
            self.values = pedidosControler().valuesPedidos(self.tree_pedi.item(self.currItem)['values'])
            Editar_Pedi(self.values)
            return self.mostrarDados()
        
    def deleteElemento(self):
        if not self.tree_pedi.focus():
            messagebox.showwarning(title="ERRO!", message="Selecione uma opção para editar", parent=self.telapedi)
        else:
            self.currItem = self.tree_pedi.focus()
            self.values = produtosControler().valuesProdutos(
                self.tree_pedi.item(self.currItem)['values'])
            self.tree_pedi.delete(self.currItem)
            pedidosControler().deletarPedido(self.values.id)
            
    def elementos(self):

        self.pathBg = imagespath / "pedidos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.telapedi, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_pedi = Button(self.telapedi, image=self.btn_voltartelainicial, command=self.voltar_inicial_pedi, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pedi.place(x=980, y=660)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_pedi_frame = Frame(self.telapedi, padx=0, pady=1, bg="lightgrey")
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
        self.mostrarDados()
     

        self.ent_pesquisar = Entry(self.telapedi, bg="lightgrey", width=25, font="Arial 18")
        self.ent_pesquisar.place(x=886, y=160)

        self.img_pesquisar = imagespath / "pesquisar.png"
        self.btn_pesquisar = PhotoImage(file =self.img_pesquisar)
        self.btn_pesquisar_pedi = Button(self.telapedi, image=self.btn_pesquisar, command=self.chamaPesquisar, relief="flat", borderwidth=0, width=110, height=50)
        self.btn_pesquisar_pedi.place(x=1225, y=150)


        self.img_mostrar = imagespath / "Mostrar.png"
        self.btn_mostrar = PhotoImage(file =self.img_mostrar)
        self.btn_showpedi = Button(self.telapedi, command=lambda:[self.mostrarDados(), self.clearEntry()], image=self.btn_mostrar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_showpedi.place(x=980,y=210)

        self.img_editar = imagespath / "editar.png"
        self.btn_editar = PhotoImage(file =self.img_editar)
        self.btn_showpedi = Button(self.telapedi, command=self.editar_pedido, image=self.btn_editar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_showpedi.place(x=980, y=400)

        self.img_deletar = imagespath / "deletar.png"
        self.btn_deletar = PhotoImage(file =self.img_deletar)
        self.btn_deletarpedi = Button(self.telapedi, command=self.deleteElemento, image=self.btn_deletar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_deletarpedi.place(x=980, y=467)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_show_pedi = Button(self.telapedi, command=Adicionar_pedi, image=self.btn_adicionar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show_pedi.place(x=980, y=330)
