from tkinter import *
from tkinter import ttk
import math

#
# Config
#
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

root = Tk()
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

canvas = Canvas(root)
canvas['width'] = CANVAS_WIDTH
canvas['height'] = CANVAS_HEIGHT

canvas.grid(column = 0, row = 0, sticky=(N, W, E, S))

''' Draws a circle at (x, y, r)'''
def draw_circle(circle):
  global canvas
  x, y, r = circle[0], circle[1],  circle[2]
  canvas.create_oval(x - r, y - r, x + r, y + r) 

''' Converts degrees to radians'''
def rad(degrees):
  return math.pi / 180 * degrees

''' 
Returns a point (x,y) on circle that's at an angle of theta degrees to the x-axis
'''
def point_on_circle(theta, circle):
  theta = rad(theta)
  x, y, r = circle[0], circle[1], circle[2]
  return (r * math.cos(theta) + x, y - r * math.sin(theta))

def plot_point_on_circle(theta, point_size = (CANVAS_WIDTH / 2, CANVAS_WIDTH / 2, r = 75):
  point = point_on_circle(theta, point_size[0], point_size[1], point_size[2])
  circle(point, 5)

def test_plot_point_on_circle():
  for theta in range(0, 360):
    plot_point_on_circle(theta)

#def node(theta = 30, radius = 50, x = CANVAS_WIDTH / 2, y = CANVAS_WIDTH / 2, len = 50):
#  rc_theta = rad(-90 + 0.5 * theta)
#  lc_theta = rad(-90 - (0.5 * theta))
#  rc_x = radius * math.cos(rc_theta) + x;


testPlotr()
#circle(200, 200, 20)

