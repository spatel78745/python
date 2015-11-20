from tkinter import *
from tkinter import ttk 

#
# Frames
#
root = Tk()
frame = ttk.Frame(root)
frame.grid()
# see how a tuple is used to pass multiple figures
# (left, top, right, bottom)
# (all the way around)
# (horizontal, vertical)
frame['padding'] = (5, 10)
frame['borderwidth'] = 20
frame['relief'] = 'sunken'

#
# Labels
#
label = ttk.Label(frame, text='My Label')
label.grid()
resultsContents = StringVar()
# Hook a variable to a widget using textvariable
label['textvariable'] = resultsContents
resultsContents.set('New value to display')
print(resultsContents.get())

#
# Images
#
image = PhotoImage(file='hitler.jpg')
label['image'] = image


