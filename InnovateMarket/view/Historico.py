from tkinter import *
import tkinter.ttk as ttk
from model.Config import *
from controller.Controller import *

class Historico():
    def __init__(self):
        self.telahistorico = Toplevel()
        self.telahistorico.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.telahistorico.title("Histórico de vendas")
        self.telahistorico.geometry("1360x768")
        self.telahistorico.configure(bg="Lightgrey")
        self.telahistorico.resizable(True, True)
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.telahistorico.iconbitmap(self.__iconImagemPath)
        
    def voltar_inicial_historico(self):
        self.telahistorico.destroy()
        return
    
    def mostrarDados(self):
        self.resultado = vendasControler().mostrarVendas()

        if self.resultado != None:
            self.tree_vendas.delete(*self.tree_vendas.get_children())
            for i in self.resultado:

                self.tree_vendas.insert("","end",values=i)
        else:
            print("Error!")
    
    def elementos(self):
        self.pathBg = imagespath / "historico_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.telahistorico, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)


    

        self.btn_voltarPath = imagespath / "voltar.png"
        self.btn_voltar = PhotoImage(file=self.btn_voltarPath)
        self.btn_voltar_vendas = Button(self.telahistorico, command=self.voltar_inicial_historico, image=self.btn_voltar, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_voltar_vendas.place(x=1100, y=400)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_vendas_frame = Frame(self.telahistorico, padx=2, pady=2, bg="lightgrey")
        self.tree_vendas_frame.place(x=8, y=5)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_vendas_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_vendas = ttk.Treeview(self.tree_vendas_frame, column=("Código de compra", "Nome do produto", "Quantidade", "Código do produto", "Data"), show='headings', height=36, yscrollcommand=self.scroll.set)

        self.tree_vendas.pack()

        self.scroll.config(command=self.tree_vendas.yview)

        self.tree_vendas.heading('#1', text="Código de compra", anchor=CENTER)
        self.tree_vendas.heading('#2', text="Nome do produto", anchor=CENTER)
        self.tree_vendas.heading('#3', text="Quantidade", anchor=CENTER)
        self.tree_vendas.heading('#4', text="Código do produto", anchor=CENTER)
        self.tree_vendas.heading('#5', text="Data", anchor=CENTER)
        self.mostrarDados()

        
