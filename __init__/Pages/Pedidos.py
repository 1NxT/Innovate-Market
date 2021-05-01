from tkinter import *

class Pedidos:
    def __init__(self):
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
            telapedi.destroy()
            return

    def elementos(self):

        btn_telainicial_pedi = Button(self.telapedi, text="Voltar Para Tela Inicial", command=self.voltar_inicial_pedi,bg="red")
        btn_telainicial_pedi.place(x=1000, y=600)
        
        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_pedi_frame = Frame(self.telapedi, padx=1, pady=10, bg="DodgerBlue")
        tree_pedi_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_pedi_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_pedi = ttk.Treeview(tree_pedi_frame, column=("1","2","3","4"), show='headings', height=35, yscrollcommand=scroll.set)
        tree_pedi.pack()

        scroll.config(command=tree_pedi.yview)

        tree_pedi.heading('#1', text="Nome do produto", anchor=CENTER)
        tree_pedi.heading('#2', text="Cliente", anchor=CENTER)
        tree_pedi.heading('#3', text="Valor Total", anchor=CENTER)
        tree_pedi.heading('#4', text="Numero do Pedido", anchor=CENTER)
     

        ent_pesquisar = Entry(self.telapedi)
        ent_pesquisar.place(x=1000, y=20)

        btn_pesquisar_pedi = Button(self.telapedi, text="Pesquisar")
        btn_pesquisar_pedi.place(x=1100, y=20)

        btn_show = Button(self.telapedi, text="Mostrar todos")
        btn_show.place(x=1000,y=60)


        


