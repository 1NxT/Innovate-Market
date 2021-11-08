from model.DB import *


class Inserir():
    def __init__(self):
        self.__cursor = DB().cursor()

    def salvarProdutos(self, valores):
        self.__cursor.execute(f"INSERT INTO produtos(ID, preco, nome) VALUES (?, ? , ?);", (valores.get('cod'), valores.get('preco'), valores.get('nome')))
        self.__cursor.execute("commit;")
        DB().closeCursor()

    def salvarFornecedor(self, valores):
        self.__cursor.execute(f"INSERT INTO fornecedores(CNPJ, nome_fornecedor, telefones, email) VALUES (?, ? , ?, ?);", (valores.get('CNPJ'), valores.get('nome'), valores.get('telefone'), valores.get('email')))
        self.__cursor.execute("commit;")
        DB().closeCursor()

    def salvarProdutoCaixa(self, valores):
        self.__cursor.execute(f"INSERT INTO caixaCompras (CodigoCompra, Nome_Produto, Qtd, CodigoProduto) VALUES (?, ?, ?, ?)", (valores.get('CodigoCompra'), valores.get('nomeProduto'), valores.get('Qtd'), valores.get('CodigoProduto')))
        self.__cursor.execute("commit;")
        DB().closeCursor()
    
    def salvarVenda(self, valores):
        self.__cursor.execute(f"INSERT INTO Vendas (CodigoCompra, NomeProduto, Qtd, CodigoProduto, Data) VALUES (?, ?, ?, ?, ?)", (valores.get('CodigoCompra'), valores.get('nomeProduto'), valores.get('Qtd'), valores.get('CodigoProduto'), valores.get('Data')))
        self.__cursor.execute("commit;")
        DB().closeCursor()

    def salvar(self, tabela, valores):
        print(valores)
        self.__cursor.execute("INSERT INTO {} VALUES ({})".format(tabela, ", ".join(value for value in valores.values())))
        self.__cursor.execute("commit;")
        DB().closeCursor()
