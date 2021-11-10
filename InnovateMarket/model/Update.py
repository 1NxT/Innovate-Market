from model.DB import *

class Update():
    def __init__(self):
        self.__cursor = DB().cursor()

    def salvar(self, tabela, valores, whereParameter):
        if tabela == "produtos":
            print(valores.nome)
            print(valores.id)
            print(valores.preco)
            self.__cursor.execute(f"UPDATE produtos SET nome = '{valores.nome}', preco = '{valores.preco}', ID = '{valores.id}' WHERE ID = {whereParameter};")
            self.__cursor.execute("commit;")
            DB().closeCursor()
        elif tabela == "fornecedores":
            self.__cursor.execute(f"UPDATE fornecedores SET CNPJ = '{valores.cnpj}', nome_fornecedor = '{valores.nome}', telefones = '{valores.telefone}', email = '{valores.email}' WHERE CNPJ = {whereParameter};")
            self.__cursor.execute("commit;")
            DB().closeCursor()
        elif tabela == "pedidos":
            self.__cursor.execute(f"UPDATE pedidos SET ID = '{valores.ID}', produtos = '{valores.produtos}', data = '{valores.data}', valores = '{valores.valores}' WHERE ID = {whereParameter};")
            self.__cursor.execute("commit;")
            DB().closeCursor()
