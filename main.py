from tkinter import *
Window = Tk()
Window.title('resgister')
Window.geometry('700x700')
Window.resizable(False, False)
Window.config(bg='darkgray')


Register = Button(Window, text='Register').place(x=100, y=100)



Window.mainloop()