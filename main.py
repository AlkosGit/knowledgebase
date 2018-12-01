class Getdoc:
    def __init__(self, module):
        self.module = module

    def printdoc(self):
        module = __import__(self.module)
        instance = getattr(module, 'Doc')()
        print (instance)
        
        

if __name__ == '__main__':
    g = Getdoc('django')
    g.printdoc()



