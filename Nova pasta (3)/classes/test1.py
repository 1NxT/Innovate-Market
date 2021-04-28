from tkinter import *
class Test():
    def __init__(self):
        self.tk = Tk()
        self.geometry()
        self.tk.mainloop()
        
    
    def geometry(self):
        self.tk.title("Teste")
        self.tk.geometry("800x720")
        self.tk.resizable(False, False)
    
    

