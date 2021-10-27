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

class SegundaTela(Frame):
    def __init__(self, resultado):
        Frame.__init__(self, master=None)
        self.tela2 = Toplevel()
        self.__ValidarPermissao(resultado[2])

    def iExit2(self):
        self.tela2.destroy()
        return

    def __geometry(self):
        self.tela2.title("Tela Inicial")
        self.tela2.geometry("1360x768")
        self.tela2.configure(bg="DodgerBlue")
        self.tela2.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.tela2.iconbitmap(self.__iconImagemPath)

    #Methods Create Buttons
    def __criarButtonCaixa(self):
        self.__btn_caixa = Button(self.tela2, text="Caixa", width=15, height=2, command=Caixa)
        self.__btn_caixa.grid(row=2, column=8)

    def __criarButtonCaixaImagem(self):
        self.__caixaImagemPath = imagespath / "caixa.png"
        self.__caixaImagem = PhotoImage(file=self.__caixaImagemPath)
        self.__btn_CaixaImagem = Button(self.tela2, image=self.__caixaImagem, width=140,height=140, bg="DodgerBlue", command=Caixa, relief="flat")
        self.__btn_CaixaImagem.grid(row=1, column=8)

    def __criarButtonProdutos(self):
        self.__btn_produtos = Button(self.tela2, text='Produtos', width=15, height=2, command=Produtos)
        self.__btn_produtos.grid(row=2, column=2)

    def __criarButtonProdutosImagem(self):
        self.__produtosImagemPath = imagespath / "produtos.png"
        self.__produtosImagem = PhotoImage(file=self.__produtosImagemPath)
        self.__btn_produtosImagem = Button(self.tela2, image=self.__produtosImagem,  width=140,height=140, bg="DodgerBlue", command=Produtos, relief="flat")
        self.__btn_produtosImagem.grid(row=1, column=2)

    def __criarButtonPedidos(self):
        self.__btn_pedidos = Button(self.tela2, text='Pedidos', width=15, height=2, command=Pedidos)
        self.__btn_pedidos.grid(row=2, column=3)
    
    def __criarButtonPedidosImagem(self):
        self.__pedidosImagemPath = imagespath / "pedidos.png"
        self.__pedidosImagem = PhotoImage(file=self.__pedidosImagemPath)
        self.__btn_pedidosImagem = Button(self.tela2, image=self.__pedidosImagem,  width=140,height=140, bg="DodgerBlue", command=Pedidos, relief="flat")
        self.__btn_pedidosImagem.grid(row=1, column=3)

    def __criarButtonFornecedores(self):
        self.__btn_fornecedores = Button(self.tela2, text='Fornecedores', width=15, height=2, command=Fornecedor)
        self.__btn_fornecedores.grid(row=2, column=4)
    
    def __criarButtonFornecedoresImagem(self):
        self.__fornecedorImagemPath = imagespath / "Fornecedor.png"
        self.__fornecedorImagem = PhotoImage(file=self.__fornecedorImagemPath)
        self.__btn_fornecedorImagem = Button(self.tela2, image=self.__fornecedorImagem,  width=140,height=140, bg="DodgerBlue", command=Fornecedor, relief="flat")
        self.__btn_fornecedorImagem.grid(row=1, column=4)

    def __criarButtonLucros(self):
        self.__btn_lucro = Button(self.tela2, text='Lucro', width=15, height=2, command=Lucros)
        self.__btn_lucro.grid(row=2, column=5)

    def __criarButtonLucrosImagem(self):
        self.__lucroImagemPath = imagespath / "lucro.png"
        self.__lucroImagem = PhotoImage(file=self.__lucroImagemPath)
        self.__btn_lucroImagem = Button(self.tela2, image=self.__lucroImagem,  width=140, height=140,bg="DodgerBlue", command=Lucros, relief="flat")
        self.__btn_lucroImagem.grid(row=1, column=5)

    def __criarButtonPromocoes(self):
        self.__btn_Promocoes = Button(self.tela2, text='Promocoes',width=15, height=2, command=Promocoes)
        self.__btn_Promocoes.grid(row=2, column=6)

    def __criarButtonPromocoesImagem(self):
        self.__promocoesImagemPath = imagespath / "promocoes.png"
        self.__promocoesImagem = PhotoImage(file=self.__promocoesImagemPath)
        self.__btn_promocoesImagem = Button(self.tela2, image=self.__promocoesImagem,  width=140,height=140, bg="DodgerBlue", command=Promocoes, relief="flat")
        self.__btn_promocoesImagem.grid(row=1, column=6)

    def __criarButtonGerenciar(self):
        self.btn_gerenciar = Button(self.tela2, text='Gerenciar Usuários',width=15, height=2, command=Gerenciar)
        self.btn_gerenciar.grid(row=2, column=7)

    def __criarButtonGerenciarImagem(self):
        self.__gerenteImagemPath = imagespath / "gerente.png"
        self.__gerenteImagem = PhotoImage(file=self.__gerenteImagemPath)
        self.__btn_gerenteImagem = Button(self.tela2, image=self.__gerenteImagem,  width=140, height=140,bg="DodgerBlue", command=Gerenciar, relief="flat")
        self.__btn_gerenteImagem.grid(row=1, column=7)

    def __criarBtnVoltar(self):
        self.btn_voltar = Button(self.tela2, text="Logout", width=20,command=self.iExit2, bg="firebrick")
        self.btn_voltar.place(x=1150, y=700)

    def __ValidarPermissao(self, permision):
        self.__permision = permision
        if self.__permision == "1":
            self.CarregarTela("Caixa")
        elif self.__permision == "2" or self.__permision == "3":
            self.CarregarTela("Administrador")
        else:
            messagebox.showwarning('ERROR', 'Sua permissão não foi encontrada!', icon="warning")

    #Validar permissão
    def CarregarTela(self, cargo):
        self.__cargo = cargo
        self.__geometry()
        if self.__cargo == "Caixa":
            self.__criarButtonCaixa()
            self.__criarButtonCaixaImagem()

            self.__criarButtonProdutos()
            self.__criarButtonProdutosImagem()

            self.__criarBtnVoltar()

        elif self.__cargo == "Administrador":
            self.__criarButtonCaixa()
            self.__criarButtonCaixaImagem()

            self.__criarButtonProdutos()
            self.__criarButtonProdutosImagem()

            self.__criarButtonPedidos()
            self.__criarButtonPedidosImagem()

            self.__criarButtonFornecedores()
            self.__criarButtonFornecedoresImagem()

            self.__criarButtonLucros()
            self.__criarButtonLucrosImagem()

            self.__criarButtonPromocoes()
            self.__criarButtonPromocoesImagem()

            self.__criarButtonGerenciar()
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
 """
