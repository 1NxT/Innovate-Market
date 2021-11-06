from tkinter import *
import tkinter.ttk as ttk
from Pages.common.Config import *
from Classes.MySql import *

class Adicionar_pedi(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.adicionar_pedi = Toplevel()
        self.adicionar_pedi.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()


    def geometry(self):
        self.adicionar_pedi.title("Adicionar Pedidos")
        self.adicionar_pedi.geometry("1360x760")
        self.adicionar_pedi.resizable(False, False)
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.telapedi.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_add_pedi(self):
        self.adicionar_pedi.destroy()
        return

    def elementos(self):
        
        self.pathBg = imagespath / "adicionarpedi_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.adicionar_pedi, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_add_pedi = Button(self.adicionar_pedi, image=self.btn_voltartelainicial, command=self.voltar_inicial_add_pedi, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_add_pedi.place(x=980, y=660)

        self.ent_produtos = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_produtos.place(x=886, y=160)

        self.ent_cliente = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_cliente.place(x=886, y=280)


        self.ent_valor = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_valor.place(x=886, y=400)


        self.ent_num_pedi = Entry(self.adicionar_pedi, width=25, font="Arial 18")
        self.ent_num_pedi.place(x=886, y=520)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_adicionar_pedi = Button(self.adicionar_pedi, image=self.btn_adicionar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_adicionar_pedi.place(x=980, y=580)


         # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_pedi_frame = Frame(self.adicionar_pedi, padx=0, pady=1, bg="lightgrey")
        self.tree_pedi_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pedi_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pedi = ttk.Treeview(self.tree_pedi_frame, column=("1","2","3","4"), show='headings', height=35, yscrollcommand=self.scroll.set)
        self.tree_pedi.pack()

        self.scroll.config(command=self.tree_pedi.yview)

        self.tree_pedi.heading('#1', text="Nome do produto", anchor=CENTER)
        self.tree_pedi.heading('#2', text="Cliente", anchor=CENTER)
        self.tree_pedi.heading('#3', text="Valor Total", anchor=CENTER)
        self.tree_pedi.heading('#4', text="Numero do Pedido", anchor=CENTER)
        