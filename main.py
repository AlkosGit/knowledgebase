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
        root.geometry('600x450')
        root.title('Docstring Reader')
        f = Frame(root)
        f.pack(fill=BOTH, expand=True)
        var = StringVar()
        values = self.listdocs()
        omenu = OptionMenu(f, var, *values, command=self.output)
        omenu.pack(padx=20, pady=10)
        omenu.config(width=10)
        self.text = Text(f)
        self.text.pack(fill=BOTH, expand=True, pady=10, padx=10)

    def output(self, value):
        self.text.delete(1.0, END)
        g = Getdoc(value)
        text = g.printdoc()
        self.text.insert(1.0, text)


          

        

if __name__ == '__main__':
    Window()
    mainloop()



