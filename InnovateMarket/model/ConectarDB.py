import sqlite3
from model.Config import *
class ConectarBanco():
    def conectar(self):
        self.banco = sqlite3.connect(databasepath)
        self.banco.commit()
        return self.banco