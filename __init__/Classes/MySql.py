import sqlite3
class MySql():
    def __init__(self):
        self.conectar()
        
    def conectar(self):
        banco = sqlite3.connect('Innovate-Market-main\__init__\data.db')
        cursor = banco.cursor()
        self.__cursor = cursor
        return self.__cursor
