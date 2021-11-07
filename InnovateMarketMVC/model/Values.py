class setValuesProduto():
    def __init__(self, id, preco, nome, fornecedor):
        self.id = id
        self.preco = preco
        self.nome = nome
        self.fornecedor = fornecedor
        

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
