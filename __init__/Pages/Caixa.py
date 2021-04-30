from tkinter import *
import tkinter.ttk as ttk


class Caixa(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)
        self.telacaixa = Toplevel()
        self.geometry()

        self.imgcaixa = PhotoImage(file="Innovate-Market-main\__init__\Imagens\Logo_Caixa.png")
        self.options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.itemVariable = StringVar()
        self.itemVariable.set(self.options[0])

        
        self.elementos()
        

    def geometry(self):
        self.telacaixa.title("Caixa")
        self.telacaixa.geometry("1360x760")
        self.telacaixa.configure(bg="DodgerBlue")
        self.telacaixa.resizable(False, False)
        self.telacaixa.iconbitmap('Innovate-Market-main\__init__\Imagens\logo.ico')

    def voltar_inicial_caixa(self):
        self.telacaixa.destroy()
        return

    def elementos(self):
        btn_telainicial_caixa = Button(self.telacaixa, text="Voltar Para Tela Inicial", command=self.voltar_inicial_caixa,bg="firebrick")
        btn_telainicial_caixa.place(x=1200, y=700)

        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview Caixa
        tree_caixa_frame = Frame(self.telacaixa, padx=1, pady=10, bg="DodgerBlue")
        tree_caixa_frame.place(x=0, y=0)

        # ScrollBar Caixa
        scroll = ttk.Scrollbar(tree_caixa_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)
        
        # Treeview Caixa
        tree_caixa = ttk.Treeview(tree_caixa_frame, column=("1","2","3","4"), show='headings', height=24, yscrollcommand=scroll.set)
        
        tree_caixa.pack()

        scroll.config(command=tree_caixa.yview)
        
        # Colunas da Treeview Caixa
        tree_caixa.heading('#1', text="N° Item", anchor=CENTER)
        tree_caixa.heading('#2', text="Descrição", anchor=CENTER)
        tree_caixa.heading('#3', text="Preço", anchor=CENTER)
        tree_caixa.heading('#4', text="ID do Produto", anchor=CENTER)

        # Imagem da Logo
        lbl_imagem_caixa = Label(self.telacaixa, image=self.imgcaixa, width=280, height=240, bg="DodgerBlue")
        lbl_imagem_caixa.place(x=1100,y=0)

        # Menu de opções
        menu_quantidade = OptionMenu(self.telacaixa, self.itemVariable, *self.options)
        menu_quantidade.place(x=840,y=300)

        # Botões da tela Caixa
        btn_editar = Button(self.telacaixa, text="Editar", font="arial 18")
        btn_editar.place(x=1150,y=400)

        btn_cancelar = Button(self.telacaixa, text="Cancelar", font="arial 18")
        btn_cancelar.place(x=850,y=400)

        btn_final = Button(self.telacaixa, text="Finalizar", font="arial 18")
        btn_final.place(x=1150,y=400)

        btn_excluir = Button(self.telacaixa, text="Excluir", font="arial 18")
        btn_excluir.place(x=1000,y=400)

        ent_cod_barras = Entry(self.telacaixa, font="arial 18")
        ent_cod_barras.place(x=830, y=60)

        
        lbl_subtotal = Label(self.telacaixa,text="SUB TOTAL:", font="arial 24",fg="black",bg="DodgerBlue")
        lbl_subtotal.place(x=0,y=527)

        lbl_total_recebido = Label(self.telacaixa, text="Total Recebido:", font="arial 24",bg="DodgerBlue")
        lbl_total_recebido.place(x=0,y=640)

        lbl_total_unitario = Label(self.telacaixa, text="Valor Unitario :", font="arial 24", bg="DodgerBlue")
        lbl_total_unitario.place(x=830,y=100)


        lbl_troco = Label(self.telacaixa, text="Troco:", font="arial 24",bg="DodgerBlue")
        lbl_troco.place(x=470,y=640)

        lbl_codigo = Label(self.telacaixa, text="ID do Produto:", font="arial 24",bg="DodgerBlue")
        lbl_codigo.place(x=830,y=10)

        lbl_total_item = Label(self.telacaixa, text="Total do item:", font="arial 24",bg="DodgerBlue")
        lbl_total_item.place(x=830,y=200)
        
