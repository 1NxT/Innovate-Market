from Classes.MySql import *
from Classes.Usuario import *


class UsuarioDB():
    def __init__(self):
        cursor = MySql().conectar()
        self.cursor = cursor

    def pegarUsuario(self, cpf) -> Usuario:
        if not cpf:
            return None
        else:
            self.cursor.execute("SELECT * FROM user WHERE CPF = ?", (cpf))
            resultado1 = self.cursor.fetchone()

            if resultado1 == None:
                return None
            else:
                return Usuario(resultado1[0], resultado1[1], Cargo(resultado1[2]), resultado1[3], resultado1[4])
