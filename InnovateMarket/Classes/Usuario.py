from enum import Enum

class Cargo(Enum):
    CAIXA = "1"
    ADMINISTRADOR = "2"

class Usuario:

    def __init__(self, cpf, password, cargo:Cargo , caixa, nome ):
        self.cpf = cpf
        self.password = password
        self.cargo = cargo 
        self.nome = nome
    
    def verificarSenha(self, Userpassword) -> bool:
        if self.password != Userpassword:
            print("Falso")
            print(self.password)
            print(Userpassword)
            return True
        else:
            print("True")
            print(self.password)
            print(Userpassword)
            return False
