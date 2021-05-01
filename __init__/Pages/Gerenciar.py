from tkinter import *
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
        self.telageren.iconbitmap('__init__\Imagens\logo.ico')

    def tela_inicial_gerenciar(self):
            cadastro_usuario.destroy()
            return

    def elementos(self):

        btn_sair_gere = Button(self.telageren,text="Voltar para a tela inicial", font="arial 12",bg="red",command=self.tela_inicial_gerenciar)
        btn_sair_gere.place(x=1100,y=700)

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_gere_frame = Frame(self.telageren, padx=1, pady=5, bg="DodgerBlue")
        tree_gere_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_gere_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_gere = ttk.Treeview(tree_gere_frame, columns=("1","2"), show="headings",height=35, yscrollcommand=scroll.set)
        tree_gere.pack()

        scroll.config(command=tree_gere.yview)

        tree_gere.heading('#1',text="Nome De Usuario", anchor=CENTER)
        tree_gere.heading('#2',text="Senha Do Usuario", anchor=CENTER)
        

        lbl_nome = Label(self.telageren,text="Nome Do Usuario: ",font="arial 12")
        lbl_nome.place(x=400,y=100,relwidth=0.17)

        ent_nome = Entry(self.telageren,bg="lightgrey")
        ent_nome.place(x=700,y=100,relwidth=0.24)
    
        lbl_senha= Label(self.telageren,text="Senha: ",font="arial 12")
        lbl_senha.place(x=500,y=200,relwidth=0.07)

        ent_senha = Entry(self.telageren,bg="lightgrey")
        ent_senha.place(x=700,y=200,relwidth=0.24)

        lbl_erro = Label(self.telageren,text="", font="arial 12 ", fg="green", bg="DodgerBlue")
        lbl_erro.place(x=500,y=300,relwidth=0.17)
        
        btn_enviar = Button(self.telageren,text="Salvar Dados", font="arial 12")
        btn_enviar.place(x=500,y=400,relwidth=0.24)


        btn_excluir = Button(self.telageren,text="Excluir", font="arial 12")
        btn_excluir.place(x=500,y=500,relwidth=0.24)

