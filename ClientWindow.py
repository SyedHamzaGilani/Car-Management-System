import tkinter.ttk
from tkinter import *
import tkinter.messagebox as tmsg
import cx_Oracle
import ctypes

class Client:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Information")
        # self.Theme()
        self.count = 0
        self.words = ""
        self.c = 0
        self.bg = 0
        self.Changebg()
        # self.Theme()
        self.root.geometry("980x440+365+235")
        self.root.minsize(980, 440)
        self.root.maxsize(980, 440)
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default='media/logo.ico')


        ##############################################################

        self.frame1 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame1.place(x=5, y=5, width=970, height=45)
        self.text = Label(self.frame1, font="Courier 18 bold underline", bg="Cyan")
        self.MovingText()
        self.text.pack()

        ##############################################################

        self.frame2 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame2.place(x = 5, y = 60, width = 340, height = 320)
        Label(self.frame2, text = "ID Number", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        Label(self.frame2, text = "First Name", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        Label(self.frame2, text = "Last Name", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        Label(self.frame2, text = "City", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        Label(self.frame2, text = "State", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        Label(self.frame2, text = "Zip Code", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        Label(self.frame2, text = "Phone Number", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        Label(self.frame2, text = "Address", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 5, anchor = NW)
        self.IdNumber = StringVar()
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.City = StringVar()
        self.State = StringVar()
        self.ZipCode = StringVar()
        self.PhoneNumber = StringVar()
        self.address = StringVar()
        self.IdNumberE = Entry(self.frame2, textvariable = self.IdNumber, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 5, width = 190)
        self.FirstNameE = Entry(self.frame2, textvariable = self.FirstName, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 40, width = 190)
        self.LastNameE = Entry(self.frame2, textvariable = self.LastName, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 75, width = 190)
        self.CityE = Entry(self.frame2, textvariable = self.City, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 110, width = 190)
        self.StateE = Entry(self.frame2, textvariable = self.State, font = "Conicsansms 10 bold", fg = "Blue")
        self.StateE.place(x = 130, y = 145, width = 190)
        self.ZipCodeE = Entry(self.frame2, textvariable = self.ZipCode, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 180, width = 190)
        self.PhoneNumberE = Entry(self.frame2, textvariable = self.PhoneNumber, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 215, width = 190)
        self.AscrollY = Scrollbar(self.frame2)
        self.AscrollY.place(x = 315, y = 250)
        self.AscrollX = Scrollbar(self.frame2, orient = HORIZONTAL)
        self.AscrollX.place(x = 130, y = 295, width = 180)
        self.address = Text(self.frame2, font = "Conicsansms 10 bold", fg = "Blue", xscrollcommand = self.AscrollX.set, yscrollcommand = self.AscrollY.set, wrap = NONE)
        self.AscrollX.config(command = self.address.xview)
        self.AscrollY.config(command = self.address.yview)
        self.address.place(x = 130, y = 250, width = 180, height = 40)

        ##############################################################

        self.frame3 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame3.place(x = 5, y = 385, width = 340, height = 50)
        Button(self.frame3, text = 'Add', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, width = 5, command = self.insert).grid(row = 0, column = 0, padx = 5, pady = 5)
        Button(self.frame3, text = 'Update', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Update).grid(row = 0, column = 1, padx = 5, pady = 5)
        Button(self.frame3, text = 'Delete', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Delete).grid(row = 0, column = 2, padx = 5, pady = 5)
        Button(self.frame3, text = 'Clear', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Clear).grid(row = 0, column = 3, padx = 5, pady = 5)
        Button(self.frame3, text = 'Exit', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, width = 5, command = self.root.destroy).grid(row = 0, column = 4, padx = 5, pady = 5)

        ##############################################################

        self.frame4 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame4.place(x = 355, y = 60, width = 620, height = 375)
        Label(self.frame4, text = "Search By", font = "Conicsansms 12 bold", bg = 'Cyan', fg = "Blue").place(x = 5, y = 9)
        self.searchby = StringVar()
        self.search = StringVar()
        self.searchby = tkinter.ttk.Combobox(self.frame4, textvariable = self.searchby, font = "Conicsansms 10 bold")
        self.searchby['values'] = ['IdNumber', 'FirstName', 'LastName']
        self.searchby.place(x = 100, y = 10, width = 130)
        self.searchE = Entry(self.frame4, textvariable = self.search, font = "Conicsansms 10 bold", fg = "Blue")
        self.searchE.place(x = 240, y = 10, width = 140)
        Button(self.frame4, text = "Search", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Search).place(x = 390, y = 9, width = 100, height = 25)
        Button(self.frame4, text = "Show All", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Fetch).place(x = 500, y = 9, width = 100, height = 25)
        scrollX = Scrollbar(self.frame4, orient = HORIZONTAL)
        scrollX.place(x = 5, y = 345, width = 580)
        scrollY = Scrollbar(self.frame4, orient = VERTICAL)
        scrollY.place(x = 590, y = 50, height = 300)
        self.Tree = tkinter.ttk.Treeview(self.frame4, xscrollcommand = scrollX.set, yscrollcommand = scrollY.set, column = ('ID Number', 'First Name', 'Last Name', 'City', 'State', 'Zip Code', 'PhoneNumber', 'Address'))
        self.Tree.heading('ID Number', text = 'ID Number')
        self.Tree.heading('First Name', text = 'First Name')
        self.Tree.heading('Last Name', text = 'Last Name')
        self.Tree.heading('City', text = 'City')
        self.Tree.heading('State', text = 'State')
        self.Tree.heading('Zip Code', text = 'Zip Code')
        self.Tree.heading('PhoneNumber', text = 'PhoneNumber')
        self.Tree.heading('Address', text = 'Address')
        self.Tree['show'] = ['headings']
        self.Tree.column('ID Number', width = 100)
        self.Tree.column('First Name', width = 80)
        self.Tree.column('Last Name', width = 80)
        self.Tree.column('City', width = 80)
        self.Tree.column('State', width = 50)
        self.Tree.column('Zip Code', width = 80)
        self.Tree.column('PhoneNumber', width = 100)
        self.Tree.column('Address', width = 150)
        self.Tree.place(x = 5, y = 50, width = 580, height = 290)
        scrollX.config(command = self.Tree.xview)
        scrollY.config(command = self.Tree.yview)
        self.Tree.bind("<Double-Button-1>", self.get_Cursor)
        self.Fetch()



        ##################################

    def MovingText(self):
        a = "Add Client Information Here"
        if self.count >= len(a):
            self.count = 0
            self.words = ""
        self.words += a[self.count]
        self.count += 1
        colors = ['Red', 'Blue', 'Purple', 'Orange', 'Green', 'Maroon']
        if self.c >= len(colors):
            self.c = 0
        self.text.config(text = self.words, fg = f"{colors[self.c]}")
        self.c += 1
        self.text.after(200, self.MovingText)

    def Changebg(self):
        colors = ['Red', 'Blue', 'Purple', 'Orange', 'Green', 'Maroon']
        if self.bg >= len(colors):
            self.bg = 0
        self.root.config(bg = f"{colors[self.bg]}")
        self.bg += 1
        self.root.after(5000, self.Changebg)

    def Theme(self):
        combostyle = tkinter.ttk.Style()
        combostyle.theme_create('custom_style',
                                parent = 'alt',
                                settings= {
                                    'TCombobox':
                                        {
                                            'configure':
                                                {
                                                    'selectforeground':'Blue',
                                                    'selectbackground':'White',
                                                    'fieldforeground':'Blue',
                                                    'fieldbackground':'White',
                                                    'background':'Red'
                                                }
                                        }
                                })
        combostyle.theme_use('custom_style')
        self.root.option_add('*TCombobox*Listbox*Background', 'White')
        self.root.option_add('*TCombobox*Listbox*Foreground', 'Blue')

    ################################        BACK END PROGRAMMING        #############################

    def getConnection(self):
        connect = cx_Oracle.connect('system/69-Gilani-53@localhost:1521/orcl')
        return connect

    def insert(self):
        try:
            IdNumber = self.IdNumber.get()
            FirstName = (self.FirstName.get()).upper()
            LastName = (self.LastName.get()).upper()
            City = (self.City.get()).upper()
            State = (self.State.get()).upper()
            ZipCode = self.ZipCode.get()
            PhoneNumber = self.PhoneNumber.get()
            address = self.address.get("1.0", END)
            connection = self.getConnection()
            cursor = connection.cursor()
            # query = f"INSERT INTO CUSTOMER VALUES ({ref}, '{LastName}', '{City}', '{State}', '{ZipCode}', '{PhoneNumber}', '{idproof}', '{idnumber}', '{address}')"
            query = f"INSERT INTO CLIENT (IDNUMBER, FIRSTNAME, LASTNAME, CITY, STATE, ZIPCODE, PHONENO, ADDRESS) VALUES ('{IdNumber}','{FirstName}', '{LastName}', '{City}', '{State}', '{ZipCode}', '{PhoneNumber}', '{address}')"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            self.Fetch()
            self.Clear()
        except Exception as e:
            tmsg.showerror("Invalid Entities", f"Check ID Number Or Error Due To {e}")

    def get_Cursor(self, event):
        try:
            cursor = self.Tree.focus()
            items = self.Tree.item(cursor)
            row = items['values']
            self.IdNumber.set(row[0])
            self.FirstName.set(row[1])
            self.LastName.set(row[2])
            self.City.set(row[3])
            self.State.set(row[4])
            self.ZipCode.set(row[5])
            self.PhoneNumber.set(row[6])
            self.address.delete(1.0, END)
            self.address.insert(END, row[7])
        except Exception as e:
            pass

    def Fetch(self):
        connection = self.getConnection()
        cursor = connection.cursor()
        query = "SELECT * FROM CLIENT ORDER BY IDNUMBER ASC"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.Tree.delete(*self.Tree.get_children())
            for row in rows:
                self.Tree.insert('', END, values=row)
            connection.commit()
        connection.close()

    def Delete(self):
        connection = self.getConnection()
        try:
            focus = self.Tree.focus()
            items = self.Tree.item(focus)
            rows = items['values']
            a = tmsg.askquestion("Warning", "Would you like to delete permenantly?")
            if a == "yes":
                # query = f"DELETE FROM CUSTOMER WHERE REF_NO = {rows[0]}"
                query = f"DELETE FROM CLIENT WHERE IDNUMBER = '{rows[0]}'"
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
                self.Clear()
        except:
            tmsg.showerror("Deletion Error", "No Client Is Selected In The Field")

    def Clear(self):
        self.IdNumber.set("")
        self.FirstName.set("")
        self.LastName.set("")
        self.City.set("")
        self.State.set("")
        self.ZipCode.set("")
        self.PhoneNumber.set("")
        self.address.delete(1.0, END)
        self.searchby.set("")
        self.search.set("")
        self.Fetch()

    def Update(self):
        try:
            connection = self.getConnection()
            query = f"UPDATE CLIENT SET FIRSTNAME = '{self.FirstName.get().upper()}', LASTNAME = '{self.LastName.get().upper()}', CITY = '{self.City.get().upper()}', STATE = '{self.State.get().upper()}', ZIPCODE = '{self.ZipCode.get()}', PHONENO = '{self.PhoneNumber.get()}', ADDRESS = '{self.address.get(1.0, END).upper()}' WHERE IDNUMBER = '{self.IdNumber.get()}'"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.Fetch()
            self.Clear()
            tmsg.showinfo("Updated", "Client Updated Successfully")
        except Exception as e:
            tmsg.showerror("Update Error", f"No Client Is Selected In The Field For Updating Or Error Due To {e}")

    def Search(self):
        try:
            connection = self.getConnection()
            query = "SELECT * FROM CLIENT WHERE " + str(self.searchby.get()) + " = '" + str(self.search.get()).upper() + "'"
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            self.Tree.delete(*self.Tree.get_children())
            if len(rows) != 0:
                for row in rows:
                    self.Tree.insert("", END, values=row)
                connection.commit()
            cursor.close()
        except Exception as e:
            tmsg.showerror("Search Error", "Search Field Is Empty, Please Fill The Search Entry")


if __name__ == "__main__":
    root = Tk()
    customer = Client(root)
    root.mainloop()