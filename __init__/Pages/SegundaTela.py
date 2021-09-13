from tkinter import *
from Pages.Caixa import *
from Pages.Fornecedores import *
from Pages.Gerenciar import *
from Pages.Lucros import *
from Pages.Pedidos import *
from Pages.Produtos import *
from Pages.Promocoes import *

class SegundaTela(Frame):
    def __init__(self, resultado):
        print(resultado)
        if resultado[1] == "1":
            print(resultado[1])
        elif resultado[1] == '2':
            print(resultado[1])
        Frame.__init__(self, master=None)
        self.tela2 = Toplevel()
        self.imgbtn2 = PhotoImage(file="__init__\Imagens\produtos.png")
        self.imgbtn3 = PhotoImage(file="__init__\Imagens\pedidos.png")
        self.imgbtn4 = PhotoImage(file="__init__\Imagens\Fornecedor.png")
        self.imgbtn5 = PhotoImage(file="__init__\Imagens\lucro.png")
        self.imgbtn6 = PhotoImage(file="__init__\Imagens\promocoes.png")
        self.imgbtn7 = PhotoImage(file="__init__\Imagens\gerente.png")
        self.imgbtn9 = PhotoImage(file="__init__\Imagens\caixa.png")
        self.geometry()
        self.elementos()

    def iExit2(self):
        self.tela2.destroy()
        return

    
        
            
        

    def geometry(self):
        self.tela2.title("Tela Inicial")
        self.tela2.geometry("1360x768")
        self.tela2.configure(bg="DodgerBlue")
        self.tela2.resizable(False, False)
        self.tela2.iconbitmap('__init__\Imagens\logo.ico')

    def elementos(self):
        #Texto botões
        self.btn_caixa = Button(self.tela2, text="Caixa", width=15,height=2, command=Caixa)
        self.btn_caixa.grid(row=2, column=8)

        self.btn_produtos = Button(self.tela2, text='Produtos',width=15, height=2, command=Produtos)
        self.btn_produtos.grid(row=2, column=2)

        self.btn_pedidos = Button(self.tela2, text='Pedidos', width=15,height=2, command=Pedidos)
        self.btn_pedidos.grid(row=2, column=3)

        self.btn_fornecedores = Button(self.tela2, text='Fornecedores', width=15, height=2, command=Fornecedor)
        self.btn_fornecedores.grid(row=2, column=4)

        self.btn_lucro = Button(self.tela2, text='Lucro', width=15, height=2, command=Lucros)
        self.btn_lucro.grid(row=2, column=5)

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

        self.btn_promocao = Button(self.tela2, text='Promocoes',width=15, height=2, command=Promocoes)
        self.btn_promocao.grid(row=2, column=6)

        self.btn_gerenciar = Button(self.tela2, text='Gerenciar Usuários',width=15, height=2, command=Gerenciar)
        self.btn_gerenciar.grid(row=2, column=7)

        self.btn_voltar = Button(self.tela2, text="Logout", width=20,command=self.iExit2, bg="firebrick")
        self.btn_voltar.place(x=1150, y=700)

        #Imagens Botões

        self.btn_img9 = Button(self.tela2, image=self.imgbtn9, width=140, height=140,bg="DodgerBlue", command=Caixa, relief="flat")
        self.btn_img9.grid(row=1, column=8)

        self.btn_img2 = Button(self.tela2, image=self.imgbtn2,  width=140, height=140,bg="DodgerBlue", command=Produtos, relief="flat")
        self.btn_img2.grid(row=1, column=2)

        self.btn_img3 = Button(self.tela2, image=self.imgbtn3,  width=140, height=140,bg="DodgerBlue", command=Pedidos, relief="flat")
        self.btn_img3.grid(row=1, column=3)

        self.btn_img4 = Button(self.tela2, image=self.imgbtn4,  width=140, height=140,bg="DodgerBlue", command=Fornecedor, relief="flat")
        self.btn_img4.grid(row=1, column=4)

        self.btn_img5 = Button(self.tela2, image=self.imgbtn5,  width=140, height=140,bg="DodgerBlue", command=Lucros, relief="flat")
        self.btn_img5.grid(row=1, column=5)

        self.btn_img6 = Button(self.tela2, image=self.imgbtn6,  width=140,height=140, bg="DodgerBlue", command=Promocoes, relief="flat")
        self.btn_img6.grid(row=1, column=6)

        self.btn_img7 = Button(self.tela2, image=self.imgbtn7,  width=140, height=140,bg="DodgerBlue", command=Gerenciar, relief="flat")
        self.btn_img7.grid(row=1, column=7)
