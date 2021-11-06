from model.UsuarioDB import *
class usuarioControler():
    def usuarioLogar(self, cpf, senha):
        #verifica se o user existe no DB
        self.__usuario = UsuarioDB().pegarUsuario(cpf)
        if self.__usuario:
            return "User ERRADO"
        
        #verifica se a senha está correta
        self.__usuario = self.__usuario.verificarSenha(senha)
        if self.__usuario:
            return self.__usuario
        else:
            return "SENHA ERRADA"

        
class pesquisarControler():
    def pesquisar(self):
        pass

class inserirControler():
    def inserir(self):
        pass

class deletarControler():
    def deletar(self):
        pass

class mostarControler():
    def mostar():
        pass

class valuesControler():
    def values():
        pass