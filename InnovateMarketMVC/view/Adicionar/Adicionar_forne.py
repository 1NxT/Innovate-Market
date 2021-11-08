from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from model.Config import *
from controller.Controller import fornecedorControler

class Adicionar_forne(Frame):
    def __init__(self):
        Frame.__init__(self, mater=None)
        self.adicionar_forne = Toplevel()
        self.adicionar_forne.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
            self.adicionar_forne.title("Adicionar Fornecedor")
            self.adicionar_forne.geometry("1360x768")
            self.adicionar_forne.resizable(False, False)
            # self.__iconImagemPath = imagespath / "logo.ico"
            # self.adicionar_forne.iconbitmap(self.__iconImagemPath)

    def mostrarDados(self):
        self.resultado = fornecedorControler().mostarFornecedor()

        if self.resultado != None:
            self.tree_forne.delete(*self.tree_forne.get_children())
            for i in self.resultado:
                self.tree_forne.insert("", "end", values=i)
        else:
            print("Error!")

    def adicionar_fornecedor(self):
        self.dicti = {}
        self.dicti["nome"] = self.ent_nome.get()
        self.dicti["CNPJ"] = self.ent_cnpj.get()
        self.dicti["telefone"] = self.ent_telefone.get()
        self.dicti["email"] = self.ent_email.get()
        fornecedorControler().inserirFornecedor(self.dicti)
        
        self.mostrarDados()
        self.voltar_inicial_add_pro()

    def voltar_inicial_add_pro(self):
        messagebox.showinfo(title="AVISO!", message="Item adicionado com sucesso!", parent=self.adicionar_pro)
        self.adicionar_forne.destroy()
        return

    def elementos(self):
        
        self.pathBg = imagespath / "editFornecedores_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.adicionar_forne, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.btn_salvarPath = imagespath / "Salvar.png"
        self.btn_salvar = PhotoImage(file =self.btn_salvarPath)
        self.btn_salvar_add_forne = Button(self.adicionar_forne, image=self.btn_salvar, command=self.adicionar_fornecedor, relief="flat", borderwidth=0, width=225, height=50, bg="Gainsboro")
        self.btn_salvar_add_forne.place(x=980, y=660)


        self.ent_nome = Entry(self.adicionar_forne, width=25, font="Arial 18")
        self.ent_nome.place(x=886, y=160)

        self.ent_cnpj = Entry(self.adicionar_forne, width=25, font="Arial 18")
        self.ent_cnpj.place(x=886, y=280)


        self.ent_telefone = Entry(self.adicionar_forne, width=25, font="Arial 18")
        self.ent_telefone.place(x=886, y=400)

        self.ent_email = Entry(self.adicionar_forne, width=25, font="Arial 18")
        self.ent_email.place(x=886, y=520)