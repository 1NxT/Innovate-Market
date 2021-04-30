from tkinter import *
from Pages.Caixa import *
from Pages.Fornecedor import *
from Pages.Gerenciar import *
from Pages.Lucros import *
from Pages.Pedidos import *
from Pages.Produtos import *
from Pages.Promocoes import *

class SegundaTela(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.tela2 = Toplevel()
        self.geometry()
        self.imgbtn2 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\produtos.png")
        self.imgbtn3 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\pedidos.png")
        self.imgbtn4 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\ornecedor.png")
        self.imgbtn5 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\lucro.png")
        self.imgbtn6 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\promocoes.png")
        self.imgbtn7 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\gerente.png")
        self.imgbtn9 = PhotoImage(file="Innovate-Market-main\__init__\Imagens\caixa.png")
        self.elementos()

    def iExit2(self):
        self.tela2.destroy()
        return


    def geometry(self):
        self.tela2.title("Tela Inicial")
        self.tela2.geometry("1360x768")
        self.tela2.configure(bg="DodgerBlue")
        self.tela2.resizable(False, False)
        self.tela2.iconbitmap('Innovate-Market-main\__init__\Imagens\logo.ico')

    def elementos(self):
        #Texto botões
        btn_caixa = Button(self.tela2, text="Caixa", width=15,height=2, command=Caixa)
        btn_caixa.grid(row=2, column=8)

        btn_produtos = Button(self.tela2, text='Produtos',width=15, height=2, command=Produtos)
        btn_produtos.grid(row=2, column=2)

        btn_pedidos = Button(self.tela2, text='Pedidos', width=15,height=2, command=Pedidos)
        btn_pedidos.grid(row=2, column=3)

        btn_fornecedores = Button(self.tela2, text='Fornecedores', width=15, height=2, command=Fornecedor)
        btn_fornecedores.grid(row=2, column=4)

        btn_lucro = Button(self.tela2, text='Lucro', width=15, height=2, command=Lucros)
        btn_lucro.grid(row=2, column=5)

        # btn_Editarpro = Button(self.tela2, text='Editar Produtos', width=15, height=2, command=editar_pro)
        # btn_Editarpro.grid(row=4, column=2)

        # btn_Editarpedi = Button(self.tela2, text='Editar Pedidos',width=15, height=2, command=edit_pedi)
        # btn_Editarpedi.grid(row=4, column=3)

        # btn_Editarfor = Button(self.tela2, text='Editar Fornecedores',width=15, height=2, command=editar_for)
        # btn_Editarfor.grid(row=4, column=4)

        # btn_Editarpromo = Button(self.tela2, text='Editar Promocoes', width=15, height=2, command=editar_promocoes)
        # btn_Editarpromo.grid(row=4, column=6)

        # btn_editar_lucro = Button(self.tela2, text="Editar Lucro", width=15, height=2)
        # btn_editar_lucro.grid(row=4, column=5)

        btn_promocao = Button(self.tela2, text='Promocoes',width=15, height=2, command=Promocoes)
        btn_promocao.grid(row=2, column=6)

        btn_gerenciar = Button(self.tela2, text='Gerenciar Usuários',width=15, height=2, command=Gerenciar)
        btn_gerenciar.grid(row=2, column=7)

        btn_voltar = Button(self.tela2, text="Logout", width=20,command=self.iExit2, bg="firebrick")
        btn_voltar.place(x=1150, y=700)

        #Imagens Botões

        btn_img9 = Button(self.tela2, image=self.imgbtn9, width=140, height=140,bg="DodgerBlue", command=Caixa, relief="flat")
        btn_img9.grid(row=1, column=8)

        btn_img2 = Button(self.tela2, image=self.imgbtn2,  width=140, height=140,bg="DodgerBlue", command=Produtos, relief="flat")
        btn_img2.grid(row=1, column=2)

        btn_img3 = Button(self.tela2, image=self.imgbtn3,  width=140, height=140,bg="DodgerBlue", command=Pedidos, relief="flat")
        btn_img3.grid(row=1, column=3)

        btn_img4 = Button(self.tela2, image=self.imgbtn4,  width=140, height=140,bg="DodgerBlue", command=Fornecedor, relief="flat")
        btn_img4.grid(row=1, column=4)

        btn_img5 = Button(self.tela2, image=self.imgbtn5,  width=140, height=140,bg="DodgerBlue", command=Lucros, relief="flat")
        btn_img5.grid(row=1, column=5)

        btn_img6 = Button(self.tela2, image=self.imgbtn6,  width=140,height=140, bg="DodgerBlue", command=Promocoes, relief="flat")
        btn_img6.grid(row=1, column=6)

        btn_img7 = Button(self.tela2, image=self.imgbtn7,  width=140, height=140,bg="DodgerBlue", command=Gerenciar, relief="flat")
        btn_img7.grid(row=1, column=7)
