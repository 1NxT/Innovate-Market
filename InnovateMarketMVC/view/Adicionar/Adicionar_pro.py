from tkinter import *
import tkinter.ttk as ttk
from model.Config import *
from controller.Controller import produtosControler


class Adicionar_pro(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.adicionar_pro = Toplevel()
        self.adicionar_pro.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def view_tree(self):
        self.resultado = produtosControler().mostarProdutos()

        if self.resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())
            for i in self.resultado:

                self.tree_pro.insert("", "end", values=i)
        else:
            print("Error!")

    def geometry(self):
        self.adicionar_pro.title("Adicionar produtos")
        self.adicionar_pro.geometry("1360x768")
        self.adicionar_pro.resizable(False, False)
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.adicionar_pro.iconbitmap(self.__iconImagemPath)

    def voltar_inicial_add_pro(self):
        self.adicionar_pro.destroy()
        return

    # def adicionar_produto(self):
    #     self.dicti = {}
    #     self.dicti["cod"] = self.ent_cod.get()
    #     self.dicti["preco"] = self.ent_preco.get()
    #     self.dicti["nome"] = self.ent_nome.get()
    #     #self.dicti["fornecedor"] = self.ent_fornecedor.get()
    #     produtosControler().inserirProduto(self.dicti)
        
        self.view_tree()

    def elementos(self):
        
        self.pathBg = imagespath / "editProdutos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.adicionar_pro, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_telainicial = imagespath / "Salvar.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_add_pro = Button(self.adicionar_pro, image=self.btn_voltartelainicial, command=self.voltar_inicial_add_pro, relief="flat", borderwidth=0, width=225, height=50, bg="Gainsboro")
        self.btn_telainicial_add_pro.place(x=980, y=660)


        self.ent_cod = Entry(self.adicionar_pro, width=25, font="Arial 18")
        self.ent_cod.place(x=886, y=160)

        self.ent_preco = Entry(self.adicionar_pro, width=25, font="Arial 18")
        self.ent_preco.place(x=886, y=280)


        self.ent_nome = Entry(self.adicionar_pro, width=25, font="Arial 18")
        self.ent_nome.place(x=886, y=400)


        # self.ent_fornecedor = Entry(self.adicionar_pro, width=25, font="Arial 18")
        # self.ent_fornecedor.place(x=886, y=520)

        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_pro_frame = Frame(self.adicionar_pro, padx=0, pady=0, bg="lightgrey")
        self.tree_pro_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pro_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pro = ttk.Treeview(self.tree_pro_frame, column=(
            "Código de barras", "Preço", "Nome", "Fornecedor"), show='headings', height=35, yscrollcommand=self.scroll.set)

        self.tree_pro.pack()

        self.scroll.config(command=self.tree_pro.yview)

        self.tree_pro.heading('#1', text="Código de barras", anchor=CENTER)
        self.tree_pro.heading('#2', text="Preço", anchor=CENTER)
        self.tree_pro.heading('#3', text="Nome", anchor=CENTER)
        #self.tree_pro.heading('#4', text="Fornecedor", anchor=CENTER)

        self.view_tree()
