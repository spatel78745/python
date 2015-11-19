from swampy.TurtleWorld import *

def check_fermat(a, b, c, n):
    if (n > 2) and (a**n + b**n == c**n):
        print 'Holy smokes, Fermat was wrong!'
    else:
        print "No that doesn't work"

def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print 'No'
    else:
        print 'Yes'

# a = raw_input('Enter side 1: ')
# b = raw_input('Enter side 2: ')
# c = raw_input('Enter side 3: ')
# is_triangle(int(a), int(b), int(c))

# check_fermat(3, 4, 5, 2)
# check_fermat(3, 4, 5, 5)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
draw(bob, 5, 10)
print 'Done!'

wait_for_user()


