class ListProps:
    def __attrnames(self):
        result = ''
        for attr in self.__dict__:
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        if result == '':
            return '\t%s\n' % """None"""
        else:
            return result

    def __methodnames(self):
        result = ''
        self.m = list((meth for meth in dir(self) if not meth.startswith('_') and callable(getattr(self, meth))))
        for meth in self.m:
            result += '\t%s\n' % meth
        if result == '':
            return '\t%s\n' % """None"""
        else:
            return result


    def __repr__(self):
        return 'Class: {}\nAttributes:\n{}Methods:\n{}\n\n{}'.format(self.__class__.__name__, self.__attrnames(), self.__methodnames(), self.__doc__)



class Test(ListProps):
    """This is a desciption of the class"""
    def __init__(self, var):
        self.var = var
        self.data = 'hoi'
        self.data1 = 'hallo'


    def functie(self):
        pass


if __name__ == '__main__':
    t = Test('vartje')
    print (t)
