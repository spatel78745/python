from functools import *

def partition(p, x):
    lines, notLines = p
    if '\n' in x: lines.append(x)
    else:         notLines.append(x)
    
    return (lines, notLines)

chunk = 'drawNode 1 4\nline2\na longer line3\ndrawN'
lines = chunk.splitlines(True)

#reduce(append(l, x), lines, [])
