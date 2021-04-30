from tkinter import *
from Pages.Caixa import *
from Pages.Fornecedores import *
from Pages.Gerenciar import *
from Pages.Lucros import *
from Pages.Pedidos import *
from Pages.Produtos import *
from Pages.Promocoes import *

class SegundaTela:
    def __init__(self):
        self.tela2 = Toplevel()
        self.geometry()
        self.elementos()

        self.imgbtn2 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\produtos.png")
        self.imgbtn3 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\pedidos.png")
        self.imgbtn4 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\fornecedor.png")
        self.imgbtn5 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\lucro.png")
        self.imgbtn6 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\promocoes.png")
        self.imgbtn7 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\gerente.png")
        self.imgbtn9 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\caixa.png")

    def geometry(self):
        self.tela2.title("Tela Inicial")
        self.tela2.geometry("1360x768")
        self.tela2.configure(bg="DodgerBlue")
        self.tela2.resizable(False, False)
        self.tela2.iconbitmap('Innovate-Market-main\__init__\Imagens\logo.ico')

    def elementos(self):
        btn_img9 = Button(tela2, image=self.imgbtn9, width=140, height=140,bg="DodgerBlue", command=Caixa(), relief="flat")
        btn_img9.grid(row=1, column=8)

        btn_img2 = Button(tela2, image=self.imgbtn2,  width=140, height=140,bg="DodgerBlue", command=Produto(), relief="flat")
        btn_img2.grid(row=1, column=2)

        btn_img3 = Button(tela2, image=self.imgbtn3,  width=140, height=140,bg="DodgerBlue", command=Pedido(), relief="flat")
        btn_img3.grid(row=1, column=3)

        btn_img4 = Button(tela2, image=self.imgbtn4,  width=140, height=140,bg="DodgerBlue", command=Fornecedor(), relief="flat")
        btn_img4.grid(row=1, column=4)

        btn_img5 = Button(tela2, image=self.imgbtn5,  width=140, height=140,bg="DodgerBlue", command=Lucros(), relief="flat")
        btn_img5.grid(row=1, column=5)

        btn_img6 = Button(tela2, image=self.imgbtn6,  width=140,height=140, bg="DodgerBlue", command=Promocoes(), relief="flat")
        btn_img6.grid(row=1, column=6)

        btn_img7 = Button(tela2, image=self.imgbtn7,  width=140, height=140,bg="DodgerBlue", command=Gerenciar(), relief="flat")
        btn_img7.grid(row=1, column=7)
