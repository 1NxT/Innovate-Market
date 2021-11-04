import sqlite3
from Pages.common.Config import *
class MySql: 

    def conectar(self):
        self.banco = sqlite3.connect(databasepath)
        self.banco.commit()
        cursor = self.banco.cursor()
        self.__cursor = cursor
        return self.__cursor

    