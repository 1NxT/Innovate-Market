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


        self.pathBg = imagespath / "gerenciar_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.telageren, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_pedi = Button(self.telageren, image=self.btn_voltartelainicial, command=self.tela_inicial_gerenciar, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pedi.place(x=980, y=660)

       

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_gere_frame = Frame(self.telageren, padx=1, pady=5, bg="lightgrey")
        self.tree_gere_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_gere_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_gere = ttk.Treeview(self.tree_gere_frame, columns=("1","2","3","4"), show="headings",height=35, yscrollcommand=self.scroll.set)
        self.tree_gere.pack()

        self.scroll.config(command=self.tree_gere.yview)

        self.tree_gere.heading('#1',text="Nome ", anchor=CENTER)
        self.tree_gere.heading('#2',text="Senha Do Usuario", anchor=CENTER)
        self.tree_gere.heading('#3',text="CPF do Usuario", anchor=CENTER)
        self.tree_gere.heading('#4',text="Cargo", anchor=CENTER)
        self.view_tree()

        self.ent_pesquisar = Entry(self.telageren,bg="lightgrey", font= "arial 18", width= "25")
        self.ent_pesquisar.place(x=860,y=80)

        self.ent_nome = Entry(self.telageren,bg="lightgrey",font= "arial 18", width= "25")
        self.ent_nome.place(x=860,y=200)
        
        self.ent_senha = Entry(self.telageren,bg="lightgrey",font= "arial 18", width= "25")
        self.ent_senha.place(x=860,y=320)

        self.ent_cpf = Entry(self.telageren,bg="lightgrey",font= "arial 18", width= "25")
        self.ent_cpf.place(x=860,y=470)

        self.ent_cargo = Entry(self.telageren,bg="lightgrey",font= "arial 18", width= "25")
        self.ent_cargo.place(x=860,y=610)
    

