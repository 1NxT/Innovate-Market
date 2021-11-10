from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from model.Config import *
from controller.Controller import fornecedorControler

class Adicionar_forne():
    def __init__(self):
        self.adicionar_forne = Toplevel()
        self.adicionar_forne.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
            self.adicionar_forne.title("Adicionar Fornecedor")
            self.adicionar_forne.geometry("1360x768")
            self.adicionar_forne.resizable(False, False)
            self.__iconImagemPath = imagespath / "logo.ico"
            self.adicionar_forne.iconbitmap(self.__iconImagemPath)

    def mostrarDados(self):
        self.resultado = fornecedorControler().mostarFornecedor()

        if self.resultado != None:
            self.tree_forne.delete(*self.tree_forne.get_children())
            for i in self.resultado:
                self.tree_forne.insert("", "end", values=i)
        else:
            print("Error!")

    def adicionar_fornecedor(self):
        try:
            self.dicti = {}
            self.dicti["nome"] = self.ent_nome.get() if self.ent_nome.get() != '' else "Vazio!"
            self.dicti["CNPJ"] = self.ent_cnpj.get() if self.ent_cnpj.get() != '' else "Vazio!" 
            self.dicti["telefone"] = self.ent_telefone.get() if self.ent_telefone.get() != '' else "Vazio!"
            self.dicti["email"] = self.ent_email.get() if self.ent_email.get() != '' else "Vazio!"
            resultado =  fornecedorControler().inserirFornecedor(self.dicti)
            
            if resultado:
                self.mostrarDados()
                messagebox.showinfo(title="AVISO!", message="Fornecedor adicionado com sucesso!", parent=self.adicionar_forne)
                self.voltar_inicial_add_forne()
            else:
                messagebox.showwarning(title="AVISO!", message="Coloque valores válidos!", parent=self.adicionar_forne)
        except Exception as e:
            e = str(e)
            if e == "datatype mismatch":
                messagebox.showwarning(title="AVISO!", message="Coloque valores válidos!", parent=self.adicionar_forne)
            elif e == "UNIQUE constraint failed: fornecedores.CNPJ":
                messagebox.showwarning(title="AVISO!", message="Itens repetidos!", parent=self.adicionar_forne)
            else:
                print(e)
                messagebox.showwarning(title="AVISO!", message="Algum erro aconteceu! Espere um pouco e tente novamente!", parent=self.adicionar_forne)

    def voltar_inicial_add_forne(self):
        self.adicionar_forne.destroy()
        return

    def elementos(self):
        
        self.pathBg = imagespath / "editFornecedores_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.adicionar_forne, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_forne_frame = Frame(self.adicionar_forne, padx=1, pady=1, bg="lightgrey")
        self.tree_forne_frame.place(x=10, y=5)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_forne_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        self.tree_forne = ttk.Treeview(self.tree_forne_frame, column=("1","2","3","4"), show='headings', height=36, yscrollcommand=self.scroll.set)
        self.tree_forne.pack()

        self.scroll.config(command=self.tree_forne.yview)

        self.tree_forne.heading('#1', text="CNPJ", anchor=CENTER)
        self.tree_forne.heading('#2', text="Nome", anchor=CENTER)
        self.tree_forne.heading('#3', text="Telefone", anchor=CENTER)
        self.tree_forne.heading('#4', text="Email", anchor=CENTER)
        self.mostrarDados()

        self.ent_nome = Entry(self.adicionar_forne, bg="lightgrey", width=25, font="Arial 18")
        self.ent_nome.place(x=865, y=200)

        self.ent_cnpj = Entry(self.adicionar_forne, bg="lightgrey", width=25, font="Arial 18")
        self.ent_cnpj.place(x=865, y=320)

        self.ent_telefone = Entry(self.adicionar_forne, bg="lightgrey", width=25, font="Arial 18")
        self.ent_telefone.place(x=865, y=445)

        self.ent_email = Entry(self.adicionar_forne, bg="lightgrey", width=25, font="Arial 18")
        self.ent_email.place(x=865, y=560)

        self.btn_salvarPath = imagespath / "adicionar.png"
        self.btn_salvar = PhotoImage(file =self.btn_salvarPath)
        self.btn_salvar_add_forne = Button(self.adicionar_forne, image=self.btn_salvar, command=self.adicionar_fornecedor, relief="flat", borderwidth=0, width=225, height=50, bg="Gainsboro")
        self.btn_salvar_add_forne.place(x=980, y=668)

        self.btn_telainicial = imagespath / "fechar_X.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_add_forne = Button(self.adicionar_forne, image=self.btn_voltartelainicial, command=self.voltar_inicial_add_forne, relief="flat", borderwidth=0, width=30, height=30, bg="Gainsboro")
        self.btn_telainicial_add_forne.place(x=1330, y=5)