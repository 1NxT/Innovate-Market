from tkinter import *
from tkinter import messagebox
import time
from tkinter import font
from Classes.UsuarioDB import UsuarioDB
from Pages.SegundaTela import *
from Pages.common.Config import *

class Principal(Frame):
    def __init__(self):
        self.tk = Tk()
        #self.tk.attributes("-fullscreen", True)
        self.logo = imagespath / "Logo.png"
        self.img = PhotoImage(file=self.logo)
        self.geometry()
        self.elementos()
        self.tk.mainloop()

    def iExit(self):
        self.result = messagebox.askquestion(
            'AVISO', 'Tem certeza que deseja sair?', icon="warning")
        if self.result == "yes":
            self.tk.destroy()
        return

    def geometry(self):
        self.tk.title("Tela de login")
        self.tk.geometry("1360x768")
               
        self.tk.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        #self.tk.iconbitmap(self.__iconImagemPath)
        
    def chamarLogar(self):
        usuario = UsuarioDB().pegarUsuario(str(self.ent_login.get()))

        self.lbl_dadosUsuario["text"] = ""
        self.lbl_dadosUsuario["text"] = ""
        if usuario == None:
            self.lbl_dadosUsuario["text"] = "Dados de usuário incorretos!"

        if not self.ent_senha.get():
            self.lbl_dadosSenha["text"] = "Dados de senha incorretos!"
        elif usuario.verificarSenha(self.ent_senha.get()):
            self.lbl_dadosSenha["text"] = "Dados de senha incorretos!"
        else:
            SegundaTela(usuario)
        
    def elementos(self):
        # LABELS 1° TELA
        self.pathBg = imagespath / "Tela de login1.png"
        self.__bg = PhotoImage(file =self.pathBg)

        self.lblimgbg = Label(self.tk, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.lbl_dadosUsuario = Label(self.tk, text="", bg="GhostWhite", font="Arial 18", fg="red")
        self.lbl_dadosUsuario.place(x=720, y=330)

        self.lbl_dadosSenha = Label(self.tk, text="", bg="GhostWhite", font="Arial 18", fg="red")
        self.lbl_dadosSenha.place(x=720, y=525)
        

        #ENTRYS 1° TELA
        self.ent_login = Entry(self.tk, font=("arial", 28), width=20)
        self.ent_login.place(x=720, y=280)

        self.ent_senha = Entry(self.tk, font=("arial", 28), width=20, show="*")
        self.ent_senha.place(x=720, y=475)

        self.__buttonEntrarImagemPath = imagespath / "Entrar.png"
        self.__buttonEntrarImagem = PhotoImage(file=self.__buttonEntrarImagemPath)
        self.btn_entrar = Button(self.tk, text="Entrar",  image=self.__buttonEntrarImagem, command=self.chamarLogar, borderwidth = 0)
        self.btn_entrar.place(x=730, y=600)

        self.__buttonSairImagemPath = imagespath / "Sair.png"
        self.__buttonSairImagem = PhotoImage(file=self.__buttonSairImagemPath)
        self.btn_sair = Button(self.tk, text="Sair", image=self.__buttonSairImagem, command=self.iExit, borderwidth = 0)
        self.btn_sair.place(x=990, y=600)
