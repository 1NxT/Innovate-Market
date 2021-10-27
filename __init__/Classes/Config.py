from pathlib import Path

class Config():
    def  __init__(self):
        self.__databasepath = Path("__init__/data3.db")
        self.__imagespath = Path("__init__/Img")
        
    def database(self):
        return self.__databasepath
    
    def images(self):
        return self.__imagespath
