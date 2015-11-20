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

def plotr(theta, x = 200, y = 200, r = 75):
  theta = rad(theta)
  xr = r * math.cos(theta) + x
  yr = y - r * math.sin(theta)
  circle(xr, yr, 5)

def testPlotr():
  for theta in range(0, 360):
    plotr(theta)

# testPlotr()
#circle(200, 200, 20)

