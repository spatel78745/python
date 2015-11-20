from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid()
button['text']
button.configure('text')
button['text'] = 'goodbye'
button.configure(text='all composite phenomena are impermanent')
button.confiure()
