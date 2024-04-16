
from tkinter import *
import tkinter as tk
from tkinter import ttk

def btn_func():
    Entry_text = Entry.get()
    lable['text'] = Entry_text
    print(lable['text'])

# window
Window = tk.Tk()
Window.title('resgister')
Window.geometry('700x700')
Window.resizable(False, False)
Window.config(bg='darkgray')


string_var = tk.StringVar(value='your name')


#
lable = ttk.Label(Window, text='Entry Text', textvariable=string_var)
lable.pack()
Entry = ttk.Entry(Window, textvariable=string_var)
Entry.pack()
btn = ttk.Button(Window, text='hello', command=btn_func)
btn.pack()

# run window with loop
Window.mainloop()
