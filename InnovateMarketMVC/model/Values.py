class setValuesProduto():
    def __init__(self, id, preco, nome):
        self.id = str(id)
        self.preco = str(preco)
        self.nome = str(nome)
        

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
