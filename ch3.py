def repeat_lyrics():
  print_lyrics()
  print_lyrics()

def print_lyrics():
  print "I'm a lumberjack, and I'm okay."
  print "I sleep all night and I work all day."

# repeat_lyrics()

### 3-3
def right_justify(s):
    print (70 - len(s)) * ' ' + s;

# right_justify('allen');

### 3-4
def do_twice(f, v):
    f(v)
    f(v)

def print_twice(s):
    print s * 2;

def print_once(s):
    print s

def do_four(f, v):
    do_twice(f, v)
    do_twice(f,v)

# do_twice(print_twice, 'spam');
# do_four(print_twice, 'spam ');

def print_row(d):
    print '+....' * d + '+'
    print '|    ' * d + '|'
    print '|    ' * d + '|'
    print '|    ' * d + '|'
    print '|    ' * d + '|'
    print '+....' * d + '+'

def grid2():
    do_twice(print_row, 2)

def grid4():
    do_twice(print_row, 4)

grid2()
grid4()

