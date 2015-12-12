def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
"""
Oh, now this is exceptionally clever. It is called a 'closure' or a 'factory
function, or as puhVON would say, 'punksun'
"""

def f2Maker(x):
    def f2(y):
        print(x + y)
    return f2

def tester(start):
#    state = start
    def nested(label):
        nonlocal start
        print(label, start)
        start += 1
    return nested
