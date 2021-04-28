from tkinter import *
class Test():
    def __init__(self):
        self.tk = Toplevel()
        self.geometry()
        self.tela()
        self.tk.mainloop()
        
    
    def geometry(self):
        self.tk.title("Teste")
        self.tk.geometry("800x720")
        self.tk.resizable(False, False)

    def tela(self):
        self.button_tal = Button(self.tk, text="JAIR GAY")
        self.button_tal.place(x=500, y=500)
    
    

