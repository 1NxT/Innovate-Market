import tkinter as tk
from model.DB import *



class Pesquisar():
    def __init__(self):
        self.__cursor = DB().cursor()

    def pesquisar(self, pesquisa, tabela, coluna):
        keys = list(pesquisa)
        if tabela == "fornecedor":
            self.__cursor.execute(f"SELECT * FROM {tabela} WHERE {keys[0]} LIKE '%{pesquisa[keys[0]]}%' OR {keys[1]} LIKE '%{pesquisa[keys[1]]}%' OR {keys[2]} LIKE '%{pesquisa[keys[2]]}%' OR {keys[3]} LIKE '%{pesquisa[keys[3]]}%' OR {keys[4]} LIKE '%{pesquisa[keys[4]]}%' ORDER BY {coluna}")
        elif tabela == "caixa":
            self.__cursor.execute(f"SELECT ID, preco, nome FROM produtos WHERE ID LIKE '%{pesquisa}%' ")
        elif tabela == "caixaFinalizar":
            self.__cursor.execute(f"SELECT * FROM caixaCompras WHERE CodigoCompra = {pesquisa}")
        elif tabela == "Vendas":
            self.__cursor.execute(f"SELECT * FROM {tabela} WHERE {keys[0]} LIKE '%{pesquisa[keys[0]]}%' OR {keys[1]} LIKE '%{pesquisa[keys[1]]}%' OR {keys[2]} LIKE '%{pesquisa[keys[2]]}%' OR {keys[3]} LIKE '%{pesquisa[keys[3]]}%' OR {keys[4]} LIKE '%{pesquisa[keys[4]]}%' ORDER BY {coluna}")
        else:
            self.__cursor.execute(f"SELECT * FROM {tabela} WHERE {keys[0]} LIKE '%{pesquisa[keys[0]]}%' OR {keys[1]} LIKE '%{pesquisa[keys[1]]}%' OR {keys[2]} LIKE '%{pesquisa[keys[2]]}%' OR {keys[3]} LIKE '%{pesquisa[keys[3]]}%' ORDER BY {coluna}")

        resultado = self.__cursor.fetchall()
        DB().closeCursor()

        return resultado
