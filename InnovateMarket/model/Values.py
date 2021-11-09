class setValuesProduto():
    def __init__(self, id, preco, nome):
        self.id = id
        self.preco = preco
        self.nome = nome
        print(self.id, self.preco, self.nome)
        

class setValuesFornecedor():
    def __init__(self, cnpj, nome, telefone, email):
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.email = email


class setValuesProdutosCaixa():
    def __init__(self, CodigoCompra, NomeProduto, Qtd, CodigoProduto):
        self.CodigoCompra = CodigoCompra
        self.NomeProduto = NomeProduto
        self.Qtd = Qtd
        self.CodigoProduto = CodigoProduto

class setValuesPedidos():
    def __init__(self, ID, produtos, data, valores):
        self.ID = ID
        self.produtos = produtos
        self.data = data
        self.valores = valores