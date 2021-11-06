from model.UsuarioDB import *
from model.Pesquisar import *
from model.Mostrar import *
from model.Inserir import *
from model.ValuesDB import *
from model.Deletar import *
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

        
class pesquisarControler():
    def pesquisarProdutos(self, valoresProdutos):
        resultado = Pesquisar().pesquisar(valoresProdutos, "produtos", "ID")
        return resultado

    def pesquisarFornecedor(self, valoresFornecedor):
        resultado = Pesquisar().pesquisar(valoresFornecedor, "fornecedor", "nome")
class inserirControler():
    def inserirProduto(self, tabela, values):
        Inserir().salvar(tabela, values)

class deletarControler():
    def deletarProduto(self, valorID):
        Deletar().deletar("produtos", "ID", valorID)

class mostarControler():
    def mostarProdutos(self):
        resultado = Mostrar().mostrar("produtos", "ID")
        return resultado
    
    def mostarFornecedor(self):
        resultado = Mostrar().mostrar("fornecedores", "CNPJ")
        return resultado

class valuesControler():
    def valuesProdutos(self, valores):
        self.__values = ValuesDB().carregarValues(valores)
        return self.__values
