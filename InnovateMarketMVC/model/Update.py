from model.DB import *

class Update():
    def __init__(self):
        self.__cursor = DB().cursor()

    def salvar(self, tabela, valores, id):
        if tabela == "produtos":
            self.__cursor.execute(f"UPDATE produtos SET nome = {valores.nome}, preco = {valores.preco}, fornecedor = {valores.fornecedor}, ID = {valores.id} WHERE ID = {id};")
            self.__cursor.execute("commit;")
            DB().closeCursor()
        
