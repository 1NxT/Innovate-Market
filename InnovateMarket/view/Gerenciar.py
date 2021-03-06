from tkinter import * 
import tkinter.ttk as ttk
from tkinter import messagebox
from controller.Controller import gerenciarControler 
from model.Config import *

class Gerenciar():
    def __init__(self):
        self.telageren = Toplevel()
        self.telageren.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.telageren.title("Gerenciar Usuarios ")
        self.telageren.geometry("1360x760")
        self.telageren.configure(bg="Lightgrey")
        self.telageren.resizable(False, False)
        self.options = ["Caixa", "Adiministrador"]
        self.itemVariable = StringVar()
        self.itemVariable.set(self.options[0])
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.telageren.iconbitmap(self.__iconImagemPath)

    # def tela_inicial_gerenciar(self):
    #         cadastro_usuario.destroy()
    #         return
    
    def deleteElemento(self):
        if not self.tree_gere.focus():
            messagebox.showwarning(
                title="ERRO!", message="Selecione uma opção para deletar!", parent=self.telaprodutos)
        else:
            self.currItem = self.tree_gere.focus()
            self.values = gerenciarControler().usuarioValue(
                self.tree_gere.item(self.currItem)['values'])
            self.tree_gere.delete(self.currItem)
            gerenciarControler().deletarUser(self.values.CPF)
            
    
        
    def mostrarDados(self):
        resultado = gerenciarControler().mostarGerenciar()
        if resultado != None:
            self.tree_gere.delete(*self.tree_gere.get_children())
            
            for i in resultado:
                i = list(i)
                if i[2] == "1":
                    i[2] = "Caixa"
                elif i[2] == "2":
                    i[2] = "Adiministrador"
                self.tree_gere.insert("","end",values=i)
        else:
            print("Error!")

    def tela_inicial_gerenciar(self):
        self.telageren.destroy()
        return

    # Função para procurar por dados na Treeview        
    def chamaPesquisar(self):
        resultado = gerenciarControler().pesquisarGerenciar(self.ent_pesquisar.get(), "usuarios")
        
        if resultado != None:
            self.tree_gere.delete(*self.tree_gere.get_children())
            
            for i in resultado:
                
                self.tree_gere.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")

    def adicionarNovoUsuario(self):
        self.cargoselecionado = self.itemVariable.get()
        if self.cargoselecionado == "Caixa":
            self.cargoselecionado = "1"
        else: 
            self.cargoselecionado = "2"
        self.dicti = {}
        self.dicti["CPF"] = self.ent_cpf.get()
        self.dicti["password"] = self.ent_senha.get()
        self.dicti["Cargo"] = self.cargoselecionado
        self.dicti["Nome"] = self.ent_nome.get()
        
        gerenciarControler().inserirUsuario(self.dicti)
        
        self.mostrarDados()
        
    def elementos(self):
        self.pathBg = imagespath / "gerenciar_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.telageren, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        
        self.btn_telainicial = imagespath / "voltar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_pedi = Button(self.telageren, image=self.btn_voltartelainicial, command=self.tela_inicial_gerenciar, relief="flat", borderwidth=0, width=224, height=50, bg="Gainsboro")
        self.btn_telainicial_pedi.place(x=940, y=668)

        self.img_pesquisar = imagespath / "pesquisar.png"
        self.btn_pesquisar = PhotoImage(file =self.img_pesquisar)
        self.btn_pesquisar_gere = Button(self.telageren, image=self.btn_pesquisar, command=self.chamaPesquisar, relief="flat", borderwidth=0, width=105, height=50)
        self.btn_pesquisar_gere.place(x=1235, y=60)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_show = Button(self.telageren, command=self.adicionarNovoUsuario, image=self.btn_adicionar, relief="flat", borderwidth=0, bg="Gainsboro")
        self.btn_show.place(x=1050, y=600)
        
        self.img_deletar = imagespath / "deletar.png"
        self.btn_deletar = PhotoImage(file =self.img_deletar)
        self.btn_show = Button(self.telageren, command=self.deleteElemento, image=self.btn_deletar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_show.place(x=850, y=600)
        
        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_gere_frame = Frame(self.telageren, padx=1, pady=5, bg="lightgrey")
        self.tree_gere_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_gere_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_gere = ttk.Treeview(self.tree_gere_frame, columns=("1","2","3","4"), show="headings",height=28, yscrollcommand=self.scroll.set)
        self.tree_gere.pack()

        self.scroll.config(command=self.tree_gere.yview)

        self.tree_gere.heading('#1',text="CPF ", anchor=CENTER)
        self.tree_gere.heading('#2',text="Senha Do Usuario", anchor=CENTER)
        self.tree_gere.heading('#3',text="Cargo", anchor=CENTER)
        self.tree_gere.heading('#4',text="Nome", anchor=CENTER)
        self.mostrarDados()

        # ENTRYS GEERENCIAR
        self.ent_pesquisar = Entry(self.telageren,bg="lightgrey", font= "arial 18", width= "25")
        self.ent_pesquisar.place(x=900,y=70)

        self.ent_nome = Entry(self.telageren,bg="lightgrey",font= "arial 18", width= "25")
        self.ent_nome.place(x=900,y=205)
        
        self.ent_senha = Entry(self.telageren,bg="lightgrey",font= "arial 18", width= "25")
        self.ent_senha.place(x=900,y=320)

        self.ent_cpf = Entry(self.telageren,bg="lightgrey",font= "arial 18", width= "25")
        self.ent_cpf.place(x=900,y=440)

        

        self.menu_quantidade = OptionMenu(self.telageren, self.itemVariable, *self.options)
        self.menu_quantidade.place(x=900,y=550)
    


