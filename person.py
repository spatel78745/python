"""
Wise statements from Herr Lutz:
- "Modules tend to work best when they have a single, cohesive purpose"
- "...of course these are known as instance object attributes in Python-speak"

Wiser statements from Herr Patel:
- "use inheritance to customize, composition to build"
"""

from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job  = job
        self.pay  = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
    
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

# Finally something new
class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    # For example:
    # tom = Manager(...)
    # tom.lastName():
    # - calls Manager.__getattr__(self, lastName)
    # - calls getattr(self.person, 'lastName')
    # This overloads the '.' operator on Manager2
    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    mared = Person('Mared Rhys')
    sian  = Person('Sian Owens', job = 'detective', pay=35000)
    print(mared.name, mared.pay)
    print(sian.name, sian.pay)
    print(mared.lastName(), sian.lastName())
    sian.giveRaise(.10)
    print(sian.pay)
    print(sian)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom)
    print('---All three---')
    for object in (mared, sian, tom):
        object.giveRaise(.10)
        print(object)

    development = Department(mared, sian)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()

    
