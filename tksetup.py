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
def drawCircle(circle):
  global canvas
  x, y, r = circle[0], circle[1],  circle[2]
  canvas.create_oval(x - r, y - r, x + r, y + r) 

''' Converts degrees to radians'''
def rad(degrees):
  return math.pi / 180 * degrees

''' 
Returns a point (x,y) on circle that's at an angle of theta degrees to the x-axis
'''
def pointOnCircle(theta, circle):
  theta = rad(theta)
  x, y, r = circle[0], circle[1], circle[2]
  return (r * math.cos(theta) + x, y - r * math.sin(theta))

'''
Plots a dot on the circumference of a circle
- originX, originY: The origin of the circle
-                r: The radius of the dot
'''
def plotDotOnCircle(theta, circle = (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, 50), dotRadius = 5):
# Calculate the center of the dot
  center = pointOnCircle(theta, circle)
  drawCircle((center[0], center[1], dotRadius))

def testPlotDotOnCircle():
  for theta in range(0, 360):
    plotDotOnCircle(theta)

#def node(theta = 30, radius = 50, x = CANVAS_WIDTH / 2, y = CANVAS_WIDTH / 2, len = 50):
#  rc_theta = rad(-90 + 0.5 * theta)
#  lc_theta = rad(-90 - (0.5 * theta))
#  rc_x = radius * math.cos(rc_theta) + x;


testPlotDotOnCircle()
#circle(200, 200, 20)

