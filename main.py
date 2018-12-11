from os import popen
from tkinter import *
import glob

class Getdoc:
    def __init__(self, file):
        self.file = file
        self.filename = '{}.txt'.format(self.file)

    def printdoc(self):
#        Keep around for future reference. Call a module by name (self.module), and create an instance.        
#        module = __import__(self.module)
#        instance = getattr(module, 'Doc')()
#        return instance
        filetext = ''
        with open(self.filename, 'r') as lines:
            for line in lines:
                filetext += line
        return filetext

    def listdocs(self):
        names = []
        for name in glob.glob('*.txt'):
            if not 'main' in name:
                names.append(name[:-4].lower()) # remove file extension
        return sorted (names)

    def savedoc(self, textstring):
        with open(self.filename, 'w') as f:
            f.write(textstring)
        

class Window(Getdoc):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x500')
        self.root.title('Docstring Reader')
        #  Initialize frames.
        self.frames = {'f1' : 'self.topframe','f2' : 'self.textframe', 'f3' : 'self.bottomframe'}
        for frame in self.frames.values():
            exec('{} = Frame(self.root)'.format(frame))
        
    def switchframe(self):
        #  Destroy and reinitialize frames.
        for frame in self.frames.values():
            exec('{}.destroy()'.format(frame))
            exec('{} = Frame(self.root)'.format(frame))
        Grid.columnconfigure(self.textframe, 0, weight=1)
        Grid.rowconfigure(self.textframe, 0, weight=1)
        Grid.columnconfigure(self.bottomframe, 0, weight=1)
        Grid.rowconfigure(self.bottomframe, 0, weight=1)

    def display(self):
        self.var = StringVar()
        self.switchframe()
        self.topframe.pack(fill=BOTH)
        self.textframe.pack(fill=BOTH, expand=True)
        self.bottomframe.pack(fill=BOTH)
        values = self.listdocs()
        omenu = OptionMenu(self.topframe, self.var, *values, command=self.output)
        omenu.config(width=20)
        omenu.pack(pady=10)
        self.text = Text(self.textframe)
        self.text.grid(column=0, row=0, padx=10, pady=5, sticky='nsew')
        bnew = Button(self.bottomframe, text='New', command=self.new)
        bnew.grid(column=0, row=0, padx=10, pady=5, sticky='e')

    def output(self, value):
        self.bottomframe.destroy()
        self.bottomframe = Frame(self.root)
        self.bottomframe.pack(fill=BOTH, pady=5)
        Grid.columnconfigure(self.bottomframe, 0, weight=1)
        self.bedit = Button(self.bottomframe, text='Edit', command=self.edit)
        self.bedit.grid(column=0, row=0, padx=10, sticky='e')
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        g = Getdoc(value)
        text = g.printdoc()
        self.text.insert(1.0, text)
        self.text.config(state=DISABLED)

    def edit(self):
        self.topframe.destroy()
        self.topframe = Frame(self.root)
        self.topframe.pack(before=self.textframe)
        ledit = Label(self.topframe, text='***EDIT MODE***')
        ledit.pack(pady=5)
        self.bedit.destroy()
        self.bcancel = Button(self.bottomframe, text='Cancel', command=self.display)
        self.bcancel.grid(column=0, row=0, padx=10, sticky='e')
        self.bsave = Button(self.bottomframe, text='Save', command=self.save)
        self.bsave.grid(column=1, row=0, padx=10, sticky='e')
        self.text.config(state=NORMAL)

    def new(self):
        self.display()
        self.edit()
        self.ledit.destroy()

    def save(self):
        filename = self.var.get()
        textstring = self.text.get(1.0, END)
        g = Getdoc(filename)
        g.savedoc(textstring)
        self.display()


if __name__ == '__main__':
    win = Window()
    win.display()
    mainloop()



