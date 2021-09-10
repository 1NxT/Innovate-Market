from tkinter import *
import tkinter.ttk as ttk
from Classes.MySql import *
from Classes.Pesquisar import *
from Classes.Mostrar import *

class Pedidos(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.telapedi = Toplevel()
        self.geometry()

        self.elementos()

    def geometry(self):
        self.telapedi.title("Pedidos")
        self.telapedi.geometry("1360x760")
        self.telapedi.configure(bg="DodgerBlue")
        self.telapedi.resizable(False, False)
        self.telapedi.iconbitmap('__init__\Imagens\logo.ico')

    def voltar_inicial_pedi(self):
            self.telapedi.destroy()
            return
        
    def clear_entry(self):
        self.ent_pesquisar.delete(0, END)
        self.ent_pesquisar.insert(0, "")
        
    def view_tree(self):
        resultado = Mostrar().mostrar(self, "pedidos", "id_pedido")
        
        if resultado != None:
            self.tree_pedi.delete(*self.tree_pedi.get_children())
            
            for i in resultado:
                self.tree_pedi.insert("","end",values=i)
        else:
            print("Error!")
    
    # Função para procurar por dados na Treeview        
    def chamaPesquisar(self):
        resultado = Pesquisar().pesquisar(self.ent_pesquisar.get(), "pedidos", "id_pedido")

        if resultado != None:
            self.tree_pedi.delete(*self.tree_pedi.get_children())
            
            for i in resultado:
                self.tree_pedi.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe") 

    def elementos(self):

        self.btn_telainicial_pedi = Button(self.telapedi, text="Voltar Para Tela Inicial", command=self.voltar_inicial_pedi,bg="red")
        self.btn_telainicial_pedi.place(x=1000, y=600)
        
        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_pedi_frame = Frame(self.telapedi, padx=1, pady=10, bg="DodgerBlue")
        self.tree_pedi_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pedi_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pedi = ttk.Treeview(self.tree_pedi_frame, column=("1","2","3","4"), show='headings', height=35, yscrollcommand=self.scroll.set)
        self.tree_pedi.pack()

        self.scroll.config(command=self.tree_pedi.yview)

        self.tree_pedi.heading('#1', text="Nome do produto", anchor=CENTER)
        self.tree_pedi.heading('#2', text="Cliente", anchor=CENTER)
        self.tree_pedi.heading('#3', text="Valor Total", anchor=CENTER)
        self.tree_pedi.heading('#4', text="Numero do Pedido", anchor=CENTER)
        self.view_tree()
     

        self.ent_pesquisar = Entry(self.telapedi)
        self.ent_pesquisar.place(x=1000, y=20)

        self.btn_pesquisar_pedi = Button(self.telapedi, text="Pesquisar", command=self.chamaPesquisar)
        self.btn_pesquisar_pedi.place(x=1100, y=20)

        self.btn_show = Button(self.telapedi, text="Mostrar todos", command=lambda:[self.view_tree(), self.clear_entry()])
        self.btn_show.place(x=1000,y=60)
