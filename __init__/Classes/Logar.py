from Classes.MySql import *
class Logar():
    def __init__(self):
        self.cursor = MySql().concectar()

    def login(user, password):
        self.cursor.execute(f"SELECT * FROM usuarios WHERE login = {user}")
        resultado1 = self.cursor.fetchone()
        self.cursor.execute(f"SELECT * FROM usuarios WHERE senha = {password}")
        resultado2 = self.cursor.fetchone()

        if resultado1 == None:
            return True
        elif resultado2 == None:
            return True
