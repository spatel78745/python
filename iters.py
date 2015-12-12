class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class Lurch:
    def __init__(self, catchphrase):
        self.catchphrase = catchphrase

    def __call__(self, yourName):
        print('%s, %s' % (self.catchphrase, yourName))

def manualIteration():
    print('begin')
    i = iter('ace')
    while True:
        try:
            print(i.__next__())
        except StopIteration:
            print('fini')
            break

if __name__ == '__main__':
#    manualIteration()
##    alpha = 'abcdef'
##    skipper = SkipObject(alpha)
##    I = iter(skipper)
##    print(next(I), next(I), next(I))
##
##    for x in skipper:
##        for y in skipper:
##            print(x + y, end = ' ')
    pass
            
