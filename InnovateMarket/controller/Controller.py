from datetime import datetime
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
                return self.__usuario
            else:
                return "SENHA ERRADA"

class produtosControler():
    def pesquisarProdutos(self, valoresProdutos):
        resultado = Pesquisar().pesquisar(valoresProdutos, "produtos", "ID")
        return resultado

    def inserirProduto(self, values):
        cadastroValido = True
        for value in values.values():
            
            if value == "Vazio!":
                cadastroValido = False
        
        if cadastroValido:
            Inserir().salvarProdutos(values)
            return True
        else:
            return False
    def deletarProduto(self, valorID):
        Deletar().deletar("produtos", "ID", valorID)

    def mostarProdutos(self):
        resultado = Mostrar().mostrar("produtos", "ID")
        return resultado

    def valuesProdutos(self, valores):
        self.__values = ValuesDB().carregarValues("produtos", valores)
        return self.__values

    def atualizarProdutos(self, valores, id):
        Update().salvar("produtos", valores, id)

class fornecedorControler():
    def pesquisarFornecedor(self, valoresFornecedor):
        resultado = Pesquisar().pesquisar(valoresFornecedor, "fornecedores", "CNPJ")
        return resultado

    def inserirFornecedor(self, values):
        cadastroValido = True
        for value in values.values():
            if value == "Vazio!":
                cadastroValido = False
        
        if cadastroValido:
            Inserir().salvarFornecedor(values)
            return True
        else:
            return False
            
    def deletarFornecedor(self, valorID):
        Deletar().deletar("fornecedores", "CNPJ", valorID)

    def mostarFornecedor(self):
        resultado = Mostrar().mostrar("fornecedores", "CNPJ")
        return resultado

    def atualizarFornecedor(self, valores, id):
        Update().salvar("fornecedores", valores, id)

    def valuesFornecedor(self, valores):
        self.__values = ValuesDB().carregarValues("fornecedor", valores)
        
        return self.__values
    
class caixaControler():
    def mostarCaixa(self):
        resultado = Mostrar().mostrar("caixaCompras", "CodigoCompra")
        return resultado

    def CaixaPesquisarProdutos(self, valoresProdutos):
        resultado = Pesquisar().pesquisar(valoresProdutos, "caixa", "ID")
        if len(resultado) != 1:
            return "Nenhum produto!"
        else:
            return resultado
    def caixaValues(self, valorCaixaProduto):
        self.values = ValuesDB().carregarValues("caixaCompras", valorCaixaProduto)
        return self.values

    def validarQuantidade(self, quantidade):
        return quantidade.isdigit()
            
    def validarValues(self, valores):
        valido = True
        for value in valores.values():
            
            if value == "Vazio!":
                valido = False
                return valido
            
        return valido

    def adicionarProdutoCaixa(self, valoresCaixa):
        Inserir().salvarProdutoCaixa(valoresCaixa)

    def deletarProduto(self, valorProdutoCaixa):
        Deletar().deletar("caixaCompras", "CodigoProduto", valorProdutoCaixa)

    def caixaAbortar(self, compraID):
        Deletar().deletar("caixaCompras", "CodigoCompra", compraID)

    def caixaFinalizarCompra(self, compraID):
        
        today = datetime.today().strftime('%d%m%Y')
        data = str(today)
        valoresCompra = Pesquisar().pesquisar(compraID, "caixaFinalizar", "CodigoCompra")
        
        for i in valoresCompra:
            self.dicti = {}
            
            self.dicti["CodigoCompra"] = compraID
            self.dicti["nomeProduto"] = str(i[1])
            self.dicti["Qtd"] = str(i[2])
            self.dicti["CodigoProduto"] = str(i[3])
            self.dicti["Data"] = data
            self.dicti["Valores"] = str(i[4])
            Inserir().salvarVenda(self.dicti)
        
        Deletar().deletar("caixaCompras", "CodigoCompra", compraID)

class pedidosControler():
    def mostarPedido(self):
        resultado = Mostrar().mostrar("pedidos", "ID")
        return resultado

    def pesquisarPedido(self, valoresPedidos):
        resultado = Pesquisar().pesquisar(valoresPedidos, "pedidos", "ID")
        return resultado
    
    def atualizarPedidos(self, valores, id):
        today = datetime.today().strftime('%d%m%Y')
        data = str(today)
        valores.data = data
        Update().salvar("pedidos", valores, id)

    def valuesPedidos(self, valores):
        self.__values = ValuesDB().carregarValues("pedidos", valores)
        
        return self.__values
    
    def inserirPedidos(self, values):
        today = datetime.today().strftime('%d%m%Y')
        data = str(today)
        values["data"] = data
        cadastroValido = True
        for value in values.values():
            if value == "Vazio!":
                cadastroValido = False

        if cadastroValido:
            Inserir().salvarPedidos(values)
            return True
        else:
            return False

    def deletarPedido(self, valorID):
        Deletar().deletar("pedidos", "ID", valorID)

class gerenciarControler():
    def mostarGerenciar(self):
        resultado = Mostrar().mostrar("user", "CPF")
        return resultado

    def pesquisarGerenciar(self, valoresGerenciar):
        resultado = Pesquisar().pesquisar(valoresGerenciar, "user", "CPF")
        return resultado
    
    def inserirUsuario(self, valoresUsuario):
        Inserir().salvarUsuario(valoresUsuario)

    def usuarioValue(self, valores):
        self.__values = ValuesDB().carregarValues("user", valores)

        return self.__values
    
    def deletarUser(self, valorID):
        Deletar().deletar("user", "CPF", valorID)
class vendasControler():
    def mostrarVendas(self):
        resultado = Mostrar().mostrar("vendas", "CodigoCompra")
        return resultado

    def pesquisarVendas(self, valoresVendas):
        resultado = Pesquisar().pesquisar(valoresVendas, "Vendas", "CodigoCompra")
        return resultado
