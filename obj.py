"""
Aphorisms

When you see 'namespace,' visualize a dictionary.

Why still so tickled when you pass different types? You still don't understand...
  - f('Julius Caesar')
  - f(3.14159)

'dir([object]) -> list of strings' returns the names in the current scope

In Python, one inherits attributes.

Again we encounter 'override' or as master Stroustrup says 'virtual'

To specialize a function, one may:
- copy it under another name, then rewrite it
- add a special case in-place

To specialize a method, one may:
- subclass and rewrite the method, calling the superclass version if one wants

Now, which is better?

Memorize the list methods. This is important. Make them an attribute of the
mind.

All that is is object. All that is not is object. WTF man.

Surprisingly, this is a 'struct':
class rec: pass
rec.name = 'Sian'
rec.age = 31

N.B. my middle-aged apprentice:
x.__class__ is a link to the class of x

"OOP in Python is mostly about looking up attributes in linked
namespace objects. So sayeth the Lutz.
"""

class ygyll: pass
    # Damn I forgot what I wanted to do

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other

