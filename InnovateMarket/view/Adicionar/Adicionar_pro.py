from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from model.Config import *
from controller.Controller import produtosControler


class Adicionar_pro():
    def __init__(self):
        self.adicionar_pro = Toplevel()
        self.adicionar_pro.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.adicionar_pro.title("Adicionar produtos")
        self.adicionar_pro.geometry("1360x768")
        self.adicionar_pro.resizable(False, False)
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.adicionar_pro.iconbitmap(self.__iconImagemPath)

    def mostrarDados(self):
        self.resultado = produtosControler().mostarProdutos()

        if self.resultado != None:
            self.tree_pro.delete(*self.tree_pro.get_children())
            for i in self.resultado:

                self.tree_pro.insert("", "end", values=i)
        else:
            print("Error!")

    def voltar_inicial_add_pro(self):
        self.adicionar_pro.destroy()
        return

    def adicionar_produto(self):
        try:
            self.dicti = {}
            self.dicti["cod"] = self.ent_cod.get() if self.ent_cod.get() != '' else "Vazio!"
            self.dicti["preco"] = self.ent_preco.get() if self.ent_preco.get() != '' else "Vazio!"
            self.dicti["nome"] = self.ent_nome.get() if self.ent_nome.get() != '' else "Vazio!"
            resultado = produtosControler().inserirProduto(self.dicti)
            if resultado:
                self.mostrarDados()
                messagebox.showinfo(title="AVISO!", message="Produto adicionado com sucesso!", parent=self.adicionar_pro)
                self.voltar_inicial_add_pro
            else:
                messagebox.showwarning(title="AVISO!", message="Coloque valores válidos!", parent=self.adicionar_pro)
        except Exception as e:
            e = str(e)
            if e == "datatype mismatch":
                messagebox.showwarning(title="AVISO!", message="Coloque valores válidos!", parent=self.adicionar_pro)
            elif e == "UNIQUE constraint failed: produtos.ID":
                messagebox.showwarning(title="AVISO!", message="Itens repetidos!", parent=self.adicionar_pro)
            else:
                print(e)
                messagebox.showwarning(title="AVISO!", message="Algum erro aconteceu! Espere um pouco e tente novamente!", parent=self.adicionar_pro)

    def elementos(self):
        self.pathBg = imagespath / "editProdutos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.adicionar_pro, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.ent_cod = Entry(self.adicionar_pro, bg="lightgrey", width=25, font="Arial 18")
        self.ent_cod.place(x=710, y=230)

        self.ent_preco = Entry(self.adicionar_pro, bg="lightgrey", width=25, font="Arial 18")
        self.ent_preco.place(x=710, y=350)

        self.ent_nome = Entry(self.adicionar_pro, bg="lightgrey", width=25, font="Arial 18")
        self.ent_nome.place(x=710, y=470)

        self.btn_telainicial = imagespath / "adicionar.png"
        self.btn_salvar = PhotoImage(file =self.btn_telainicial)
        self.btn_salvar_add_pro = Button(self.adicionar_pro, image=self.btn_salvar, command=self.adicionar_produto, relief="flat", borderwidth=0, width=225, height=55, bg="Gainsboro")
        self.btn_salvar_add_pro.place(x=900, y=660)

        self.btn_telainicial = imagespath / "fechar_X.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_add_pro = Button(self.adicionar_pro, image=self.btn_voltartelainicial, command=self.voltar_inicial_add_pro, relief="flat", borderwidth=0, width=30, height=30, bg="Gainsboro")
        self.btn_telainicial_add_pro.place(x=1325, y=5)

        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview Produtos
        self.tree_pro_frame = Frame(self.adicionar_pro, padx=2, pady=2, bg="lightgrey")
        self.tree_pro_frame.place(x=10, y=5)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pro_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_pro = ttk.Treeview(self.tree_pro_frame, column=("Código de barras", "Preço", "Nome"), show='headings', height=35, yscrollcommand=self.scroll.set)

        self.tree_pro.pack()

        self.scroll.config(command=self.tree_pro.yview)

        self.tree_pro.heading('#1', text="Código de barras", anchor=CENTER)
        self.tree_pro.heading('#2', text="Preço", anchor=CENTER)
        self.tree_pro.heading('#3', text="Nome", anchor=CENTER)
        
        self.mostrarDados()
