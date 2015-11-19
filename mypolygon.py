from swampy.TurtleWorld import *
from math import pi

def square(t, l):
  for i in range(4):
    fd(t, l)
    lt(t)

def partial_polygon(t, l, total_sides, num_sides):
  for i in range(num_sides):
    fd(t, l)
    lt(t, 360 / total_sides)

def test_partial_polygon():
  partial_polygon(bob, 100, 4, 3)

def polygon(t, l, n):
  partial_polygon(t, l, n, n)

def arc(t, r, angle):
  partial_polygon(t, 2 * pi * r / 360, 360, angle)

def test_arc():
  print 'test_arc'
  arc(bob, 50, 180)

def circle(t, r):
  arc(t, r, 360)

def test_circle():
  circle(bob, 50)
  square(bob, 100)

def test_square():
  square(bob, 100)
  square(bob, 110)
  square(bob, 120)
  square(bob, 130)
  square(bob, 140)
  square(bob, 150)

def test_polygon():
  polygon(bob, 100, 3)
  polygon(bob, 100, 4)
  polygon(bob, 100, 5)
  polygon(bob, 100, 6)
  polygon(bob, 100, 7)
  polygon(bob, 100, 8)

def curve(turtle, angle, step):
  lt(turtle, angle)
  for i in range(180 - (2 * angle)):
    fd(turtle, step)
    lt(turtle, 1)

def petal(turtle, angle, step):
  curve(turtle, angle, step)
  lt(turtle, angle)
  curve(turtle, angle, step)

def flower(turtle, angle):
  for i in range (360 / angle):
    petal(turtle, 30, 1)
    lt(turtle, angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.00001 

flower(bob, 60)

wait_for_user()
