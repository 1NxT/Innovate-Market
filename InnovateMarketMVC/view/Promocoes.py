from tkinter import *
import tkinter.ttk as ttk
from controller.Controller import *

from model.Config import *

class Promocoes:
    def __init__(self):
        self.telapromo = Toplevel()
        self.telapromo.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.telapromo.title("Promoçoes")
        self.telapromo.geometry("1360x760")
        self.telapromo.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        #self.telapromo.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_promocoes(self):
        self.telapromo.destroy()
        return
    
    
    # def clear_entry(self):
    #     self.ent_pesquisar.delete(0, END)
    #     self.ent_pesquisar.insert(0, "")
    
    
    # def view_tree(self):
    #     resultado = Mostrar().mostrar(self, "cupons", "ID")
        
    #     if resultado != None:
    #         self.tree_promo.delete(*self.tree_promo.get_children())
            
    #         for i in resultado:
    #             self.tree_promo.insert("","end",values=i)
    #     else:
    #         print("Error!")
        
    
    # def chamaPesquisar(self):
    #     resultado = Pesquisar().pesquisar(self.ent_pesquisar.get(), "promocoes", "nome_produto")

        
    #     if resultado != None:
    #         self.tree_promo.delete(*self.tree_promo.get_children())
            
    #         for i in resultado:
    #             self.tree_promo.insert("","end",values=i)
    #     else:
    #         print("Error: Nenhum valor saiu da Classe")


    def elementos(self):
        self.pathBg = imagespath / "promocoes_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.telapromo, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_promo = Button(self.telapromo, image= self.btn_voltartelainicial, command=self.voltar_inicial_promocoes, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_promo.place(x=980, y=660)
        
        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_promo_frame = Frame(self.telapromo, padx=0, pady=1, bg="Lightgrey")
        self.tree_promo_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_promo_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_promo = ttk.Treeview(self.tree_promo_frame,column=("1","2","3","4"), show='headings', height=37, yscrollcommand=self.scroll.set)
        self.tree_promo.pack()

        self.scroll.config(command=self.tree_promo.yview)

        self.tree_promo.heading('#1', text="Cupom", anchor=CENTER)
        self.tree_promo.heading('#2', text="Nome do Produto", anchor=CENTER)
        self.tree_promo.heading('#3', text="Preço do Produto", anchor=CENTER)
        self.tree_promo.heading('#4', text="Desconto", anchor=CENTER)
        self.view_tree()


        self.ent_pesquisar = Entry(self.telapromo, width=25, font="Arial 18")
        self.ent_pesquisar.place(x=886, y=160)

        self.img_pesquisar = imagespath / "pesquisar.png"
        self.btn_pesquisar = PhotoImage(file =self.img_pesquisar)
        self.btn_pesquisar_promo = Button(self.telapromo, image=self.btn_pesquisar, command=self.chamaPesquisar, relief="flat", borderwidth=0, width=110, height=50)
        self.btn_pesquisar_promo.place(x=1225, y=150)

        self.img_mostrar = imagespath / "Mostrar.png"
        self.btn_mostrar = PhotoImage(file =self.img_mostrar)
        self.btn_show = Button(self.telapromo, command=lambda:[self.view_tree(), self.clear_entry()], image=self.btn_mostrar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=980,y=210)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_show = Button(self.telapromo, command=lambda:[self.view_tree()], image=self.btn_adicionar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=980, y=330)

        self.img_editar = imagespath / "editar.png"
        self.btn_editar = PhotoImage(file =self.img_editar)
        self.btn_show = Button(self.telapromo, command=lambda:[self.view_tree()], image=self.btn_editar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=980, y=400)

        self.img_deletar = imagespath / "deletar.png"
        self.btn_deletar = PhotoImage(file =self.img_deletar)
        self.btn_show = Button(self.telapromo, command=lambda:[self.view_tree()], image=self.btn_deletar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=980, y=467)
