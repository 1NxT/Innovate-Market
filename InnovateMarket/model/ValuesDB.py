from model.Values import *


class ValuesDB():
    def carregarValues(self, tabela, values):
        if tabela == "produtos":
            self.values = values
            return setValuesProduto(self.values[0], self.values[1], self.values[2])
        elif tabela == "fornecedor":
            self.values = values
            return setValuesFornecedor(self.values[0], self.values[1], self.values[2], self.values[3])
        elif tabela == "caixaCompras":
            self.values = values
            print(self.values)
            return setValuesProdutosCaixa(self.values[0], self.values[1], self.values[2], self.values[3], self.values[4])
        elif tabela == "pedidos":
            self.values = values
            return setValuesPedidos(self.values[0], self.values[1], self.values[2], self.values[3])
