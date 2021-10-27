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
    
    def verificarSenha(self,password) -> bool:
        if self.password == password:
            return True
        else:
            return False
