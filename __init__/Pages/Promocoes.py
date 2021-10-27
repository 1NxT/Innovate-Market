from tkinter import *
from Classes.Config import *
from Classes.MySql import *
from Classes.Pesquisar import *
from Classes.Mostrar import *

class Promocoes:
    def __init__(self):
        self.telapromo = Toplevel()
        self.geometry()

        self.elementos()

    def geometry(self):
        self.telapromo.title("Promoçoes")
        self.telapromo.geometry("1360x760")
        self.telapromo.configure(bg="DodgerBlue")
        self.telapromo.resizable(False, False)
        self.__iconImagemPath = Config().images() / "logo.ico"
        self.telapromo.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_promocoes(self):
        self.telapromo.destroy()
        return
    
    
    def clear_entry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")
    
    
    def view_tree(self):
        resultado = Mostrar().mostrar(self, "promocoes", "nome_produto")
        
        if resultado != None:
            self.tree_promo.delete(*self.tree_promo.get_children())
            
            for i in resultado:
                self.tree_promo.insert("","end",values=i)
        else:
            print("Error!")
        
    
    def chamaPesquisar(self):
        resultado = Pesquisar().pesquisar(self.ent_pesquisar.get(), "promocoes", "nome_produto")

        
        if resultado != None:
            self.tree_promo.delete(*self.tree_promo.get_children())
            
            for i in resultado:
                self.tree_promo.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")


    def elementos(self):

        self.btn_telainicial_promo = Button(self.telapromo, text="Voltar Para Tela Inicial",bg="red", command=self.voltar_inicial_promocoes)
        self.btn_telainicial_promo.place(x=1100, y=550)
        
        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_promo_frame = Frame(self.telapromo, padx=1, pady=5, bg="DodgerBlue")
        self.tree_promo_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_promo_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_promo = ttk.Treeview(self.tree_promo_frame,column=("1","2","3","4"), show='headings', height=35, yscrollcommand=self.scroll.set)
        self.tree_promo.pack()

        self.scroll.config(command=self.tree_promo.yview)

        self.tree_promo.heading('#1', text="Cupom", anchor=CENTER)
        self.tree_promo.heading('#2', text="Nome do Produto", anchor=CENTER)
        self.tree_promo.heading('#3', text="Preço do Produto", anchor=CENTER)
        self.tree_promo.heading('#4', text="Desconto", anchor=CENTER)
        self.view_tree()


        self.ent_pesquisar = Entry(self.telapromo)
        self.ent_pesquisar.place(x=1100, y=20)

        self.btn_pesquisar_pedi = Button(self.telapromo, text="Pesquisar")
        self.btn_pesquisar_pedi.place(x=1000, y=20)

        self.btn_show = Button(self.telapromo, text="Mostrar todos")
        self.btn_show.place(x=1200,y=100)
