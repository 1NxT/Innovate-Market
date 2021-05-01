from tkinter import *

class Promocoes:
    def __init__(self):
        self.telap = Toplevel()
        self.geometry()

        self.elementos()

    def geometry(self):
        self.telap.title("Promoçoes")
        self.telap.geometry("1360x760")
        self.telap.configure(bg="DodgerBlue")
        self.telap.resizable(False, False)
        self.telap.iconbitmap('__init__\Imagens\logo.ico')

    def voltar_inicial_promocoes(self):
        promocoes.destroy()
        return

    def elementos(self):

        btn_telainicial_promo = Button(self.telap, text="Voltar Para Tela Inicial",bg="red", command=self.voltar_inicial_promocoes)
        btn_telainicial_promo.place(x=1100, y=550)
        
        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_promo_frame = Frame(self.telap, padx=1, pady=5, bg="DodgerBlue")
        tree_promo_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_promo_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_promo = ttk.Treeview(tree_promo_frame,column=("1","2","3","4"), show='headings', height=35, yscrollcommand=scroll.set)
        tree_promo.pack()

        scroll.config(command=tree_promo.yview)

        tree_promo.heading('#1', text="Cupom", anchor=CENTER)
        tree_promo.heading('#2', text="Nome do Produto", anchor=CENTER)
        tree_promo.heading('#3', text="Preço do Produto", anchor=CENTER)
        tree_promo.heading('#4', text="Desconto", anchor=CENTER)
        


        ent_pesquisar = Entry(self.telap)
        ent_pesquisar.place(x=1100, y=20)

        btn_pesquisar_pedi = Button(self.telap, text="Pesquisar")
        btn_pesquisar_pedi.place(x=1000, y=20)

        btn_show = Button(self.telap, text="Mostrar todos")
        btn_show.place(x=1200,y=100)



