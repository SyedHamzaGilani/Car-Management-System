from tkinter import *
import cx_Oracle
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import ctypes
class Account:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500+400+100")
        self.root.resizable(False, False)
        self.c = 0
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default='media/logo.ico')
        img1 = Image.open("Images/Dealership.jpg")
        img1 = img1.resize((500, 500), Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        img1 = Label(self.root, image = self.img1)
        img1.place(x = 0, y = 0)
        frame = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        frame.place(x = 50, y = 50, width = 400, height = 400)
        self.createUser = StringVar()
        self.oldPass = StringVar()
        self.newPass = StringVar()
        self.label = Label(frame, text = "Create Login Details", font = "Courier 20 bold underline", bg = "Cyan")
        self.MovingText()
        self.label.place(x = 40, y = 10)
        Label(frame, text = "User Name", font = "Arial 13 bold", bg = "Cyan", fg = "Blue").place(x = 20, y = 90)
        Entry(frame, textvariable = self.createUser,font = "Arial 12 bold", fg = "Red").place(x = 160, y = 90)
        Label(frame, text = "Old Password", font = "Arial 13 bold", bg = "Cyan", fg = "Blue").place(x = 20, y = 160)
        Entry(frame, textvariable=self.oldPass, font="Arial 12 bold", fg="Red").place(x=160, y=160)
        Label(frame, text = "New Password", font = "Arial 13 bold", bg = "Cyan", fg = "Blue").place(x = 20, y = 230)
        Entry(frame, textvariable=self.newPass, font="Arial 12 bold", fg="Red").place(x=160, y=230)
        Button(frame, text = "Exit", font = "Courier 14 bold", bg = "Maroon", fg = "Cyan", cursor = "hand2", command = self.root.destroy).place(x = 50, y = 320, width = 95)
        Button(frame, text = "Clear", font = "Courier 14 bold", bg = "Green", fg = "Cyan", cursor = "hand2", command = self.Clear).place(x = 150, y = 320, width = 95)
        Button(frame, text = "Reset Now", font = "Courier 14 bold", bg = "Blue", fg = "Cyan", cursor = "hand2", command = self.new).place(x = 250, y = 320)

    def MovingText(self):
        colors = ['Red', 'Blue', 'Purple', 'Orange', 'Green', 'Maroon']
        if self.c >= len(colors):
            self.c = 0
        self.label.config(fg = f"{colors[self.c]}")
        self.c += 1
        self.label.after(500, self.MovingText)

    def Clear(self):
        self.createUser.set("")
        self.oldPass.set("")
        self.newPass.set("")

    def new(self):
        self.Fetch()
        # self.newAccount(self.createUser.get(), self.newPass.get())

    def Connection(self):
        connection = cx_Oracle.connect("system/Reem2009!@localhost:1521/orcl")
        return connection

    def Fetch(self):
        try:
            connection = self.Connection()
            cursor = connection.cursor()
            query = "SELECT * FROM LOGIN"
            cursor.execute(query)
            rows = cursor.fetchone()
            a = str(self.createUser.get().upper())
            b = str(self.oldPass.get())
            try:
                if a == rows[0] and b == rows[1]:
                    self.newAccount(self.createUser.get().upper(), self.newPass.get())
                    tmsg.showinfo("Successful", "Password Updated Successfully!")
                    self.root.destroy()
                else:
                    tmsg.showerror("Error", "Operation Denied!, Error In Username Or Old Password")
                    self.root.destroy()
            except Exception as er:
                tmsg.showerror("Error", f"Error due to {er}")
            connection.commit()
            cursor.close()
        except Exception as er:
            tmsg.showerror("Error", f"Error due to {er}")

    def newAccount(self, user, passw):
        connection = self.Connection()
        cursor = connection.cursor()
        query = f"UPDATE LOGIN SET PASSWORD = '{passw}' WHERE USERNAME = '{user}'"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        self.Clear()


if __name__ == "__main__":
    root = Tk()
    account = Account(root)
    root.mainloop()
