from model.DB import *


class Deletar():
    def __init__(self):
        self.__cursor = DB().cursor()

    def deletar(self, tabela: str, coluna: str, valor: int):
        self.__cursor.execute(f"DELETE FROM {tabela} WHERE {coluna} = {valor};")
        self.__cursor.execute("commit;")
        DB().closeCursor()
