from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from model.Config import *
from controller.Controller import pedidosControler

class Adicionar_pedi():
    def __init__(self):
        self.adicionar_pedi = Toplevel()
        self.adicionar_pedi.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.adicionar_pedi.title("Adicionar pedidos")
        self.adicionar_pedi.geometry("1360x768")
        self.adicionar_pedi.resizable(False, False)
        #self.__iconImagePath = imagespath / "logo.ico"
        #self.adicionar_pedi.iconbitmap(self.__iconImagePath)

    def view_tree(self):
        self.resultado = pedidosControler().mostarPedido()

        if self.resultado != None:
            self.tree_pedi.delete(*self.tree_pedi.get_children())
            for i in self.resultado:
                self.tree_pedi.insert("", "end", values=i)
        else:
            print("ERROR!")

    def voltar_inicial_add_pedi(self):
        self.adicionar_pedi.destroy()
        return
        
    def elementos(self):
        self.pathBg = imagespath / "editPedidos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.adicionar_pedi, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "Salvar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_add_pedi = Button(self.adicionar_pedi, image=self.btn_voltartelainicial, command=self.voltar_inicial_add_pedi, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_add_pedi.place(x=980, y=660)


        self.ent_nomeProduto = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_nomeProduto.place(x=886, y=160)

        self.ent_cliente = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_cliente.place(x=886, y=280)


        self.ent_valorTotal = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_valorTotal.place(x=886, y=400)


        self.ent_numPedi = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_numPedi.place(x=886, y=520)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_adicionar_pro = Button(self.adicionar_pedi, command=self.adicionar_pedido, image=self.btn_adicionar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_adicionar_pro.place(x=980, y=580)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_pedi_frame = Frame(self.adicionar_pedi, padx=0, pady=1, bg="lightgrey")
        self.tree_pedi_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pedi_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        # Treeview
        self.tree_pedi = ttk.Treeview(self.tree_pedi_frame, column=("1","2","3","4"), show='headings', height=35, yscrollcommand=self.scroll.set)
        self.tree_pedi.pack()

        self.scroll.config(command=self.tree_pedi.yview)

        self.tree_pedi.heading('#1', text="Nome do produto", anchor=CENTER)
        self.tree_pedi.heading('#2', text="Cliente", anchor=CENTER)
        self.tree_pedi.heading('#3', text="Valor Total", anchor=CENTER)
        self.tree_pedi.heading('#4', text="Numero do Pedido", anchor=CENTER)
        self.view_tree()