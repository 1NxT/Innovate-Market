import sqlite3
from Pages.common.Config import *
class MySql: 
    def conectar(self):
        banco = sqlite3.connect(databasepath)
        cursor = banco.cursor()
        self.__cursor = cursor
        return self.__cursor
