"""
Remember that namespaces are packages of variables, and that variables refer
to objects, and that objects have attributes, and attributes are key value
pairs, and that variables have values.
"""

from person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')

for object in (bob, sue, tom):
    db[object.name] = object
db.close()
