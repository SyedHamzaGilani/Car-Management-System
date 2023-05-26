from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Geometry")
root.geometry('500x500')
root.resizable(False, False)
root.config(bg = "Cyan")
Label(root, bg = "Cyan").pack(pady = 50)
Label(root, text = f'The width of screen is {root.winfo_screenwidth()}', fg = "Blue", bg = "Cyan", font = "Conicsansms 20 bold").pack(pady = 50)
Label(root, text = f'The Height of screen is {root.winfo_screenheight()}', fg = "Blue", bg = "Cyan", font = "Conicsansms 20 bold").pack()
root.mainloop()
