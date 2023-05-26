import os
import tkinter.ttk
from tkinter import *
import tkinter.messagebox as tmsg
import cx_Oracle
import ctypes


class Setting:
    def __init__(self, root):
        self.root = root
        self.root.title("Setting")
        self.root.geometry("980x440+365+235")
        self.root.minsize(980, 440)
        self.root.maxsize(980, 440)
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default='media/logo.ico')
        self.i = 0
        self.frame1 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame1.place(x=5, y=5, width=970, height=45)
        self.text = Label(self.frame1, text="Settings", fg = "Yellow", font="Courier 18 bold underline")
        self.text.pack()
        self.Changebg()

        ########################################################

        self.frame2 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame2.place(x=5, y=60, width=340, height=320)
        self.Make = StringVar()
        self.Model = StringVar()
        Label(self.frame2, text = "ADD OR UPDATE", font = "Conicsansms 12 bold underline", bg = 'Cyan', fg = 'Blue').place(x = 100, y = 10)
        Label(self.frame2, text = "Make", font = "Conicsansms 12 bold", bg = 'Cyan', fg = 'Blue').place(x = 5, y = 60)
        Label(self.frame2, text = "Model", font = "Conicsansms 12 bold", bg = 'Cyan', fg = 'Blue').place(x = 5, y = 120)
        self.MakeE = Entry(self.frame2, textvariable = self.Make, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 60, width = 170)
        self.ModelE = Entry(self.frame2, textvariable = self.Model, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 120, width = 170)
        Button(self.frame2, text = 'Delete Make', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.DeleteMake).place(x = 5, y = 200, width = 325)
        Button(self.frame2, text = 'Delete Model', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.DeleteModel).place(x = 5, y = 250, width = 325)


        ########################################################

        self.frame3 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame3.place(x=350, y=60, width=625, height=375)
        Label(self.frame3, text="Search By", fg="Blue", bg="Cyan", font="Conicsansms 16 bold").place(x=5, y=7)
        self.searchby = StringVar()
        self.searchE = StringVar()
        self.searchby = tkinter.ttk.Combobox(self.frame3, textvariable=self.searchby, font="Conicsansms 10 bold")
        self.searchby['values'] = ['Model', 'Make']
        self.searchby.place(x=130, y=10, width=110)
        Entry(self.frame3, font="Conicsansms 10 bold", fg="Blue", textvariable = self.searchE).place(x=250, y=10, width=130)
        Button(self.frame3, text="Search", font="Conicsansms 12 bold", fg="Cyan", bg="Blue", cursor="hand2", bd=5, relief=SUNKEN).place(x=390, y=9, width=100, height=25)
        Button(self.frame3, text="Show All", font="Conicsansms 12 bold", fg="Cyan", bg="Blue", cursor="hand2", bd=5, relief=SUNKEN).place(x=500, y=9, width=100, height=25)
        scrollX = Scrollbar(self.frame3, orient=HORIZONTAL)
        scrollX.place(x=5, y=345, width=250)
        scroll1X = Scrollbar(self.frame3, orient=HORIZONTAL)
        scroll1X.place(x=330, y=345, width=250)
        scrollY = Scrollbar(self.frame3, orient=VERTICAL)
        scrollY.place(x=260, y=50, height=295)
        scroll1Y = Scrollbar(self.frame3, orient=VERTICAL)
        scroll1Y.place(x=585, y=50, height=295)
        self.Tree1 = tkinter.ttk.Treeview(self.frame3, xscrollcommand=scrollX.set, yscrollcommand=scrollY.set, column=('Make'))
        self.Tree1.heading('Make', text='Make')
        self.Tree1['show'] = ['headings']
        self.Tree1.column('Make', width=50)
        self.Tree1.place(x=5, y=50, width=250, height=290)
        self.Tree1.bind("<Double-Button-1>", self.get_Cursor)
        self.Tree2 = tkinter.ttk.Treeview(self.frame3, xscrollcommand=scroll1X.set, yscrollcommand=scroll1Y.set, column=('Model'))
        self.Tree2.heading('Model', text='Model')
        self.Tree2['show'] = ['headings']
        self.Tree2.column('Model', width=50)
        self.Tree2.place(x=330, y=50, width=250, height=290)
        self.Tree2.bind("<Double-Button-1>", self.get_Cursor1)
        scrollX.config(command=self.Tree1.xview)
        scroll1X.config(command=self.Tree2.xview)
        scrollY.config(command=self.Tree1.yview)
        scroll1Y.config(command=self.Tree2.yview)


        ########################################################

        self.frame4 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame4.place(x=5, y=385, width=340, height=50)
        Button(self.frame4, text='Add Make', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor="hand2", bd=5, relief=SUNKEN, command=self.AddMake).grid(row=0, column=0, padx=40, pady=5)
        Button(self.frame4, text='Add Model', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor="hand2", bd=5, relief=SUNKEN, command=self.AddModel).grid(row=0, column=1, padx=40, pady=5)
        self.Fetch()

    def Changebg(self):
        colors = ['red', 'green', 'Hot Pink', 'black', 'purple', 'Maroon']
        color = ['grey', 'pink', 'cyan', 'magenta']
        # color = ['Maroon', 'red', 'green', 'Hot Pink', 'black', 'purple']
        colors = ['#314af7', '#f94b4b']
        color = ['#f94b4b', '#314af7']
        if self.i >= len(colors) or self.i >= len(color):
            self.i = 0
        self.frame1.config(bg = f"{colors[self.i]}")
        self.text.config(bg = f"{colors[self.i]}")
        self.root.config(bg = f"{color[self.i]}")
        self.i += 1
        self.frame1.after(500, self.Changebg)

    def getConnection(self):
        connection = cx_Oracle.connect('system/69-Gilani-53@localhost:1521/orcl')
        return connection

    def AddMake(self):
        try:
            if self.Make.get() and self.Make.get() != 'None':
                mk = self.Make.get()
                connection = self.getConnection()
                cursor = connection.cursor()
                query = f"INSERT INTO MAKEE (MAKE) VALUES ('{mk}')"
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
            else:
                tmsg.showerror("Error", "Enter Some Value Of Make")
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")

    def UpdateMake(self):
        try:
            if self.Make.get() and self.Make.get() != 'None':
                mk = self.Make.get()
                connection = self.getConnection()
                cursor = connection.cursor()
                query = f"UPDATE MAKEE SET MAKE =  ('{mk}') WHERE MAKE = '{self.Make.get()}'"
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
            else:
                tmsg.showerror("Error", "Enter Some Value Of Make")
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")


    def AddModel(self):
        try:
            if self.Model.get() and self.Model.get() != 'None':
                mk = self.Model.get()
                connection = self.getConnection()
                cursor = connection.cursor()
                query = f"INSERT INTO MODELL (MODEL) VALUES ('{mk}')"
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
            else:
                tmsg.showerror("Error", "Enter Value Of Model")
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")


    def UpdateModel(self):
        try:
            if self.Model.get() and self.Model.get() != 'None':
                md = self.Model.get()
                connection = self.getConnection()
                cursor = connection.cursor()
                query = f"UPDATE MAKEE SET MAKE =  ('{md}') WHERE MAKE = '{self.Model.get()}'"
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
            else:
                tmsg.showerror("Error", "Enter Some Value Of Make")
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")


    def DeleteMake(self):
        try:
            focus = self.Tree1.focus()
            items = self.Tree1.item(focus)
            rows = items['values']
            a = tmsg.askquestion("Warning", "Would you like to delete permenantly?")
            if a == 'yes':
                mk = self.Make.get()
                connection = self.getConnection()
                cursor = connection.cursor()
                query = f"DELETE FROM MAKEE WHERE MAKE = '{rows[0]}'"
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
        except:
            pass

    def DeleteModel(self):
        try:
            focus = self.Tree2.focus()
            items = self.Tree2.item(focus)
            rows = items['values']
            a = tmsg.askquestion("Warning", "Would you like to delete permenantly?")
            if a == 'yes':
                mk = self.Model.get()
                connection = self.getConnection()
                cursor = connection.cursor()
                query = f"DELETE FROM MODELL WHERE MODEL = '{mk}'"
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
        except:
            pass

    def get_Cursor(self, event):
        try:
            cursor = self.Tree1.focus()
            items = self.Tree1.item(cursor)
            row = items['values']
            self.Make.set(row[0])
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")
            pass

    def get_Cursor1(self, event):
        try:
            cursor = self.Tree2.focus()
            items = self.Tree2.item(cursor)
            row = items['values']
            self.Model.set(row[0])
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")
            pass

    def Fetch(self):
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor1 = connection.cursor()
        query = "SELECT * FROM MAKEE"
        query1 = "SELECT * FROM MODELL"
        cursor.execute(query)
        cursor1.execute(query1)
        rows = cursor.fetchall()
        rows1 = cursor1.fetchall()
        if len(rows) != 0:
            self.Tree1.delete(*self.Tree1.get_children())
            for row in rows:
                self.Tree1.insert('', END, values=row)
            connection.commit()
        if len(rows1) != 0:
            self.Tree2.delete(*self.Tree2.get_children())
            for row2 in rows1:
                self.Tree2.insert('', END, values=row2)
            connection.commit()
        connection.close()

if __name__ == "__main__":
    root = Tk()
    setting = Setting(root)
    root.mainloop()