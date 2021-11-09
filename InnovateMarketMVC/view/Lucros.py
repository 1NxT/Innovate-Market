from tkinter import *
#import seaborn as sns
#import matplotlib.pyplot as plt
from model.Config import *

class Lucros():
    def __init__(self):
        self.telalucro = Toplevel()
        self.geometry()
        
        self.elementos()

    def geometry(self):
        self.telalucro.title("Lucro")
        self.telalucro.geometry("1360x760")
        self.telalucro.configure(bg="DodgerBlue")
        self.telalucro.resizable(False, False)
        # self.__iconImagemPath = imagespath / "logo.ico"
        # self.telalucro.iconbitmap(self.__iconImagemPath)
        
    def voltar_inicial_lucros(self):
        self.telalucro.destroy()
        return
    
    def elementos(self):        
        self.btn_telainicial_lucro = Button(self.telalucro, text="Voltar Para Tela Inicial", command=self.voltar_inicial_lucros, bg="red")
        self.btn_telainicial_lucro.place(x=430, y=550)
        
        self.lbl_lucro= Label(self.telalucro, text="Lucros:", font="arial 18", bg="DodgerBlue", width=13)
        self.lbl_lucro.place(x=1,y=1 )
        
        # self.sns.lineplot(data=variavel_dos_dados)
        #self.plt.show()
