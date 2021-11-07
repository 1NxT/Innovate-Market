from tkinter import *
from tkinter import messagebox
from view.Caixa import *
from view.Fornecedores import *
from view.Gerenciar import *
from view.Lucros import *
from view.Pedidos import *
from view.Produtos import *
from model.Config import *
from model.Usuario import Cargo


class SegundaTela(Frame):
    def __init__(self, usuario):
        Frame.__init__(self, master=None)
        self.tela2 = Toplevel()
        self.tela2.attributes("-fullscreen", True)
        self.elementos()
        self.CarregarTela(usuario.cargo)

    def iExit2(self):
        self.tela2.destroy()
        return

    def __geometry(self):
        self.tela2.title("Tela Inicial")
        self.tela2.geometry("1360x768")
        self.tela2.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        #self.tela2.iconbitmap(self.__iconImagemPath)

    def elementos(self):
        self.pathBg = imagespath / "Tela de menu.png"
        self.__bg = PhotoImage(file=self.pathBg)

        self.lblimgbg = Label(self.tela2, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

    #Methods Create Buttons
    def __criarButtonCaixaImagem(self):
        self.__caixaImagemPath = imagespath / "caixa.png"
        self.__caixaImagem = PhotoImage(file=self.__caixaImagemPath)
        self.__btn_CaixaImagem = Button(
            self.tela2, image=self.__caixaImagem, width=140,  command=Caixa, relief="flat", borderwidth=0)
        self.__btn_CaixaImagem.place(x=745, y=70)

    def __criarButtonProdutosImagem(self):
        self.__produtosImagemPath = imagespath / "Produtos1.png"
        self.__produtosImagem = PhotoImage(file=self.__produtosImagemPath)
        self.__btn_produtosImagem = Button(
            self.tela2, image=self.__produtosImagem,  width=140, command=Produtos, relief="flat", borderwidth=0)
        self.__btn_produtosImagem.place(x=60, y=70)

    def __criarButtonPedidosImagem(self):
        self.__pedidosImagemPath = imagespath / "pedidos.png"
        self.__pedidosImagem = PhotoImage(file=self.__pedidosImagemPath)
        self.__btn_pedidosImagem = Button(
            self.tela2, image=self.__pedidosImagem,  width=140,  command=Pedidos, relief="flat", borderwidth=0)
        self.__btn_pedidosImagem.place(x=60, y=400)

    def __criarButtonFornecedoresImagem(self):
        self.__fornecedorImagemPath = imagespath / "Fornecedor.png"
        self.__fornecedorImagem = PhotoImage(file=self.__fornecedorImagemPath)
        self.__btn_fornecedorImagem = Button(
            self.tela2, image=self.__fornecedorImagem,  width=140,  command=Fornecedor, relief="flat", borderwidth=0)
        self.__btn_fornecedorImagem.place(x=370, y=70)

    def __criarButtonLucrosImagem(self):
        self.__lucroImagemPath = imagespath / "lucro.png"
        self.__lucroImagem = PhotoImage(file=self.__lucroImagemPath)
        self.__btn_lucroImagem = Button(
            self.tela2, image=self.__lucroImagem,  width=140, command=Lucros, relief="flat", borderwidth=0)
        self.__btn_lucroImagem.place(x=370, y=400)

    def __criarButtonGerenciarImagem(self):
        self.__gerenteImagemPath = imagespath / "gerente.png"
        self.__gerenteImagem = PhotoImage(file=self.__gerenteImagemPath)
        self.__btn_gerenteImagem = Button(
            self.tela2, image=self.__gerenteImagem,  width=140, command=Gerenciar, relief="flat", borderwidth=0)
        self.__btn_gerenteImagem.place(x=745, y=400)

    def __criarBtnVoltar(self):
        self.__btn_voltarImagePath = imagespath / "logout_button.png"
        self.__btn_voltarImage = PhotoImage(file=self.__btn_voltarImagePath)
        self.btn_voltar = Button(self.tela2, command=self.iExit2, image=self.__btn_voltarImage, relief="ridge", borderwidth=0)
        self.btn_voltar.place(x=1150, y=660)

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

            self.__criarButtonGerenciarImagem()

            self.__criarBtnVoltar()
