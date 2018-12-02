from os import popen
from tkinter import *

class Getdoc:
    def __init__(self, module):
        self.module = module

    def printdoc(self):
        module = __import__(self.module)
        instance = getattr(module, 'Doc')()
        return instance

    def listdocs(self):
        files = popen('ls *.py').read().splitlines() # remove trailing '\n'
        names = []
        for name in files:
            if not 'main' in name and not 'listprops' in name:
                names.append(name.rstrip('.py')) # remove file extension
        return names


        
           

        

if __name__ == '__main__':
    g = Getdoc('django')
    print (g.listdocs())



