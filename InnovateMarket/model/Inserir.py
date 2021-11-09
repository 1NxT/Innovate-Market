from model.DB import *


class Inserir():
    def __init__(self):
        self.__cursor = DB().cursor()

    def salvarProdutos(self, valores):
        self.__cursor.execute("INSERT INTO produtos(ID, preco, nome) VALUES (?, ? , ?);", (valores.get('cod'), valores.get('preco'), valores.get('nome')))
        self.__cursor.execute("commit;")
        DB().closeCursor()

    def salvarFornecedor(self, valores):
        self.__cursor.execute("INSERT INTO fornecedores(CNPJ, nome_fornecedor, telefones, email) VALUES (?, ? , ?, ?);", (valores.get('CNPJ'), valores.get('nome'), valores.get('telefone'), valores.get('email')))
        self.__cursor.execute("commit;")
        DB().closeCursor()

    def salvarProdutoCaixa(self, valores):
        self.__cursor.execute("INSERT INTO caixaCompras (CodigoCompra, Nome_Produto, Qtd, CodigoProduto, Valores) VALUES (?, ?, ?, ?, ?)", (valores.get('CodigoCompra'), valores.get('nomeProduto'), valores.get('Qtd'), valores.get('CodigoProduto'), valores.get('valorProduto')))
        self.__cursor.execute("commit;")
        DB().closeCursor()
    
    def salvarVenda(self, valores):
        self.__cursor.execute("INSERT INTO Vendas (CodigoCompra, NomeProduto, Qtd, CodigoProduto, Data) VALUES (?, ?, ?, ?, ?)", (valores.get('CodigoCompra'), valores.get('nomeProduto'), valores.get('Qtd'), valores.get('CodigoProduto'), valores.get('Data')))
        self.__cursor.execute("commit;")
        DB().closeCursor()
    
    def salvarUsuario(self, valores):
        self.__cursor.execute("INSERT INTO user (CPF, password, Cargo, Nome) VALUES (?, ?, ?, ?)", (valores.get('CPF'), valores.get('password'), valores.get('Cargo'), valores.get('Nome')))
        self.__cursor.execute("commit;")
        DB().closeCursor()
        
    def salvarPedidos(self, valores):
        self.__cursor.execute("INSERT INTO pedidos (ID, produtos, data, valores) VALUES (?, ?, ?, ?)", (valores.get('ID'), valores.get('produtos'), valores.get('data'),valores.get('valores')))
        self.__cursor.execute("commit;")
        DB().closeCursor()
        
    def salvar(self, tabela, valores):
        print(valores)
        self.__cursor.execute("INSERT INTO {} VALUES ({})".format(tabela, ", ".join(value for value in valores.values())))
        self.__cursor.execute("commit;")
        DB().closeCursor()
