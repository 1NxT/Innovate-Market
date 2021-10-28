from tkinter import *
from tkinter import messagebox
from Pages.Caixa import *
from Pages.Fornecedores import *
from Pages.Gerenciar import *
from Pages.Lucros import *
from Pages.Pedidos import *
from Pages.Produtos import *
from Pages.Promocoes import *
from Pages.common.Config import *
from Classes.Usuario import Cargo

class SegundaTela(Frame):
    def __init__(self, usuario):
        Frame.__init__(self, master=None)
        self.tela2 = Toplevel()
        self.elementos()
        self.CarregarTela(usuario.cargo)

    def iExit2(self):
        self.tela2.destroy()
        return

    def __geometry(self):
        self.tela2.title("Tela Inicial")
        self.tela2.geometry("1360x768")
        self.tela2.resizable(False, False)
        #self.__iconImagemPath = imagespath / "logo.ico"
        #self.tela2.iconbitmap(self.__iconImagemPath)

    def elementos(self):
        self.pathBg = imagespath / "Tela de menu.png"
        self.__bg = PhotoImage(file =self.pathBg)

        self.lblimgbg = Label(self.tela2, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

    #Methods Create Buttons
    def __criarButtonCaixaImagem(self):
        self.__caixaImagemPath = imagespath / "caixa.png"
        self.__caixaImagem = PhotoImage(file=self.__caixaImagemPath)
        self.__btn_CaixaImagem = Button(self.tela2, image=self.__caixaImagem, width=140,  command=Caixa, relief="flat", borderwidth=0)
        self.__btn_CaixaImagem.place(x=1117, y=70)

    def __criarButtonProdutosImagem(self):
        self.__produtosImagemPath = imagespath / "Produtos1.png"
        self.__produtosImagem = PhotoImage(file=self.__produtosImagemPath)
        self.__btn_produtosImagem = Button(self.tela2, image=self.__produtosImagem,  width=140, command=Produtos, relief="flat", borderwidth=0)
        self.__btn_produtosImagem.place(x=60, y=70)


    
    def __criarButtonPedidosImagem(self):
        self.__pedidosImagemPath = imagespath / "pedidos.png"
        self.__pedidosImagem = PhotoImage(file=self.__pedidosImagemPath)
        self.__btn_pedidosImagem = Button(self.tela2, image=self.__pedidosImagem,  width=140,  command=Pedidos, relief="flat", borderwidth=0)
        self.__btn_pedidosImagem.place(x=60, y=400)


    
    def __criarButtonFornecedoresImagem(self):
        self.__fornecedorImagemPath = imagespath / "Fornecedor.png"
        self.__fornecedorImagem = PhotoImage(file=self.__fornecedorImagemPath)
        self.__btn_fornecedorImagem = Button(self.tela2, image=self.__fornecedorImagem,  width=140,  command=Fornecedor, relief="flat", borderwidth=0)
        self.__btn_fornecedorImagem.place(x=370, y=70)



    def __criarButtonLucrosImagem(self):
        self.__lucroImagemPath = imagespath / "lucro.png"
        self.__lucroImagem = PhotoImage(file=self.__lucroImagemPath)
        self.__btn_lucroImagem = Button(self.tela2, image=self.__lucroImagem,  width=140, command=Lucros, relief="flat", borderwidth=0)
        self.__btn_lucroImagem.place(x=370, y=400)



    def __criarButtonPromocoesImagem(self):
        self.__promocoesImagemPath = imagespath / "promocoes.png"
        self.__promocoesImagem = PhotoImage(file=self.__promocoesImagemPath)
        self.__btn_promocoesImagem = Button(self.tela2, image=self.__promocoesImagem,  width=140,  command=Promocoes, relief="flat", borderwidth=0)
        self.__btn_promocoesImagem.place(x=745, y=70)



    def __criarButtonGerenciarImagem(self):
        self.__gerenteImagemPath = imagespath / "gerente.png"
        self.__gerenteImagem = PhotoImage(file=self.__gerenteImagemPath)
        self.__btn_gerenteImagem = Button(self.tela2, image=self.__gerenteImagem,  width=140, command=Gerenciar, relief="flat", borderwidth=0)
        self.__btn_gerenteImagem.place(x=745, y=400)

    def __criarBtnVoltar(self):
        self.__btn_voltarImagePath = imagespath / "sairdosbuttons.png"
        self.__btn_voltarImage = PhotoImage(file=self.__btn_voltarImagePath)
        self.btn_voltar = Button(self.tela2, command=self.iExit2, image=self.__btn_voltarImage)
        self.btn_voltar.place(x=1150, y=665)

    #Validar permissão
    def CarregarTela(self, cargo):
        self.__geometry()
        if cargo == Cargo.CAIXA:
            self.__criarButtonCaixaImagem()

            self.__criarButtonProdutosImagem()

            self.__criarBtnVoltar()

        elif cargo == Cargo.ADMINISTRADOR:
            self.__criarButtonCaixaImagem()

            self.__criarButtonProdutosImagem()

            self.__criarButtonPedidosImagem()

            self.__criarButtonFornecedoresImagem()

            self.__criarButtonLucrosImagem()

            self.__criarButtonPromocoesImagem()

            self.__criarButtonGerenciarImagem()

            self.__criarBtnVoltar()

"""     def elementos(self):
        #Texto botões
        self.__btn_caixa = Button(self.tela2, text="Caixa", width=15,height=2, command=Caixa)
        self.__btn_caixa.grid(row=2, column=8)

        self.__btn_produtos = Button(self.tela2, text='Produtos',width=15, height=2, command=Produtos)
        self.__btn_produtos.grid(row=2, column=2)

        self.__btn_pedidos = Button(self.tela2, text='Pedidos', width=15,height=2, command=Pedidos)
        self.__btn_pedidos.grid(row=2, column=3)

        self.__btn_fornecedores = Button(self.tela2, text='Fornecedores', width=15, height=2, command=Fornecedor)
        self.__btn_fornecedores.grid(row=2, column=4)

        self.__btn_lucro = Button(self.tela2, text='Lucro', width=15, height=2, command=Lucros)
        self.__btn_lucro.grid(row=2, column=5)

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

        self.btn_img9 = Button(self.tela2, image=self.imgbtn9, width=140, height=140, command=Caixa, relief="flat", borderwidth=0)
        self.btn_img9.grid(row=1, column=8)

        self.btn_img2 = Button(self.tela2, image=self.imgbtn2,  width=140, height=140, command=Produtos, relief="flat", borderwidth=0)
        self.btn_img2.grid(row=1, column=2)

        self.btn_img3 = Button(self.tela2, image=self.imgbtn3,  width=140, height=140, command=Pedidos, relief="flat", borderwidth=0)
        self.btn_img3.grid(row=1, column=3)

        self.btn_img4 = Button(self.tela2, image=self.imgbtn4,  width=140, height=140, command=Fornecedor, relief="flat", borderwidth=0)
        self.btn_img4.grid(row=1, column=4)

        self.btn_img5 = Button(self.tela2, image=self.imgbtn5,  width=140, height=140, command=Lucros, relief="flat", borderwidth=0)
        self.btn_img5.grid(row=1, column=5)

        self.btn_img6 = Button(self.tela2, image=self.imgbtn6,  width=140,height=140,  command=Promocoes, relief="flat", borderwidth=0)
        self.btn_img6.grid(row=1, column=6)

        self.btn_img7 = Button(self.tela2, image=self.imgbtn7,  width=140, height=140, command=Gerenciar, relief="flat", borderwidth=0)
        self.btn_img7.grid(row=1, column=7)
 """
