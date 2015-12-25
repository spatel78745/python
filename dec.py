class Decorator:
    def __init__(self, C):
        print('hello from __init__', C)
        self.C = C

    def __call__(self, *args):
        print('hello from __call__', args)
        self.wrapped = self.C(*args)
        return self

    def __getattr__(self, attrname):
        return getattr(self.wrapped, attrname)

#@Decorator
#class C: pass

def decorator(A, B):
    print('in decorator', A, B)
    def actualDecorator(F):
        print('in actual decorator', A, B)
        def augmentedF(*args):
            print('in augmentedF', A, B, args)
            F(*args)
        return augmentedF
    return actualDecorator

@decorator('AAA', 'BBB')
def F(x, y):
    print('in f', x, y)

F(6, 9)

