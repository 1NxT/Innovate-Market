from model.DB import *
from model.Usuario import *

class UsuarioDB():
    def __init__(self):
        self.__cursor = DB().cursor()

    def pegarUsuario(self, cpf) -> Usuario:
        if not cpf:
            return None
        else:
            self.__cursor.execute("SELECT * FROM user WHERE CPF = ?", (cpf,))
            resultado1 = self.cursor.fetchone()
            DB().closeCursor()

            #verificação de user
            if resultado1 == None:
                return False
            else:
                return Usuario(resultado1[0], resultado1[1], Cargo(resultado1[2]), resultado1[3], resultado1[4])
