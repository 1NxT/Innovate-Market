from model.DB import *


class Inserir():
    def __init__(self):
        self.__cursor = DB().cursor()


    def salvar(self, tabela, valores):
        print(valores)
        self.__cursor.execute("INSERT INTO {} VALUES ({})".format(tabela, ", ".join(value for value in valores.values())))
        self.__cursor.execute("commit;")
        DB().closeCursor()
