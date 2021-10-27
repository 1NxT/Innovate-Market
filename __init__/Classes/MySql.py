import sqlite3
from Classes.Config import *
class MySql: 
    def conectar(self):
        banco = sqlite3.connect(Config().database())
        cursor = banco.cursor()
        self.__cursor = cursor
        return self.__cursor
