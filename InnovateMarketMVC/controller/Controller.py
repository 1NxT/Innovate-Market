from model.UsuarioDB import *
from model.Pesquisar import *
from model.Mostrar import *
from model.Inserir import *
from model.ValuesDB import *
from model.Deletar import *
from model.Update import *
class usuarioControler():
    def usuarioLogar(self, cpf, senha):
        #verifica se o user existe no DB
        self.__usuario = UsuarioDB().pegarUsuario(cpf)
        if self.__usuario == None:
            return None
        else:
            #verifica se a senha está correta
            self.__usuarioSenhaOK = self.__usuario.verificarSenha(senha)
            if self.__usuarioSenhaOK:
                print(self.__usuario)
                return self.__usuario
            else:
                return "SENHA ERRADA"

class produtosControler():
    def pesquisarProdutos(self, valoresProdutos):
        resultado = Pesquisar().pesquisar(valoresProdutos, "produtos", "ID")
        return resultado

    def inserirProduto(self, values):
        Inserir().salvar("produtos",  values)
    
    def deletarProduto(self, valorID):
        Deletar().deletar("produtos", "ID", valorID)

    def mostarProdutos(self):
        resultado = Mostrar().mostrar("produtos", "ID")
        return resultado

    def valuesProdutos(self, valores):
        self.__values = ValuesDB().carregarValues(valores)
        return self.__values

    def atualizarProdutos(self, valores, id):
        Update().salvar("produtos", valores, id)

class fornecedorControler():
    def pesquisarFornecedor(self, valoresFornecedor):
        resultado = Pesquisar().pesquisar(valoresFornecedor, "fornecedor", "nome")
        return resultado

    def mostarFornecedor(self):
        resultado = Mostrar().mostrar("fornecedores", "CNPJ")
        return resultado

class promocoesControler():
    def pesquisarPromocoes(self, valoresPromocao):
        resultado = Pesquisar().pesquisar(valoresPromocao, "promocoes", "ID")
        return resultado

    def mostarPromocoes(self):
        resultado = Mostrar().mostrar("cupons", "ID")
        return resultado

    
class caixaControler():
    def mostarCaixa(self):
        resultado = Mostrar().mostrar("caixa", "ID")
        return resultado

    def pesquisarPromocoes(self, valoresCaixa):
        resultado = Pesquisar().pesquisar(valoresCaixa, "caixa", "ID")
        return resultado

class pedidosControler():
    def mostarPedido(self):
        resultado = Mostrar().mostrar("pedidos", "ID")
        return resultado

    def pesquisarPedido(self, valoresPedidos):
        resultado = Pesquisar().pesquisar(valoresPedidos, "pedidos", "ID")
        return resultado

class gerenciarControler():
    def mostarGerenciar(self):
        resultado = Mostrar().mostrar("user", "CPF")
        return resultado

    def pesquisarGerenciar(self, valoresGerenciar):
        resultado = Pesquisar().pesquisar(valoresGerenciar, "user", "CPF")
        return resultado
