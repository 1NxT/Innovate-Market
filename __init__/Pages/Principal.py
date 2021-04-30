from tkinter import *
from Classes.Logar import *
class Principal():
    def __init__(self):
        self.tk = Tk()
        self.img = PhotoImage(file="Innovate-Market-main\__init__\Imagens\Logo.png")
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
        self.tk.iconbitmap('Innovate-Market-main\__init__\Imagens\logo.ico')

    def elementos(self):
        lbl_login = Label(self.tk, text="Login: ",font="arial 18", bg="DodgerBlue", width=6)


        lbl_login.place(x=150, y=295)

        lbl_senha = Label(self.tk, text="Senha: ", font="arial 18", bg="DodgerBlue")
        lbl_senha.place(x=150, y=350)

        lbl_imagem = Label(self.tk, image=self.img,
                           width=280, height=240, bg="DodgerBlue")
        lbl_imagem.place(x=175, y=0)

        lbl_dados = Label(self.tk, text="", bg="DodgerBlue", font="arial 18", fg="red")
        lbl_dados.place(x=140, y=400)
        #ENTRYS 1° TELA
        ent_login = Entry(self.tk, font=("arial", 12), width=18)
        ent_login.place(x=240, y=300)

        ent_senha = Entry(self.tk, font=("arial", 12), width=18, show="*")
        ent_senha.place(x=240, y=355)

        # #BUTTONS 1° TELA
        btn_entrar = Button(self.tk, text="Entrar", command=Logar().login(ent_login.get(), ent_senha.get()),width=30, height=2, bg="cyan")
        btn_entrar.place(x=190, y=450)


        btn_sair = Button(self.tk, text="Sair", command=self.iExit, width=15, bg="firebrick")
        btn_sair.place(x=430, y=550)
        
        
