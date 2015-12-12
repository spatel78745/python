class MyClass:
    # Can you call a method without qualifying it with 'self.'?

    val = 69
    
    def __init__(self, val):
        self.val = val

    def addOne(self):
        self.val += 1

    def printNextVal(self):
        print('Going through the class')
        MyClass.addOne(self);
        self.addOne()
        print('next val: ', self.val)

    def mixedNames(self):
        print(self.val, MyClass.val)

mc = MyClass(0)
