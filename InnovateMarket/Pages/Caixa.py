from tkinter import *
import tkinter.ttk as ttk
from Classes.Pesquisar import *
from Classes.Mostrar import *
from Pages.common.Config import *


class Caixa(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.telacaixa = Toplevel()
        self.geometry()
        self.imagecaixapath = imagespath /  "Logo.png"
        self.imgcaixa = PhotoImage(file=self.imagecaixapath)
        self.options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.itemVariable = StringVar()
        self.itemVariable.set(self.options[0])

        
        self.elementos()
        

    def geometry(self):
        self.telacaixa.title("Caixa")
        self.telacaixa.geometry("1360x760")
        self.telacaixa.configure(bg="DodgerBlue")
        self.telacaixa.resizable(False, False)
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.telacaixa.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_caixa(self):
        self.telacaixa.destroy()
        return
    
    # Função para aparecer os dados na Treeview
    def view_tree(self):
        resultado = Mostrar().mostrar(self, "caixa", "ID")
        
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


        self.pathBg = imagespath / "caixa_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.telacaixa, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        #Button de voltar a tela inicial
        self.btn_telainicial_caixa = Button(self.telacaixa, text="Voltar Para Tela Inicial", command=self.voltar_inicial_caixa,bg="firebrick")
        self.btn_telainicial_caixa.place(x=1200, y=700)

        #Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Caixa
        self.tree_caixa_frame = Frame(self.telacaixa, padx=1, pady=3, bg="lightgrey")
        self.tree_caixa_frame.place(x=530, y=0)

        # ScrollBar Caixa
        self.scroll = ttk.Scrollbar(self.tree_caixa_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)
        
        # Treeview Caixa
        self.tree_caixa = ttk.Treeview(self.tree_caixa_frame, column=("1","2","3","4"), show='headings', height=24, yscrollcommand=self.scroll.set)
        
        self.tree_caixa.pack()

        self.scroll.config(command=self.tree_caixa.yview)
        
        # Colunas da Treeview Caixa
        self.tree_caixa.heading('#1', text="N. item", anchor=CENTER)
        self.tree_caixa.heading('#2', text="Codigo", anchor=CENTER)
        self.tree_caixa.heading('#3', text="Descricao", anchor=CENTER)
        self.tree_caixa.heading('#4', text="Qtde", anchor=CENTER)
        self.view_tree()
        # Menu de opções
        #self.menu_quantidade = OptionMenu(self.telacaixa, self.itemVariable, *self.options)
        #self.menu_quantidade.place(x=840,y=300)

        # Botões da tela Caixa
        

        self.ent_cod_barras = Entry(self.telacaixa, font="arial 18")
        self.ent_cod_barras.place(x=50, y=100)

        
