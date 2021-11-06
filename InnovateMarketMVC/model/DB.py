from model.ConectarDB import *

class DB():
    def __init__(self):
        self.__banco = ConectarBanco().conectar()
        self.__cursor = self.__banco.cursor()

    def commit(self):
        self.__banco.commit()

    def cursor(self):
        return self.__cursor
    
    def closeCursor(self):
        self.__cursor.close()

    
