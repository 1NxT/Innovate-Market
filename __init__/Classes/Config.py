from pathlib import Path

class Config():
    def  __init__(self):
        self.databasepath = Path("__init__/data3.db")
        self.imagespath = Path("__init__/Img")
        
    def database(self):
        return self.databasepath
    
    def images(self):
        return self.imagespath
