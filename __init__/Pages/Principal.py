from tkinter import *
import time
from Classes.Logar import Logar
from Pages.SegundaTela import *

class Principal(Frame):
    def __init__(self):
        self.tk = Tk()
        self.img = PhotoImage(file="__init__\Imagens\Logo.png")
        self.geometry()
        self.elementos()
        self.tk.mainloop()
        

    def iExit(self):
        self.tk.destroy()
        return

    def geometry(self):
        self.tk.title("Tela de login")
        self.tk.geometry("600x600")
        self.tk.configure(bg="DodgerBlue")
        self.tk.resizable(False, False)
        self.tk.iconbitmap('__init__\Imagens\logo.ico')
        

    def chamarLogar(self):
        resultado1 = Logar().login(self.ent_login.get(), self.ent_senha.get())
        
        if resultado1 != None:
            SegundaTela()
        else:
            self.lbl_dados["text"] = "Dados de usuário ou senha incorretos!"
            

    def elementos(self):
        # LABELS 1° TELA
        self.lbl_login = Label(self.tk, text="Login: ",font="arial 18", bg="DodgerBlue", width=6)
        self.lbl_login.place(x=150, y=295)

        self.lbl_senha = Label(self.tk, text="Senha: ", font="arial 18", bg="DodgerBlue")
        self.lbl_senha.place(x=150, y=350)

        self.lbl_imagem = Label(self.tk, image=self.img,width=280, height=240, bg="DodgerBlue")
        self.lbl_imagem.place(x=175, y=0)

        self.lbl_dados = Label(self.tk, text="", bg="DodgerBlue", font="arial 18", fg="red")
        self.lbl_dados.place(x=140, y=400)
        #ENTRYS 1° TELA
        self.ent_login = Entry(self.tk, font=("arial", 12), width=18)
        self.ent_login.place(x=240, y=300)

        self.ent_senha = Entry(self.tk, font=("arial", 12), width=18, show="*")
        self.ent_senha.place(x=240, y=355)


           
        # #BUTTONS 1° TELA
        self.btn_entrar = Button(self.tk, text="Entrar", command=self.chamarLogar, width=30, height=2, bg="cyan")
        self.btn_entrar.place(x=190, y=450)


        self.btn_sair = Button(self.tk, text="Sair", command=self.iExit, width=15, bg="firebrick")
        self.btn_sair.place(x=430, y=550)
