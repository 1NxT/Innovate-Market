from tkinter import *
import tkinter.ttk as ttk
from Classes.Pesquisar import *
from Classes.Mostrar import *
from Pages.common.Config import *

class Gerenciar :
    def __init__(self):
        self.telageren = Toplevel()
        self.geometry()

        self.elementos()

    def geometry(self):
        self.telageren.title("Gerenciar Usuarios ")
        self.telageren.geometry("1360x760")
        self.telageren.configure(bg="DodgerBlue")
        self.telageren.resizable(False, False)
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.telageren.iconbitmap(self.__iconImagemPath)

    # def tela_inicial_gerenciar(self):
    #         cadastro_usuario.destroy()
    #         return
        
    def view_tree(self):
        resultado = Mostrar().mostrar(self, "user", "CPF")
        
        if resultado != None:
            self.tree_gere.delete(*self.tree_gere.get_children())
            
            for i in resultado:
                self.tree_gere.insert("","end",values=i)
        else:
            print("Error!")

    def tela_inicial_gerenciar(self):
        self.telageren.destroy()
        return

    # Função para procurar por dados na Treeview        
    def chamaPesquisar(self):
        resultado = Pesquisar().pesquisar(self.ent_pesquisar.get(), "usuarios")

        if resultado != None:
            self.tree_gere.delete(*self.tree_gere.get_children())
            
            for i in resultado:
                self.tree_gere.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")

    def elementos(self):

        self.btn_sair_gere = Button(self.telageren,text="Voltar para a tela inicial", font="arial 12",bg="red",command=self.tela_inicial_gerenciar)
        self.btn_sair_gere.place(x=1100,y=700)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_gere_frame = Frame(self.telageren, padx=1, pady=5, bg="DodgerBlue")
        self.tree_gere_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_gere_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_gere = ttk.Treeview(self.tree_gere_frame, columns=("1","2"), show="headings",height=35, yscrollcommand=self.scroll.set)
        self.tree_gere.pack()

        self.scroll.config(command=self.tree_gere.yview)

        self.tree_gere.heading('#1',text="Nome De Usuario", anchor=CENTER)
        self.tree_gere.heading('#2',text="Senha Do Usuario", anchor=CENTER)
        self.view_tree()
        

        self.lbl_nome = Label(self.telageren,text="Nome Do Usuario: ",font="arial 12")
        self.lbl_nome.place(x=400,y=100,relwidth=0.17)

        self.ent_nome = Entry(self.telageren,bg="lightgrey")
        self.ent_nome.place(x=700,y=100,relwidth=0.24)
        
        self.ent_pesquisar = Entry(self.telageren,bg="lightgrey")
        self.ent_pesquisar.place(x=700,y=600)
    
        self.lbl_senha= Label(self.telageren,text="Senha: ",font="arial 12")
        self.lbl_senha.place(x=500,y=200,relwidth=0.07)

        self.ent_senha = Entry(self.telageren,bg="lightgrey")
        self.ent_senha.place(x=700,y=200,relwidth=0.24)

        self.lbl_erro = Label(self.telageren,text="", font="arial 12 ", fg="green", bg="DodgerBlue")
        self.lbl_erro.place(x=500,y=300,relwidth=0.17)
        
        self.btn_enviar = Button(self.telageren,text="Salvar Dados", font="arial 12")
        self.btn_enviar.place(x=500,y=400,relwidth=0.24)


        self.btn_excluir = Button(self.telageren,text="Excluir", font="arial 12")
        self.btn_excluir.place(x=500,y=500,relwidth=0.24)
