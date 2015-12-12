class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    uses __X names to avoid clashing with client's attrs
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,    # My class's name
            id(self),                   # My address
            self.__attrnames())         # name = value list
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result

if __name__ == '__main__':
    class Spam(ListInstance):
        def __init__(self):
            self.data1 = 'food'
        def makeSpam(self): pass

    x = Spam()
    print(x)

class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def first(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
def func(a, b, *args):
    print(type(args))
    for i in (a, b, args):
        print(type(i))
        
def func2(a, b, c):
    print('a = %d, b = %d, c = %d' % (a, b, c))
