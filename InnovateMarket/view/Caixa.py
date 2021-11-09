from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from time import sleep
from controller.Controller import *
from model.Config import *
from random import randint
from view.CaixaProdutos import *

class Caixa():
    def __init__(self):
        self.compraID = self.gerarVendaId()
        self.telacaixa = Toplevel()
        self.valor = 0
        self.troco = 0
        self.telacaixa.attributes("-fullscreen", True)
        self.geometry()
        self.imagecaixapath = imagespath /  "Logo.png"
        self.imgcaixa = PhotoImage(file=self.imagecaixapath)
        self.options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.itemVariable = StringVar()
        self.itemVariable.set(self.options[0])

        
        self.elementos()
        self.telacaixa.bind('<F1>', lambda event: self.adicionarProduto())
        self.telacaixa.bind('<F2>', lambda event: self.excluirProdutoCompra())
        self.telacaixa.bind('<F5>', lambda event: self.pesquisarProduto())
        self.telacaixa.bind('<F6>', lambda event: self.finalizarVenda())
        self.telacaixa.bind('<F7>', lambda event: self.abortarCompra())
        

    def geometry(self):
        self.telacaixa.title("Caixa")
        self.telacaixa.geometry("1360x768")
        self.telacaixa.configure(bg="Lightgrey")
        self.telacaixa.resizable(False, False)
        self.__iconImagemPath = imagespath / "logo.ico"
        self.telacaixa.iconbitmap(self.__iconImagemPath)

    def pesquisarProduto(self):
        CaixaProdutos()

    def abortarCompra(self):
        self.result = messagebox.askquestion(
            'AVISO', 'Tem certeza que deseja abortar a compra?', icon="warning", parent=self.telacaixa)
        if self.result == "yes":
            caixaControler().caixaAbortar(self.compraID)
            self.telacaixa.destroy()
        return
    
    def treeViewSelectionItem(self):
        self.currItem = self.tree_caixa.focus()
        self.values = self.tree_caixa.item(self.currItem)['values']
        print(self.values)
        self.values = self.values[1]
        return self.values

    def atualizarDadosLabel(self):
        self.lbl_valorPagar.config(text=self.valor)
        self.lbl_troco.config(text=self.troco)
        

    def adicionarProduto(self):
        self.dicti = {}
        self.dicti["Qtd"] = "Vazio!"
        
        self.nomeProduto = caixaControler().CaixaPesquisarProdutos(self.ent_cod_barras.get())
        if self.nomeProduto == "Nenhum produto!":
            messagebox.showwarning(
                title="ERROR!", message="Selecione um produto válido! Use F5 para pesquisar!", parent=self.telacaixa) 
        else:
            self.dicti["nomeProduto"] = self.nomeProduto[0][2]
            self.dicti["valorProduto"] = self.nomeProduto[0][1]
        self.quantidade = self.ent_qtde.get()
        resultado = caixaControler().validarQuantidade(self.quantidade)
        if resultado:
            self.dicti["Qtd"] = self.quantidade
        else:
            messagebox.showwarning(
            title="ERROR!", message="Coloque uma quantidade válida!", parent=self.telacaixa)
        
        resultado = caixaControler().validarValues(self.dicti)
        
        if resultado:
            self.dicti["CodigoProduto"] = self.ent_cod_barras.get()
            self.dicti["CodigoCompra"] = self.compraID
            self.valor += (int(self.nomeProduto[0][1]) * int(self.quantidade))
            caixaControler().adicionarProdutoCaixa(self.dicti)
            self.mostrarDados()
            self.atualizarDadosLabel()

    def excluirProdutoCompra(self):
        self.currItem = self.tree_caixa.focus()
        if not self.currItem :
            messagebox.showwarning(title="ERROR!", message="Selecione um produto para deletar!", parent=self.telacaixa)
        else:
            self.values = self.tree_caixa.item(self.currItem)['values']
            self.values.append(self.compraID)
            self.values = caixaControler().caixaValues(self.values)
            self.tree_caixa.delete(self.currItem)
            self.valor -= (int(self.values.Valores) * int(self.values.Qtd))
            caixaControler().deletarProduto(self.values.CodigoProduto)
            self.atualizarDadosLabel()
            self.mostrarDados()

    def finalizarVenda(self):
        if self.ent_totalRecebido.get() != '':
            self.troco = int(self.ent_totalRecebido.get()) - int(self.valor)
            self.atualizarDadosLabel()
            self.result = messagebox.askquestion(
            'AVISO', 'Tem certeza que deseja finalizar a compra?', icon="warning", parent=self.telacaixa)
            if self.result == "yes":
                caixaControler().caixaFinalizarCompra(self.compraID)
                self.mostrarDados()
                messagebox.showinfo(title="Finalizado!", message="Compra finalizada!", parent=self.telacaixa)
                sleep(3)
                self.telacaixa.destroy()
            return
        else:
            messagebox.showwarning(
                title="ERROR!", message="Coloque o valor recebido!", parent=self.telacaixa) 
    
    def gerarVendaId(self):
        self.compraID = randint(0, 9999999)
        self.compraID = str(self.compraID)
        return self.compraID
    
    # Função para aparecer os dados na Treeview
    def mostrarDados(self):
        resultado = caixaControler().mostarCaixa()
        
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
        self.__bg = PhotoImage(file=self.pathBg)
        self.lblimgbg = Label(self.telacaixa, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)


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
        self.tree_caixa = ttk.Treeview(self.tree_caixa_frame, column=(
            "1", "2", "3", "4"), show='headings', height=24, yscrollcommand=self.scroll.set)

        self.tree_caixa.pack()

        self.scroll.config(command=self.tree_caixa.yview)

        # Colunas da Treeview Caixa
        self.tree_caixa.heading('#1', text="Nome produto", anchor=CENTER)
        self.tree_caixa.heading('#2', text="Preço", anchor=CENTER)
        self.tree_caixa.heading('#3', text="Quantidade", anchor=CENTER)
        self.tree_caixa.heading('#4', text="Codigo produto", anchor=CENTER)
        self.mostrarDados()      

        ### ENTRYS ###
        self.ent_cod_barras = Entry(self.telacaixa, bg="lightgrey", font="arial 18")
        self.ent_cod_barras.place(x=50, y=80)

        self.ent_qtde = Entry(self.telacaixa, bg="lightgrey", font="arial 18")
        self.ent_qtde.place(x=50, y=195)

        self.ent_totalRecebido = Entry(self.telacaixa, bg="lightgrey", font="arial 18")
        self.ent_totalRecebido.place(x=50, y=320)

        ### LABELS ###
        self.lbl_troco = Label(self.telacaixa, text="Troco", width=16, font="arial 20", anchor="w", bg="#305c81", fg="black")
        self.lbl_troco.place(x=45, y=443)

        self.lbl_valorPagar = Label(self.telacaixa, text="Valor à pagar", width=16, font="arial 20", anchor="w", bg="#305c81", fg="black")
        self.lbl_valorPagar.place(x=920, y=585)