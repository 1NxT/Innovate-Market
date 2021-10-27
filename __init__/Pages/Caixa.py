from tkinter import *
import tkinter.ttk as ttk
from Classes.Config import *
from Classes.Pesquisar import *
from Classes.Mostrar import *


class Caixa(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.telacaixa = Toplevel()
        self.geometry()

        self.imgcaixa = PhotoImage(file="__init__\Imagens\Logo_Caixa.png")
        self.options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.itemVariable = StringVar()
        self.itemVariable.set(self.options[0])

        
        self.elementos()
        

    def geometry(self):
        self.telacaixa.title("Caixa")
        self.telacaixa.geometry("1360x760")
        self.telacaixa.configure(bg="DodgerBlue")
        self.telacaixa.resizable(False, False)
        self.__iconImagemPath = Config().images() / "logo.ico"
        self.telacaixa.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_caixa(self):
        self.telacaixa.destroy()
        return
    
    # Função para aparecer os dados na Treeview
    def view_tree(self):
        resultado = Mostrar().mostrar(self, "caixa", "id_produto")
        
        if resultado != None:
            self.tree_caixa.delete(*self.tree_caixa.get_children())
            
            for i in resultado:
                self.tree_caixa.insert("","end",values=i)
        else:
            print("Error!")
    
    # Função para procurar por dados na Treeview        
    def chamaPesquisar(self):
        resultado = Pesquisar.pesquisar(self.ent_pesquisar.get(), "caixa")

        if resultado != None:
            self.tree_caixa.delete(*self.tree_caixa.get_children())
            
            for i in resultado:
                self.tree_caixa.insert("","end",values=i)
        else:
            print("Error: Nenhum valor saiu da Classe")
        
    
    # LABELS, ENTRYS, BUTTONS e ETC da tela:
    def elementos(self):
        #Button de voltar a tela inicial
        self.btn_telainicial_caixa = Button(self.telacaixa, text="Voltar Para Tela Inicial", command=self.voltar_inicial_caixa,bg="firebrick")
        self.btn_telainicial_caixa.place(x=1200, y=700)

        #Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Caixa
        self.tree_caixa_frame = Frame(self.telacaixa, padx=1, pady=3, bg="DodgerBlue")
        self.tree_caixa_frame.place(x=0, y=0)

        # ScrollBar Caixa
        self.scroll = ttk.Scrollbar(self.tree_caixa_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)
        
        # Treeview Caixa
        self.tree_caixa = ttk.Treeview(self.tree_caixa_frame, column=("1","2","3","4"), show='headings', height=24, yscrollcommand=self.scroll.set)
        
        self.tree_caixa.pack()

        self.scroll.config(command=self.tree_caixa.yview)
        
        # Colunas da Treeview Caixa
        self.tree_caixa.heading('#1', text="Nome do Item", anchor=CENTER)
        self.tree_caixa.heading('#2', text="Preço", anchor=CENTER)
        self.tree_caixa.heading('#3', text="Fornecedor", anchor=CENTER)
        self.tree_caixa.heading('#4', text="ID do Produto", anchor=CENTER)
        self.view_tree()

        # Imagem da Logo
        self.lbl_imagem_caixa = Label(self.telacaixa, image=self.imgcaixa, width=280, height=240, bg="DodgerBlue")
        self.lbl_imagem_caixa.place(x=1100,y=0)

        # Menu de opções
        self.menu_quantidade = OptionMenu(self.telacaixa, self.itemVariable, *self.options)
        self.menu_quantidade.place(x=840,y=300)

        # Botões da tela Caixa
        self.btn_editar = Button(self.telacaixa, text="Editar", font="arial 18")
        self.btn_editar.place(x=1150,y=400)

        self.btn_cancelar = Button(self.telacaixa, text="Cancelar", font="arial 18")
        self.btn_cancelar.place(x=850,y=400)

        self.btn_final = Button(self.telacaixa, text="Finalizar", font="arial 18")
        self.btn_final.place(x=1150,y=400)

        self.btn_excluir = Button(self.telacaixa, text="Excluir", font="arial 18")
        self.btn_excluir.place(x=1000,y=400)

        self.ent_cod_barras = Entry(self.telacaixa, font="arial 18")
        self.ent_cod_barras.place(x=830, y=60)

        
        self.lbl_subtotal = Label(self.telacaixa,text="SUB TOTAL:", font="arial 24",fg="black",bg="DodgerBlue")
        self.lbl_subtotal.place(x=0,y=527)

        self.lbl_total_recebido = Label(self.telacaixa, text="Total Recebido:", font="arial 24",bg="DodgerBlue")
        self.lbl_total_recebido.place(x=0,y=640)

        self.lbl_total_unitario = Label(self.telacaixa, text="Valor Unitario :", font="arial 24", bg="DodgerBlue")
        self.lbl_total_unitario.place(x=830,y=100)


        self.lbl_troco = Label(self.telacaixa, text="Troco:", font="arial 24",bg="DodgerBlue")
        self.lbl_troco.place(x=470,y=640)

        self.lbl_codigo = Label(self.telacaixa, text="ID do Produto:", font="arial 24",bg="DodgerBlue")
        self.lbl_codigo.place(x=830,y=10)

        self.lbl_total_item = Label(self.telacaixa, text="Total do item:", font="arial 24",bg="DodgerBlue")
        self.lbl_total_item.place(x=830,y=200)
        
