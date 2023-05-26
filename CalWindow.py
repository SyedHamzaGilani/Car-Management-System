import calendar
import tkinter.ttk
from datetime import date
from tkinter import *
import ctypes

class calWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Calander")
        self.root.state('zoomed')
        self.root.minsize(1366, 768)
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default='media/logo.ico')
        self.root.config(bg = "grey")
        self.i = 0
        self.Changebg()
        today = date.today()
        year = int(today.strftime('%Y'))
        self.frame = Frame(self.root, bd = 5, relief = SUNKEN, bg = "Blue")
        self.frame.place(x = 5, y = 10, width = 1355, height = 50)
        self.h = Label(self.frame, text = f"CALANDER OF YEAR {2022}", bg = "Blue", fg = "Cyan", font = "Algerian 25 bold underline italic")
        self.h.pack(pady = 5)
        self.frame1 = Frame(self.root, bg = "Blue", bd = 5, relief = SUNKEN)
        self.frame1.place(x = 290, y = 65, width = 1068, height = 670)
        self.yyyy = Label(self.frame1, text = f"{calendar.calendar(year)}", font = "Consolas 11 bold", fg = "Cyan", bg = "Blue")
        self.yyyy.pack()
        self.frame2 = Frame(self.root, bg = "Blue", bd = 5, relief = SUNKEN)
        self.frame2.place(x = 5, y = 65, width = 280, height = 670)
        self.year = StringVar()
        self.year.set(year)
        Label(self.frame2, text = "Select  Year", font = "algerian 18 bold", fg = "Cyan", bg = "Blue").place(x = 5, y = 250)
        yy = tkinter.ttk.Combobox(self.frame2, textvariable = self.year, font = "Courier 12 bold")
        yy['values'] = ['2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050']
        yy.place(x = 5, y = 300)
        Button(self.frame2, text = "OK", font = "Courier 15 bold", bg = "Cyan", fg = "Blue", cursor = "hand1", command = self.getYear).place(x = 100, y = 350, width = 150)
        Button(self.frame2, text = "EXIT NOW", font = "Courier 15 bold", bg = "Cyan", fg = "Blue", cursor = "hand1", command = self.root.destroy).place(x = 100, y = 400, width = 150)

    def getYear(self):
        self.a = int(self.year.get())
        self.frame.destroy()
        self.frame1.destroy()
        self.frame = Frame(self.root, bd=5, relief=SUNKEN, bg="Blue")
        self.frame.place(x=5, y=10, width=1355, height=50)
        self.h = Label(self.frame, text=f"CALANDER OF YEAR {self.a}", bg="Blue", fg="Cyan",font="Algerian 25 bold underline italic")
        self.h.pack(pady=5)
        self.frame1 = Frame(self.root, bg="Blue", bd=5, relief=SUNKEN)
        self.frame1.place(x=290, y=65, width=1068, height=670)
        self.yyyy = Label(self.frame1, text=f"{calendar.calendar(self.a)}", font="Consolas 11 bold", fg="Cyan", bg="Blue")
        self.yyyy.pack()

    def Changebg(self):
        color = ['pink', 'light green', 'grey', 'yellow', 'Hot Pink', '#24dd28', 'sea green']
        if self.i >= len(color):
            self.i = 0
        self.root.config(bg = f"{color[self.i]}")
        self.i += 1
        self.root.after(500, self.Changebg)

if __name__ == '__main__':
    root = Tk()
    cal = calWindow(root)
    root.mainloop()