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

def circle(x, y, r):
  global canvas
  canvas.create_oval(x-r, y-r, x+r, y+r) 

def rad(deg):
  return math.pi / 180 * deg

def xr(theta, x, y, r):
  theta = rad(theta)
  return r * math.cos(theta) + x

def yr(theta, x, y, r):
  theta = rad(theta)
  return y - r * math.sin(theta)

def plotr(theta, x = CANVAS_WIDTH / 2, y = CANVAS_WIDTH / 2, r = 75):
#  theta = rad(theta)
#  xr = r * math.cos(theta) + x
#  yr = y - r * math.sin(theta)
  circle(xr(theta, x, y, r), yr(theta, x, y, r), 5)

def testPlotr():
  for theta in range(0, 360):
    plotr(theta)

#def node(theta = 30, radius = 50, x = CANVAS_WIDTH / 2, y = CANVAS_WIDTH / 2, len = 50):
#  rc_theta = rad(-90 + 0.5 * theta)
#  lc_theta = rad(-90 - (0.5 * theta))
#  rc_x = radius * math.cos(rc_theta) + x;


testPlotr()
#circle(200, 200, 20)

