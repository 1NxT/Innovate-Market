import sqlite3

class MySql: 
    def conectar(self):
        banco = sqlite3.connect('__init__\data.db')
        cursor = banco.cursor()
        self.__cursor = cursor
        return self.__cursor
