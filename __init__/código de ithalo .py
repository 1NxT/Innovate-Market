from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

tela1 = Tk()
tela1.title("Tela de Login")
tela1.geometry("600x600")
tela1.configure(bg="DodgerBlue")
tela1.resizable(False, False)
#tela1.iconbitmap('logo.ico')

img = PhotoImage(file="Logo.png")
imgcaixa = PhotoImage(file="Logo(1).png")
imgbtn2 = PhotoImage(file="produtos.png")
imgbtn3 = PhotoImage(file="pedidos.png")
imgbtn4 = PhotoImage(file="fornecedor.png")
imgbtn5 = PhotoImage(file="lucro.png")
imgbtn6 = PhotoImage(file="promocoes.png")
imgbtn7 = PhotoImage(file="gerente.png")
imgbtn8 = PhotoImage(file="troca.png")
imgbtn9 = PhotoImage(file="caixa.png")


#Defs de saida e Endrada
def Entrou():
    print("Entrou com sucesso!")

def saiu():
    print("Saindo do programa!")

def iExit():
    
    result=tkMessageBox.askquestion('AVISO','Tem certeza que deseja sair?', icon="warning")
    if result== "yes":
        tela1.destroy()
        exit

#2° Tela do programa:
def logar():
    banco = sqlite3.connect('data.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE login = '"+ent_login.get()+"'")
    resultado1 = cursor.fetchone()
    cursor.execute("SELECT * FROM usuarios WHERE senha = '"+ent_senha.get()+"'")
    resultado2 = cursor.fetchone()

    if resultado1 == None:
        lbl_dados["text"] = "Dados de usuário incorretos!"
    elif resultado2 == None:
        lbl_dados["text"] = "Dados de senha incorretos!"
    else:
        tela2 = Toplevel()
        tela2.title("Tela Inicial")
        tela2.geometry("1360x768")
        tela2.configure(bg="DodgerBlue")
        tela2.resizable(False, False)
        #tela2.iconbitmap('logo.ico')

        
    def editar_promocoes():

        edit_promo = Toplevel()
        edit_promo.title("Editar Promocoes")
        edit_promo.geometry("1366x768")
        edit_promo.configure(bg="DodgerBlue")

        def voltar_inicial_promo_edit():
            edit_promo.destroy()
            return

        def inserir():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            if ent_cupom.get() == "" or ent_nome_produto.get() == "" or ent_preco_padrao_promo.get() == "" or ent_desconto.get() == "":
                lbl_confere["text"] = "Insira todos os dados do produto!"
            else:
                cursor.execute("INSERT INTO promocoes (cupom,nome_produto,preco_padrao,desconto) VALUES ('"+ent_cupom.get()+"' , '"+ent_nome_produto.get()+"' , '"+ent_preco_padrao_promo.get()+"' , '"+ent_desconto.get()+"')")
                tree_promo_edit.insert("", "end", values=(ent_cupom.get(),ent_nome_produto.get(),ent_preco_padrao_promo.get(),ent_desconto.get()))
                banco.commit()
                
                cursor.close()
                banco.close()

        def view_edit_promo():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_promo_edit.delete(*tree_promo_edit.get_children())
            cursor.execute("SELECT * FROM promocoes ORDER BY desconto DESC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_promo_edit.insert("", "end", values=i)

        def excluir():
            try:
                item = tree_promo_edit.selection()[0]
                tree_promo_edit.delete(item)
            except:
                tkMessageBox.showinfo('ERRO', message="SELECIONE UM PRODUTO")

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_promo_edit.delete(*tree_promo_edit.get_children())
            vquery = "SELECT * FROM promocoes WHERE nome_produto LIKE '%"+ent_pesquisar.get()+"%' order by desconto"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_promo_edit.insert("","end",values=i)
       
         # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")
        
        # Frame da Treeview
        tree_promo_frame = Frame(edit_promo, padx=1, pady=10, bg="DodgerBlue")
        tree_promo_frame.place(x=0, y=0)

        ## ScrollBar        
        scroll = ttk.Scrollbar(tree_promo_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_promo_edit = ttk.Treeview(tree_promo_frame, column=("1","2","3","4"), show='headings', height=35, yscrollcommand=scroll.set)
        
        tree_promo_edit.pack()

        scroll.config(command=tree_promo_edit.yview)

        tree_promo_edit.heading('#1', text="Cupom", anchor=CENTER)
        tree_promo_edit.heading('#2', text="Nome do produto", anchor=CENTER)
        tree_promo_edit.heading('#3', text="Preço do Produto", anchor=CENTER)
        tree_promo_edit.heading('#4', text="Desconto(%)", anchor=CENTER)
        view_edit_promo()

        lbl_cupom = Label(edit_promo, text="Cupom:", bg="DodgerBlue")
        lbl_cupom.place(x=820,y=70)

        lbl_nome_produto = Label(edit_promo, text="Nome do Produto:", bg="DodgerBlue")
        lbl_nome_produto.place(x=820,y=100)

        lbl_preco_padrao_promo = Label(edit_promo, text="Preço Padrao:", bg="DodgerBlue")
        lbl_preco_padrao_promo.place(x=820,y=130)

        lbl_desconto = Label(edit_promo, text="Desconto:", bg="DodgerBlue")
        lbl_desconto.place(x=820,y=160)

        lbl_confere = Label(edit_promo, text="", fg="Red", bg="DodgerBlue")
        lbl_confere.place(x=900,y=300)

        ent_cupom = Entry(edit_promo)
        ent_cupom.place(x=1010,y=70)
        
        ent_nome_produto = Entry(edit_promo)
        ent_nome_produto.place(x=1010,y=100)

        ent_preco_padrao_promo = Entry(edit_promo)
        ent_preco_padrao_promo.place(x=1010,y=130)

        ent_desconto = Entry(edit_promo)
        ent_desconto.place(x=1010,y=160)

        ent_pesquisar = Entry(edit_promo)
        ent_pesquisar.place(x=950,y=12.5)

        btn_pesquisar_pro = Button(edit_promo, text="Pesquisar", command=pesquisar)
        btn_pesquisar_pro.place(x=1100, y=10)

        btn_show = Button(edit_promo, text="Mostrar todos", command=view_edit_promo)
        btn_show.place(x=1200,y=10)

        btn_inserir_promo = Button(edit_promo, text="Salvar", command=inserir)
        btn_inserir_promo.place(x=1000,y=200)

        btn_deletar_promo = Button(edit_promo, text="Excluir", command=excluir)
        btn_deletar_promo.place(x=1100,y=200)      

        btn_tela_cancelar_promo = Button(edit_promo, text="Voltar Para a Tela Inicial", bg="Red", font="arial 12", command=voltar_inicial_promo_edit)
        btn_tela_cancelar_promo.place(x=1100,y=600)

    def caixa():
        caixa = Toplevel()
        caixa.title("Caixa")
        caixa.geometry("1366x768")
        caixa.configure(bg="DodgerBlue")

        options=["1","2","3","4","5","6","7","8","9","10"]
        itemVariable = StringVar()
        itemVariable.set(options[0])

        def voltar_inicial_caixa():
            caixa.destroy()
            return
    
        btn_telainicial_caixa = Button(caixa, text="Voltar Para Tela Inicial", command=voltar_inicial_caixa,bg="firebrick")
        btn_telainicial_caixa.place(x=1200, y=700)

        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview Caixa
        tree_caixa_frame = Frame(caixa, padx=1, pady=10, bg="DodgerBlue")
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
        lbl_imagem_caixa = Label(caixa, image=imgcaixa, width=280, height=240, bg="DodgerBlue")
        lbl_imagem_caixa.place(x=1100,y=0)

        # Menu de opções
        menu_quantidade = OptionMenu(caixa, itemVariable, *options)
        menu_quantidade.place(x=840,y=300)

        # Botões da tela Caixa
        btn_editar = Button(caixa,text="Editar", font="arial 18")
        btn_editar.place(x=1150,y=400)

        btn_cancelar = Button(caixa,text="Cancelar", font="arial 18")
        btn_cancelar.place(x=850,y=400)

        btn_final = Button(caixa, text="Finalizar", font="arial 18")
        btn_final.place(x=1150,y=400)

        btn_excluir = Button(caixa,text="Excluir", font="arial 18")
        btn_excluir.place(x=1000,y=400)

        
        ent_cod_barras = Entry(caixa,font="arial 18")
        ent_cod_barras.place(x=830,y=60)

        
        lbl_subtotal = Label(caixa,text="SUB TOTAL:", font="arial 24",fg="black",bg="DodgerBlue")
        lbl_subtotal.place(x=0,y=527)

        lbl_total_recebido = Label(caixa, text="Total Recebido:", font="arial 24",bg="DodgerBlue")
        lbl_total_recebido.place(x=0,y=640)

        lbl_total_unitario = Label(caixa, text="Valor Unitario :", font="arial 24",bg="DodgerBlue")
        lbl_total_unitario.place(x=830,y=100)


        lbl_troco = Label(caixa, text="Troco:", font="arial 24",bg="DodgerBlue")
        lbl_troco.place(x=470,y=640)

        lbl_codigo = Label(caixa, text="ID do Produto:", font="arial 24",bg="DodgerBlue")
        lbl_codigo.place(x=830,y=10)

        lbl_total_item = Label(caixa, text="Total do item:", font="arial 24",bg="DodgerBlue")
        lbl_total_item.place(x=830,y=200)
        

    #Def de produto
    def produto():
        produtos = Toplevel()
        produtos.title("Produtos")
        produtos.geometry("1366x768")
        produtos.configure(bg="DodgerBlue")

        
        def voltar_inicial_pro():
            produtos.destroy()
            return

        def view_prod():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_pro.delete(*tree_pro.get_children())
            cursor.execute("SELECT * FROM produtos ORDER BY id_produto ASC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_pro.insert("", "end", values=i)

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_pro.delete(*tree_pro.get_children())
            vquery = "SELECT * FROM produtos WHERE nome LIKE '%"+ent_pesquisar.get()+"%' order by id_produto"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_pro.insert("","end",values=i)
        
         # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")
        
        # Frame da Treeview
        tree_pro_frame = Frame(produtos, padx=1, pady=10, bg="DodgerBlue")
        tree_pro_frame.place(x=0, y=0)

        ## ScrollBar        
        scroll = ttk.Scrollbar(tree_pro_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_pro = ttk.Treeview(tree_pro_frame, column=("Nome","Fornecedor", "Preco","Codigo de Barras"), show='headings', height=35, yscrollcommand=scroll.set)
        
        tree_pro.pack()

        scroll.config(command=tree_pro.yview)

        tree_pro.heading('#1', text="Nome", anchor=CENTER)
        tree_pro.heading('#3', text="Preco", anchor=CENTER)
        tree_pro.heading('#2', text="Codigo de Barras", anchor=CENTER)
        tree_pro.heading('#3', text="Fornecedor", anchor=CENTER)
        tree_pro.heading('#4', text="Codigo de Barras", anchor=CENTER)
        view_prod()

        ent_pesquisar = Entry(produtos)
        ent_pesquisar.place(x=950,y=10)

        btn_pesquisar_pro = Button(produtos, text="Pesquisar", command=pesquisar)
        btn_pesquisar_pro.place(x=1100, y=10)

        btn_show = Button(produtos, text="Mostrar todos", command=view_prod)
        btn_show.place(x=1000,y=50)

        btn_telainicial_pro = Button(produtos, text="Voltar a tela Inicial", command=voltar_inicial_pro)
        btn_telainicial_pro.place(x=1100, y=700)

    def editar_pro():
    
        editpro = Toplevel()
        editpro.title("Editar Produtos")
        editpro.configure(bg="DodgerBlue")
        editpro.geometry("1360x768")
        

        def voltar_inicial_pro():
            editpro.destroy()
            return

        def inserir():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            if ent_nome.get() == "" or ent_preco.get() == "" or ent_fornece.get() == "" or ent_id.get() == "":
                lbl_confere["text"] = "Insira todos os dados do produto!"
            else:
                cursor.execute("INSERT INTO produtos (nome,preco,fornecedor,id_produto) VALUES ('"+ent_nome.get()+"' , '"+ent_preco.get()+"' , '"+ent_fornece.get()+"' , '"+ent_id.get()+"')")
                tree_editpro.insert("", "end", values=(ent_nome.get(),ent_preco.get(),ent_fornece.get(),ent_id.get()))
                banco.commit()
                cursor.close()
                banco.close()

        def view_prod():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_editpro.delete(*tree_editpro.get_children())
            cursor.execute("SELECT * FROM produtos ORDER BY id_produto ASC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_editpro.insert("", "end", values=i)

        def excluir():
            try:
                item = tree_editpro.selection()[0]
                tree_editpro.delete(item)
            except:
                tkMessageBox.showinfo('ERRO', message="SELECIONE UM PRODUTO")

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_editpro.delete(*tree_editpro.get_children())
            vquery = "SELECT * FROM produtos WHERE nome LIKE '%"+ent_pesquisar.get()+"%' order by id_produto"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_editpro.insert("","end",values=i)

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")
        
        # Frame da Treeview
        tree_editpro_frame = Frame(editpro, padx=1, pady=10, bg="DodgerBlue")
        tree_editpro_frame.place(x=0, y=0)

        ## ScrollBar        
        scroll = ttk.Scrollbar(tree_editpro_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_editpro = ttk.Treeview(tree_editpro_frame, columns=("1","2","3"), show="headings", height=35, yscrollcommand=scroll.set)
        
        tree_editpro.pack()

        scroll.config(command=tree_editpro.yview)

        tree_editpro.heading('#1',text="Produto", anchor=CENTER)
        tree_editpro.heading('#2',text="Preço", anchor=CENTER)
        tree_editpro.heading('#3',text="Fornecedor", anchor=CENTER)
        view_prod()


        lbl_nome = Label(editpro, text="Nome do produto:", bg="DodgerBlue")
        lbl_nome.place(x=610,y=10)

        lbl_preco = Label(editpro, text="Preço:", bg="DodgerBlue")
        lbl_preco.place(x=610,y=40)

        lbl_fornece = Label(editpro, text="Fornecedor:", bg="DodgerBlue")
        lbl_fornece.place(x=610,y=70)

        lbl_id = Label(editpro, text="ID", bg="DodgerBlue")
        lbl_id.place(x=610,y=100)

        lbl_confere = Label(editpro, text="", bg="DodgerBlue", fg="red")
        lbl_confere.place(x=700,y=200)
        
        ent_nome = Entry(editpro)
        ent_nome.place(x=700,y=10)
        
        ent_preco = Entry(editpro)
        ent_preco.place(x=700,y=40)

        ent_fornece = Entry(editpro)
        ent_fornece.place(x=700,y=70)

        ent_id = Entry(editpro)
        ent_id.place(x=700,y=100)

        ent_pesquisar = Entry(editpro)
        ent_pesquisar.place(x=950,y=500)
        

        btn_inserir = Button(editpro, text="Inserir", command=inserir)
        btn_inserir.place(x=700,y=150)

        btn_deletar = Button(editpro, text="Excluir", command=excluir)
        btn_deletar.place(x=770,y=150)

        btn_pesquisar_pro = Button(editpro, text="Pesquisar", command=pesquisar)
        btn_pesquisar_pro.place(x=1100, y=500)

        btn_show = Button(editpro, text="Mostrar todos", command=view_prod)
        btn_show.place(x=700,y=600)

        btn_telainicial = Button(editpro, text="Voltar Para Tela Inicial", command=voltar_inicial_pro,bg="firebrick")
        btn_telainicial.place(x=1100, y=700)

    #Def de pedido
    def pedido():
        pedidos = Toplevel()
        pedidos.title("Pedidos")
        pedidos.geometry("1366x768")
        pedidos.configure(bg="DodgerBlue")

        def voltar_inicial_pedi():
            pedidos.destroy()
            return

        def view_pedido():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_pedi.delete(*tree_pedi.get_children())
            cursor.execute("SELECT * FROM pedidos ORDER BY id_pedido ASC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_pedi.insert("", "end", values=i)

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_pedi.delete(*tree_pedi.get_children())
            vquery = "SELECT * FROM pedidos WHERE cliente LIKE '%"+ent_pesquisar.get()+"%' order by id_pedido"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_pedi.insert("","end",values=i)

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_pedi_frame = Frame(pedidos, padx=1, pady=10, bg="DodgerBlue")
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
        view_pedido()

        ent_pesquisar = Entry(pedidos)
        ent_pesquisar.place(x=1000, y=20)

        btn_pesquisar_pedi = Button(pedidos, text="Pesquisar", command=pesquisar)
        btn_pesquisar_pedi.place(x=1100, y=20)

        btn_show = Button(pedidos, text="Mostrar todos", command=view_pedido)
        btn_show.place(x=1000,y=60)

        btn_telainicial_pedi = Button(pedidos, text="Voltar Para Tela Inicial", command=voltar_inicial_pedi,bg="red")
        btn_telainicial_pedi.place(x=1000, y=600)
        


    #Def de Fornecedores
    def fornecedor():
        fornecedores = Toplevel()
        fornecedores.title("Fornecedores")
        fornecedores.geometry("1366x768")
        fornecedores.configure(bg="DodgerBlue")

        def voltar_inicial_forne():
            fornecedores.destroy()
            return

        def view_forne():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_forne.delete(*tree_forne.get_children())
            cursor.execute("SELECT * FROM fornecedor ORDER BY nome ASC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_forne.insert("", "end", values=i)

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_forne.delete(*tree_forne.get_children())
            vquery = "SELECT * FROM fornecedor WHERE nome LIKE '%"+ent_pesquisar.get()+"%' order by nome"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_forne.insert("","end",values=i)
    
        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_forne_frame = Frame(fornecedores, padx=1, pady=5, bg="DodgerBlue")
        tree_forne_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_forne_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_forne = ttk.Treeview(tree_forne_frame, column=("1","2","3","4","5"), show='headings', height=35, yscrollcommand=scroll.set)
        tree_forne.pack()

        scroll.config(command=tree_forne.yview)

        tree_forne.heading('#1', text="Nome", anchor=CENTER)
        tree_forne.heading('#2', text="CNPJ", anchor=CENTER)
        tree_forne.heading('#3', text="Telefone", anchor=CENTER)
        tree_forne.heading('#4', text="Endereco", anchor=CENTER)
        tree_forne.heading('#5',text="Produto Fornecido", anchor=CENTER)
        view_forne()

        ent_pesquisar = Entry(fornecedores)
        ent_pesquisar.place(x=1100, y=20)

        btn_pesquisar_pedi = Button(fornecedores, text="Pesquisar", command=pesquisar)
        btn_pesquisar_pedi.place(x=1000, y=20)

        btn_show = Button(fornecedores, text="Mostrar todos", command=view_forne)
        btn_show.place(x=1200,y=100)

        btn_telainicial_forne = Button(fornecedores, text="Voltar Para Tela Inicial", command=voltar_inicial_forne,bg="red")
        btn_telainicial_forne.place(x=1100, y=700)


#Def de Lucro
    def lucros():
        lucro = Toplevel()
        lucro.title("Lucros")
        lucro.geometry("600x600")
        lucro.configure(bg="DodgerBlue")

        def voltar_inicial_lucros():
            lucro.destroy()
            return
    
        lbl_lucro= Label(lucro, text="Lucros:", font="arial 18", bg="blue", width=13)
        lbl_lucro.place(x=1,y=1 )
        btn_telainicial_lucro = Button(lucro, text="Voltar Para Tela Inicial", command=voltar_inicial_lucros)
        btn_telainicial_lucro.place(x=430, y=550)
        
    #DEF DE Gerenciar usuario
    def gerenciar():
        cadastro_usuario = Tk()
        cadastro_usuario.title("Gerenciar Usuários")
        cadastro_usuario.geometry("1366x768")
        cadastro_usuario.resizable(False, False)
        cadastro_usuario.configure(bg="DodgerBlue")
        
        def tela_inicial_gerenciar():
            cadastro_usuario.destroy()
            return

        def inserir():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            if ent_nome.get() == "" or ent_senha.get() == "":
                lbl_erro["text"] = "Digite todos os dados do produto"
            else:
                cursor.execute("INSERT INTO usuarios (login,senha) VALUES ('"+ent_nome.get()+"' , '"+ent_senha.get()+"')")
                tree_gere.insert("", "end", values=(ent_nome.get(),ent_senha.get()))
                banco.commit()
                cursor.close()
                banco.close()

        def view_gere():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()
            
            tree_gere.delete(*tree_gere.get_children())
            cursor.execute("SELECT * FROM usuarios ORDER BY login ASC")
            resultado = cursor.fetchall()
            for i in resultado:
                tree_gere.insert("","end",values=i)

        def excluir():
            try:
                item = tree_gere.selection()[0]
                tree_gere.delete(item)
                
            except:
                tkMessageBox.showinfo('ERRO', message="SELECIONE UM PRODUTO")

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_gere_frame = Frame(cadastro_usuario, padx=1, pady=5, bg="DodgerBlue")
        tree_gere_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_gere_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_gere = ttk.Treeview(tree_gere_frame, columns=("1","2"), show="headings",height=35, yscrollcommand=scroll.set)
        tree_gere.pack()

        scroll.config(command=tree_gere.yview)

        tree_gere.heading('#1',text="Nome De Usuario", anchor=CENTER)
        tree_gere.heading('#2',text="Senha Do Usuario", anchor=CENTER)
        view_gere()

        lbl_nome = Label(cadastro_usuario,text="Nome Do Usuario: ",font="arial 12")
        lbl_nome.place(x=400,y=100,relwidth=0.17)

        ent_nome = Entry(cadastro_usuario,bg="lightgrey")
        ent_nome.place(x=700,y=100,relwidth=0.24)
    
        lbl_senha= Label(cadastro_usuario,text="Senha: ",font="arial 12")
        lbl_senha.place(x=500,y=200,relwidth=0.07)

        ent_senha = Entry(cadastro_usuario,bg="lightgrey")
        ent_senha.place(x=700,y=200,relwidth=0.24)

        lbl_erro = Label(cadastro_usuario,text="", font="arial 12 ", fg="green", bg="DodgerBlue")
        lbl_erro.place(x=500,y=300,relwidth=0.17)
        
        btn_enviar = Button(cadastro_usuario,text="Salvar Dados", font="arial 12",command=inserir)
        btn_enviar.place(x=500,y=400,relwidth=0.24)

        btn_sair_gere = Button(cadastro_usuario,text="Voltar para a tela inicial", font="arial 12",bg="red",command=tela_inicial_gerenciar)
        btn_sair_gere.place(x=1100,y=700)

        btn_excluir = Button(cadastro_usuario,text="Excluir", font="arial 12", command=excluir)
        btn_excluir.place(x=500,y=500,relwidth=0.24)

    
       #Editar Fornecedor


    def editar_for():
        tela_editar_for = Tk()
        tela_editar_for.title("Cadastrar Fornecedores")
        tela_editar_for.geometry("1366x768")
        tela_editar_for.configure(bg="DodgerBlue")
        tela_editar_for.resizable(False, False)
        
        def voltar_inicial_tela_editr_for():
            tela_editar_for.destroy()
            return

        def inserir():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            if ent_nome_for.get() == "" or ent_CNPJ_for.get() == "" or ent_telefone_for.get() == "" or ent_endereco_for.get() == "" or ent_fornece_for.get() == "":
                lbl_confere_for["text"] = "Insira todos os dados do produto!"
            else:
                cursor.execute("INSERT INTO fornecedor (nome,CNPJ,telefone,endereco,produto_fornecido) VALUES ('"+ent_nome_for.get()+"' , '"+ent_CNPJ_for.get()+"' , '"+ent_telefone_for.get()+"' , '"+ent_endereco_for.get()+"' , '"+ent_fornece_for.get()+"')")
                tree_for.insert("", "end", values=(ent_nome_for.get(),ent_CNPJ_for.get(),ent_telefone_for.get(),ent_endereco_for.get(),ent_fornece_for.get()))
                banco.commit()
                cursor.close()
                banco.close()

        def view_for():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_for.delete(*tree_for.get_children())
            cursor.execute("SELECT * FROM fornecedor ORDER BY nome ASC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_for.insert("", "end", values=i)

        def excluir():
            try:
                item = tree_for.selection()[0]
                tree_for.delete(item)
            except:
                tkMessageBox.showinfo('ERRO', message="SELECIONE UM PRODUTO")

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_for.delete(*tree_for.get_children())
            vquery = "SELECT * FROM fornecedor WHERE nome LIKE '%"+ent_pesquisar.get()+"%' order by nome"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_for.insert("","end",values=i)

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_editfor_frame = Frame(tela_editar_for, padx=1, pady=5, bg="DodgerBlue")
        tree_editfor_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_editfor_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_for = ttk.Treeview(tree_editfor_frame, columns=("1","2","3","4","5"), show="headings",height=35, yscrollcommand=scroll.set)
        tree_for.pack()

        scroll.config(command=tree_for.yview)

        tree_for.heading('#1',text="Nome", anchor=CENTER)
        tree_for.heading('#2',text="CNPJ", anchor=CENTER)
        tree_for.heading('#3',text="Telefone", anchor=CENTER)
        tree_for.heading('#4',text="Endereço", anchor=CENTER)        
        tree_for.heading('#5',text="Produto", anchor=CENTER)
        view_for()


        lbl_nome_for = Label(tela_editar_for, text="Nome:", bg="DodgerBlue")
        lbl_nome_for.place(x=1010,y=10)

        lbl_CNPJ_for = Label(tela_editar_for, text="CNPJ", bg="DodgerBlue")
        lbl_CNPJ_for.place(x=1010,y=40)

        lbl_telefone_for = Label(tela_editar_for, text="Telefone:", bg="DodgerBlue")
        lbl_telefone_for.place(x=1010,y=70)

        lbl_endereco_for = Label(tela_editar_for, text="Endereço", bg="DodgerBlue")
        lbl_endereco_for.place(x=1010,y=100)

        lbl_fornece_for = Label(tela_editar_for, text="Produto Fornecido:", bg="DodgerBlue")
        lbl_fornece_for.place(x=1010,y=130)

        lbl_confere_for = Label(tela_editar_for, text="", bg="DodgerBlue")
        lbl_confere_for.place(x=1010,y=130)

        ent_confere_for = Entry(tela_editar_for)
        ent_confere_for.place(x=1100,y=130)
        
        ent_nome_for = Entry(tela_editar_for)
        ent_nome_for.place(x=1100,y=10)

        ent_CNPJ_for = Entry(tela_editar_for)
        ent_CNPJ_for.place(x=1100,y=40)
        
        ent_telefone_for = Entry(tela_editar_for)
        ent_telefone_for.place(x=1100,y=70)

        ent_endereco_for = Entry(tela_editar_for)
        ent_endereco_for.place(x=1100,y=100)
        
        ent_fornece_for = Entry(tela_editar_for)
        ent_fornece_for.place(x=1100,y=130)

        ent_pesquisar = Entry(tela_editar_for)
        ent_pesquisar.place(x=950,y=500)
        

        btn_inserir_for = Button(tela_editar_for, text="Salvar", command=inserir)
        btn_inserir_for.place(x=1100,y=200)

        btn_deletar_for = Button(tela_editar_for, text="Excluir", command=excluir)
        btn_deletar_for.place(x=1170,y=200)

        btn_pesquisar_for = Button(tela_editar_for, text="Pesquisar", command=pesquisar)
        btn_pesquisar_for.place(x=1100, y=500)

        btn_show = Button(tela_editar_for, text="Mostrar todos", command=view_for)
        btn_show.place(x=1000,y=600)


    def edit_pedi():
        edit_pedidos = Tk()
        edit_pedidos.title("Editar Pedidos")
        edit_pedidos.geometry("1360x768")
        edit_pedidos.configure(bg="DodgerBlue")
        edit_pedidos.resizable(False, False)
        
        def voltar_inicial_tela_edit_pedi():
            edit_pedidos.destroy()
            return

        def inserir():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            if ent_produto_pedi.get() == "" or ent_cliente_pedi.get() == "" or ent_total_pedi.get() == "" or ent_numero_pedi.get() == "":
                lbl_confere["text"] = "Insira todos os dados do produto!"
            else:
                cursor.execute("INSERT INTO pedidos (nome_produto,cliente,valor_total,id_pedido) VALUES ('"+ent_produto_pedi.get()+"' , '"+ent_cliente_pedi.get()+"' , '"+ent_total_pedi.get()+"' , '"+ent_numero_pedi.get()+"')")
                tree_edit_pedi.insert("", "end", values=(ent_produto_pedi.get(),ent_cliente_pedi.get(),ent_total_pedi.get(),ent_numero_pedi.get()))
                banco.commit()
                cursor.close()
                banco.close()

        def view_pedi():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_edit_pedi.delete(*tree_edit_pedi.get_children())
            cursor.execute("SELECT * FROM pedidos ORDER BY id_pedido ASC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_edit_pedi.insert("", "end", values=i)

        def excluir():
            try:
                item = tree_edit_pedi.selection()[0]
                tree_edit_pedi.delete(item)
            except:
                tkMessageBox.showinfo('ERRO', message="SELECIONE UM PRODUTO")

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_edit_pedi.delete(*tree_edit_pedi.get_children())
            vquery = "SELECT * FROM pedidos WHERE cliente LIKE '%"+ent_pesquisar.get()+"%' order by id_pedido"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_edit_pedi.insert("","end",values=i)        

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_editpedi_frame = Frame(edit_pedidos, padx=1, pady=5, bg="DodgerBlue")
        tree_editpedi_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_editpedi_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_edit_pedi = ttk.Treeview(tree_editpedi_frame, columns=("1","2","3","4"), show="headings",height=35, yscrollcommand=scroll.set)
        tree_edit_pedi.pack()

        scroll.config(command=tree_edit_pedi.yview)

        tree_edit_pedi.heading('#1',text="Nome do Produto", anchor=CENTER)
        tree_edit_pedi.heading('#2',text="Cliente", anchor=CENTER)
        tree_edit_pedi.heading('#3',text="Valor Total", anchor=CENTER)
        tree_edit_pedi.heading('#4',text="ID do Pedido", anchor=CENTER)
        view_pedi()

        lbl_produto_pedi = Label(edit_pedidos, text="Nome do produto:", bg="DodgerBlue")
        lbl_produto_pedi.place(x=810,y=10)

        lbl_cliente_pedi = Label(edit_pedidos, text="Cliente:", bg="DodgerBlue")
        lbl_cliente_pedi.place(x=810,y=40)

        lbl_total_pedi = Label(edit_pedidos, text="Valor total", bg="DodgerBlue")
        lbl_total_pedi.place(x=810,y=70)

        lbl_numero_pedi = Label(edit_pedidos, text="ID do pedido:", bg="DodgerBlue")
        lbl_numero_pedi.place(x=810,y=100)


        lbl_confere = Label(edit_pedidos, text="", fg="green")
        lbl_confere.place(x=810,y=200)

        ent_produto_pedi = Entry(edit_pedidos)
        ent_produto_pedi.place(x=950,y=10)

        ent_cliente_pedi = Entry(edit_pedidos)
        ent_cliente_pedi.place(x=900,y=40)

        ent_total_pedi = Entry(edit_pedidos)
        ent_total_pedi.place(x=900,y=70)
        
        ent_numero_pedi = Entry(edit_pedidos)
        ent_numero_pedi.place(x=950,y=100)

        ent_pesquisar = Entry(edit_pedidos)
        ent_pesquisar.place(x=1150,y=10)

        
        btn_inserir_pedi = Button(edit_pedidos, text="inserir", command=inserir)
        btn_inserir_pedi.place(x=900,y=150)

        btn_deletar_pedi = Button(edit_pedidos, text="excluir", command=excluir)
        btn_deletar_pedi.place(x=970,y=150)

        btn_pesquisar_pedi = Button(edit_pedidos, text="Pesquisar", command=pesquisar)
        btn_pesquisar_pedi.place(x=1160, y=40)

        btn_show = Button(edit_pedidos, text="Mostrar todos", command=view_pedi)
        btn_show.place(x=1000,y=600)

        btn_voltar_tela_edit_pedi = Button(edit_pedidos, text="Voltar para a Tela Inicial",command=voltar_inicial_tela_edit_pedi,bg="red")
        btn_voltar_tela_edit_pedi.place(x=1160, y=500)

    #DEF DE PROMOÇÕES
    def pro():
        promocoes = Toplevel()
        promocoes.title("Promocoes")
        promocoes.geometry("1360x768")
        promocoes.configure(bg="DodgerBlue")

        def voltar_inicial_promocoes():
            promocoes.destroy()
            return

        def view_promo():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_promo.delete(*tree_promo.get_children())
            cursor.execute("SELECT * FROM promocoes ORDER BY nome_produto ASC")
            res_view = cursor.fetchall()
            for i in res_view:
                tree_promo.insert("", "end", values=i)

        def pesquisar():
            banco = sqlite3.connect("data.db")
            cursor = banco.cursor()

            tree_promo.delete(*tree_promo.get_children())
            vquery = "SELECT * FROM promocoes WHERE nome_produto LIKE '%"+ent_pesquisar.get()+"%' order by desconto"
            cursor.execute(vquery)
            res_pesquisa = cursor.fetchall()
            for i in res_pesquisa:
                tree_promo.insert("","end",values=i)

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Frame da Treeview
        tree_promo_frame = Frame(promocoes, padx=1, pady=5, bg="DodgerBlue")
        tree_promo_frame.place(x=0, y=0)

        # ScrollBar
        scroll = ttk.Scrollbar(tree_promo_frame)
        scroll.pack(side=RIGHT, fill=Y, padx=0)

        tree_promo = ttk.Treeview(tree_promo_frame,column=("1","2","3","4"), show='headings', height=35, yscrollcommand=scroll.set)
        tree_promo.pack()

        scroll.config(command=tree_promo.yview)

        tree_promo.heading('#1', text="Cupom", anchor=CENTER)
        tree_promo.heading('#2', text="Nome do Produto", anchor=CENTER)
        tree_promo.heading('#3', text="Preço do Produto", anchor=CENTER)
        tree_promo.heading('#4', text="Desconto", anchor=CENTER)
        view_promo()


        ent_pesquisar = Entry(promocoes)
        ent_pesquisar.place(x=1100, y=20)

        btn_pesquisar_pedi = Button(promocoes, text="Pesquisar", command=pesquisar)
        btn_pesquisar_pedi.place(x=1000, y=20)

        btn_show = Button(promocoes, text="Mostrar todos", command=view_promo)
        btn_show.place(x=1200,y=100)

        btn_telainicial_promo = Button(promocoes, text="Voltar Para Tela Inicial",bg="red", command=voltar_inicial_promocoes)
        btn_telainicial_promo.place(x=1100, y=550)

            

#Defs 2° Tela:
    def iExit2():
        tela2.destroy()
        return
    
##################  BUTTONS 2° TELA  ########################


    btn_caixa = Button(tela2, text="Caixa", width=15, height=2,command=caixa) 
    btn_caixa.grid(row=2,column=8)

    btn_produtos = Button(tela2, text='Produtos',width=15, height=2,command=produto)
    btn_produtos.grid(row=2,column=2)

    btn_pedidos = Button(tela2, text='Pedidos',width=15, height=2,command=pedido)
    btn_pedidos.grid(row=2,column=3)

    btn_fornecedores = Button(tela2, text='Fornecedores',width=15, height=2, command=fornecedor)
    btn_fornecedores.grid(row=2,column=4)

    btn_lucro = Button(tela2, text='Lucro',width=15, height=2,command=lucros)
    btn_lucro.grid(row=2,column=5)

    btn_Editarpro = Button(tela2, text='Editar Produtos',width=15, height=2, command=editar_pro)
    btn_Editarpro.grid(row=4,column=2)

    btn_Editarpedi = Button(tela2, text='Editar Pedidos',width=15, height=2,command=edit_pedi)
    btn_Editarpedi.grid(row=4,column=3)

    btn_Editarfor = Button(tela2, text='Editar Fornecedores',width=15, height=2,command=editar_for)
    btn_Editarfor.grid(row=4,column=4)
    
    btn_Editarpromo = Button(tela2, text='Editar Promocoes',width=15, height=2,command=editar_promocoes)
    btn_Editarpromo.grid(row=4,column=6)

    btn_editar_lucro = Button(tela2, text="Editar Lucro", width=15, height=2)
    btn_editar_lucro.grid(row=4,column=5)
        
        
    btn_promocao = Button(tela2, text='Promocoes',width=15, height=2, command=pro)
    btn_promocao.grid(row=2,column=6)


    btn_gerenciar = Button(tela2, text='Gerenciar Usuários',width=15, height=2, command=gerenciar)
    btn_gerenciar.grid(row=2,column=7)

    btn_voltar = Button(tela2, text="Logout", width=20, command=iExit2, bg="firebrick")
    btn_voltar.place(x=1150, y=700)

    #ICON BUTTONS 2° tela
    btn_img9 = Button(tela2, image=imgbtn9, width=140, height=140, bg="DodgerBlue", command=caixa, relief="flat")
    btn_img9.grid(row=1,column=8)

    btn_img2 = Button(tela2, image=imgbtn2,  width=140, height=140, bg="DodgerBlue", command=produto,relief="flat")
    btn_img2.grid(row=1,column=2)

    btn_img3 = Button(tela2, image=imgbtn3,  width=140, height=140, bg="DodgerBlue", command=pedido,relief="flat")
    btn_img3.grid(row=1,column=3)

    btn_img4 = Button(tela2, image=imgbtn4,  width=140, height=140, bg="DodgerBlue", command=fornecedor,relief="flat")
    btn_img4.grid(row=1,column=4)


    btn_img5 = Button(tela2, image=imgbtn5,  width=140, height=140, bg="DodgerBlue", command=lucros,relief="flat")
    btn_img5.grid(row=1,column=5)

    btn_img6 = Button(tela2, image=imgbtn6,  width=140, height=140, bg="DodgerBlue", command=pro,relief="flat")
    btn_img6.grid(row=1,column=6)

    btn_img7 = Button(tela2, image=imgbtn7,  width=140, height=140, bg="DodgerBlue", command=gerenciar,relief="flat")
    btn_img7.grid(row=1,column=7)


#LABELS 1° TELA
lbl_login = Label(tela1, text="Login: ", font="arial 18", bg="DodgerBlue", width=6)
lbl_login.place(x=150, y=295)

lbl_senha = Label(tela1, text="Senha: ", font="arial 18", bg="DodgerBlue")
lbl_senha.place(x=150, y=350)

lbl_imagem = Label(tela1, image=img, width=280, height=240, bg="DodgerBlue")
lbl_imagem.place(x=175,y=0)

lbl_dados=Label(tela1, text="", bg="DodgerBlue", font="arial 18", fg="red")
lbl_dados.place(x=140, y=400)
#ENTRYS 1° TELA
ent_login = Entry(tela1, font=("arial", 12), width=18)
ent_login.place(x=240, y=300)

ent_senha = Entry(tela1, font=("arial", 12), width=18, show="*")
ent_senha.place(x=240, y=355)

#BUTTONS 1° TELA
btn_entrar = Button(tela1, text="Entrar", command=logar, width=30, height=2, bg="cyan")
btn_entrar.place(x=190, y=450)

btn_sair = Button(tela1, text="Sair", command=iExit, width=15, bg="firebrick")
btn_sair.place(x=430, y=550)


#Variaveis para adicionar produtos

cod_barras = StringVar()
preco = IntVar()
quant_prod = IntVar()
nome_prod = IntVar()
procurar = StringVar()


tela1.mainloop()
