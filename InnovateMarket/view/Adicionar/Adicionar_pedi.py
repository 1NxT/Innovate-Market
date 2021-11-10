from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from model.Config import *
from controller.Controller import pedidosControler

class Adicionar_pedi():
    def __init__(self):
        self.adicionar_pedi = Toplevel()
        self.adicionar_pedi.attributes("-fullscreen", True)
        self.geometry()
        self.elementos()

    def geometry(self):
        self.adicionar_pedi.title("Adicionar pedidos")
        self.adicionar_pedi.geometry("1360x768")
        self.adicionar_pedi.resizable(False, False)
        self.__iconImagePath = imagespath / "logo.ico"
        self.adicionar_pedi.iconbitmap(self.__iconImagePath)

    def mostrarDados(self):
        self.resultado = pedidosControler().mostarPedido()

        if self.resultado != None:
            self.tree_pedi.delete(*self.tree_pedi.get_children())
            for i in self.resultado:
                self.tree_pedi.insert("", "end", values=i)
        else:
            print("Error!")

    def adicionar_pedido(self):
        try:
            self.dicti = {}
            self.dicti["ID"] = self.ent_numPedi.get() if self.ent_numPedi.get() != '' else "Vazio!"
            self.dicti["produtos"] = self.ent_nomeProduto.get() if self.ent_nomeProduto.get() != '' else "Vazio!" 
            self.dicti["valores"] = self.ent_valorTotal.get() if self.ent_valorTotal.get() != '' else "Vazio!"
            self.dicti["data"] = self.ent_data.get() if self.ent_data.get() != '' else "Vazio!"

            resultado =  pedidosControler().inserirPedidos(self.dicti)
            
            if resultado:
                self.mostrarDados()
                messagebox.showinfo(title="AVISO!", message="Pedido adicionado com sucesso!", parent=self.adicionar_pedi)
                self.voltar_inicial_add_pedi()
            else:
                messagebox.showwarning(title="AVISO!", message="Coloque valores válidos!", parent=self.adicionar_pedi)
        except Exception as e:
            e = str(e)
            if e == "datatype mismatch":
                messagebox.showwarning(title="AVISO!", message="Coloque valores válidos!", parent=self.adicionar_pedi)
            elif e == "UNIQUE constraint failed: pedidos.ID":
                messagebox.showwarning(title="AVISO!", message="Itens repetidos!", parent=self.adicionar_pedi)
            else:
                print(e)
                messagebox.showwarning(title="AVISO!", message="Algum erro aconteceu! Espere um pouco e tente novamente!", parent=self.adicionar_pedi)

    def voltar_inicial_add_pedi(self):
        self.adicionar_pedi.destroy()
        return
        
    def elementos(self):
        self.pathBg = imagespath / "addPedidos_bg.png"
        self.__bg = PhotoImage(file =self.pathBg)
        self.lblimgbg = Label(self.adicionar_pedi, image=self.__bg)
        self.lblimgbg.place(x=0, y=0)

        self.ent_nomeProduto = Entry(self.adicionar_pedi, bg="lightgrey", width=25, font="Arial 18")
        self.ent_nomeProduto.place(x=865, y=315)

        self.ent_data = Entry(self.adicionar_pedi, bg="lightgrey", width=25, font="Arial 18")
        self.ent_data.place(x=865, y=435)


        self.ent_valorTotal = Entry(self.adicionar_pedi, bg="lightgrey", width=25, font="Arial 18")
        self.ent_valorTotal.place(x=865, y=553)


        self.ent_numPedi = Entry(self.adicionar_pedi, bg="lightgrey", width=25, font="Arial 18")
        self.ent_numPedi.place(x=865, y=200)

        self.img_adicionar = imagespath / "adicionar.png"
        self.btn_adicionar = PhotoImage(file =self.img_adicionar)
        self.btn_adicionar_pedido = Button(self.adicionar_pedi, command=self.adicionar_pedido, image=self.btn_adicionar, relief="flat", borderwidth=0, bg="lightgrey")
        self.btn_adicionar_pedido.place(x=980, y=668)

        self.btn_telainicial = imagespath / "fechar_X.png"
        self.btn_voltartelainicial = PhotoImage(file =self.btn_telainicial)
        self.btn_telainicial_add_pedi = Button(self.adicionar_pedi, image=self.btn_voltartelainicial, command=self.voltar_inicial_add_pedi, relief="flat", borderwidth=0, width=30, height=30, bg="Gainsboro")
        self.btn_telainicial_add_pedi.place(x=1330, y=5)

        # Estilo da Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Frame da Treeview
        self.tree_pedi_frame = Frame(self.adicionar_pedi, padx=0, pady=1, bg="lightgrey")
        self.tree_pedi_frame.place(x=0, y=0)

        # ScrollBar
        self.scroll = ttk.Scrollbar(self.tree_pedi_frame)
        self.scroll.pack(side=RIGHT, fill=Y, padx=0)

        # Treeview
        self.tree_pedi = ttk.Treeview(self.tree_pedi_frame, column=("1","2","3","4"), show='headings', height=35, yscrollcommand=self.scroll.set)
        self.tree_pedi.pack()

        self.scroll.config(command=self.tree_pedi.yview)

        self.tree_pedi.heading('#1', text="Numero do Pedido", anchor=CENTER)
        self.tree_pedi.heading('#2', text="Nome do produto", anchor=CENTER)
        self.tree_pedi.heading('#3', text="Data", anchor=CENTER)
        self.tree_pedi.heading('#4', text="Valores", anchor=CENTER)
        self.mostrarDados()
