from tkinter import *
import tkinter.ttk as ttk

class Fornecedor(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.telaforne = Toplevel()
        self.geometry()


        self.elementos()

    def geometry(self):
        self.telaforne.title("Fornecedor")
        self.telaforne.geometry("1360x760")
        self.telaforne.configure(bg="DodgerBlue")
        self.telaforne.resizable(False, False)    
        self.telaforne.iconbitmap('__init__\Imagens\logo.ico')

    def voltar_inicial_forne(self):
        self.telaforne.destroy()
        return

    def elementos(self):
        btn_telainicial_forne = Button(self.telaforne, text="Voltar Para Tela Inicial", command=self.voltar_inicial_forne,bg="red")
        btn_telainicial_forne.place(x=1100, y=700)
    

        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_forne_frame = Frame(self.telaforne, padx=1, pady=5, bg="DodgerBlue")
        tree_forne_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_forne_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_forne = ttk.Treeview(tree_forne_frame, column=("1","2","3","4","5"), show='headings', height=35, yscrollcommand=scroll.set)
        tree_forne.pack()

        scroll.config(command=tree_forne.yview)

        tree_forne.heading('#1', text="Nome", anchor=CENTER)
        tree_forne.heading('#2', text="CNPJ", anchor=CENTER)
        tree_forne.heading('#3', text="Telefone", anchor=CENTER)
        tree_forne.heading('#4', text="Endereco", anchor=CENTER)
        tree_forne.heading('#5',text="Produto Fornecido", anchor=CENTER)
        

        ent_pesquisar = Entry(self.telaforne)
        ent_pesquisar.place(x=1100, y=20)

        btn_pesquisar_pedi = Button(self.telaforne, text="Pesquisar")
        btn_pesquisar_pedi.place(x=1000, y=20)

        btn_show = Button(self.telaforne, text="Mostrar todos")
        btn_show.place(x=1200,y=100)

    


