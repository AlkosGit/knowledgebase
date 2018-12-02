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


class Window(Getdoc):
    def __init__(self):
        root = Tk()
        root.geometry('200x200')
        f = Frame(root)
        f.pack()
        var = StringVar()
        values = self.listdocs()
        omenu = OptionMenu(f, var, *values, command=self.output)
        omenu.pack()
        self.text = Text(f)
        self.text.pack()

    def output(self, value):
        self.text.delete(1.0, END)
        g = Getdoc(value)
        text = g.printdoc()
        self.text.insert(1.0, text)


          

        

if __name__ == '__main__':
    Window()
    mainloop()



