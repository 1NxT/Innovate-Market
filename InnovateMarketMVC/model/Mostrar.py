from model.DB import *



class Mostrar():
    def __init__(self):
        self.__cursor = DB().cursor()

    def mostrar(self, tabela, coluna):

        self.__cursor.execute(f"SELECT * FROM {tabela} ORDER BY {coluna} ASC")
        resultado = self.__cursor.fetchall()
        DB().closeCursor()
        return resultado
