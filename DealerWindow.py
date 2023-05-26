from tkinter import *
import tkinter.ttk
import cx_Oracle
import tkinter.messagebox as tmsg
import ctypes
from tkcalendar import Calendar
class Dealer:
    def __init__(self, root):
        self.root = root
        self.root.title("Dealer Expenses")
        self.root.geometry("980x440+365+235")
        self.root.config(bg = "Hot Pink")
        self.root.minsize(980, 440)
        self.root.maxsize(980, 440)
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default='media/logo.ico')
        self.count = 0

        ##############################################################

        self.frame1 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame1.place(x=5, y=5, width=970, height=45)
        self.text = Label(self.frame1, text="Dealer Expenses", bg="Cyan", font="Courier 18 bold underline")
        self.ColorChange()
        self.text.pack()

        ##############################################################

        self.frame2 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame2.place(x=5, y=57, width=340, height=320)
        self.DealerID = StringVar()
        self.ExpenseDate = StringVar()
        self.ExpenseType = StringVar()
        self.Amount = StringVar()
        self.Amount.set('$000,00')
        self.PaymentType = StringVar()
        self.Remark = StringVar()
        Label(self.frame2, bg = "Cyan").pack(pady = 5)
        Label(self.frame2, text = "Dealer Id", font = "Conicsansms 12 bold", fg = "Blue", bg = "Cyan").pack(padx = 5, pady = 10, anchor = NW)
        Label(self.frame2, text = "Expense Date", font = "Conicsansms 12 bold", fg = "Blue", bg = "Cyan").pack(padx = 5, pady = 10, anchor = NW)
        Label(self.frame2, text = "Expense Type", font = "Conicsansms 12 bold", fg = "Blue", bg = "Cyan").pack(padx = 5, pady = 10, anchor = NW)
        Label(self.frame2, text = "Amount", font = "Conicsansms 12 bold", fg = "Blue", bg = "Cyan").pack(padx = 5, pady = 10, anchor = NW)
        Label(self.frame2, text = "Payment Type", font = "Conicsansms 12 bold", fg = "Blue", bg = "Cyan").pack(padx = 5, pady = 10, anchor = NW)
        Label(self.frame2, text = "Remark", font = "Conicsansms 12 bold", fg = "Blue", bg = "Cyan").pack(padx = 5, pady = 10, anchor = NW)

        self.DealerIDE = Entry(self.frame2, textvariable=self.DealerID, font="Conicsansms 10 bold", fg="Blue").place(x=130, y=45, width=190)
        self.ExpenseDateE = Entry(self.frame2, textvariable=self.ExpenseDate, font="Conicsansms 10 bold", fg="Blue").place(x=130, y=90, width=190)
        Button(self.frame2, text="Cal", font="Conicsansms 10 bold", fg="Blue", command=self.getPDate).place(x=288, y=90, height=20)
        self.ExpenseTypeE = tkinter.ttk.Combobox(self.frame2, textvariable=self.ExpenseType, font="Conicsansms 10 bold")
        self.ExpenseTypeE['values'] = ["Electricity Bill", "Rent", "Milage", "Other"]
        self.ExpenseTypeE.place(x=130, y=135, width=190)
        self.AmountE = Entry(self.frame2, textvariable=self.Amount, font="Conicsansms 10 bold", fg="Blue").place(x=130, y=180, width=190)
        self.PaymentTypeE = tkinter.ttk.Combobox(self.frame2, textvariable=self.PaymentType, font="Conicsansms 10 bold")
        self.PaymentTypeE['values'] = ["Cash", "Visa", "Check"]
        self.PaymentTypeE.place(x=130, y=225, width=190)
        self.RemarkE = Entry(self.frame2, textvariable=self.Remark, font="Conicsansms 10 bold", fg="Blue").place(x=130, y=270, width=190)

        ##############################################################

        self.frame3 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame3.place(x=350, y=57, width=625, height=378)
        Label(self.frame3, text="Search By", fg="Blue", bg="Cyan", font="Conicsansms 16 bold").place(x=5, y=7)
        self.searchby = StringVar()
        self.searchE = StringVar()
        self.searchby = tkinter.ttk.Combobox(self.frame3, textvariable=self.searchby, font="Conicsansms 10 bold")
        self.searchby['values'] = ['DealerID']
        self.searchby.place(x=130, y=10, width=110)
        self.search = Entry(self.frame3, font="Conicsansms 10 bold", fg="Blue", textvariable = self.searchE)
        self.search.place(x=250, y=10, width=130)
        Button(self.frame3, text="Search", font="Conicsansms 12 bold", fg="Cyan", bg="Blue", cursor = "hand2", bd=5, relief=SUNKEN, command = self.Search).place(x=390, y=9, width=100, height=25)
        Button(self.frame3, text="Show All", font="Conicsansms 12 bold", fg="Cyan", bg="Blue", cursor = "hand2", bd=5, relief=SUNKEN, command = self.Fetch).place(x=500, y=9, width=100, height=25)
        scrollX = Scrollbar(self.frame3, orient=HORIZONTAL)
        scrollX.place(x=5, y=345, width=580)
        scrollY = Scrollbar(self.frame3, orient=VERTICAL)
        scrollY.place(x=590, y=50, height=300)
        self.Tree = tkinter.ttk.Treeview(self.frame3, xscrollcommand=scrollX.set, yscrollcommand=scrollY.set, column=('Dealer ID', 'Expense Date', 'Expense Type', 'Amount', 'Payment Type', 'Remark'))
        self.Tree.heading('Dealer ID', text='Dealer ID')
        self.Tree.heading('Expense Date', text='Expense Date')
        self.Tree.heading('Expense Type', text='Expense Type')
        self.Tree.heading('Amount', text='Amount')
        self.Tree.heading('Payment Type', text='Payment Type')
        self.Tree.heading('Remark', text='Remark')
        self.Tree['show'] = ['headings']
        self.Tree.column('Dealer ID', width=50)
        self.Tree.column('Expense Date', width=50)
        self.Tree.column('Expense Type', width=50)
        self.Tree.column('Amount', width=50)
        self.Tree.column('Payment Type', width=50)
        self.Tree.column('Remark', width=50)
        self.Tree.place(x=5, y=50, width=580, height=290)
        scrollX.config(command=self.Tree.xview)
        scrollY.config(command=self.Tree.yview)

        ##############################################################

        self.frame4 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame4.place(x=5, y=385, width=340, height=50)
        Button(self.frame4, text='Add', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, width=5, command = self.insert).grid(row=0, column=0, padx=5, pady=5)
        Button(self.frame4, text='Update', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, command = self.Update).grid(row=0, column=1, padx=5, pady=5)
        Button(self.frame4, text='Delete', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, command = self.Delete).grid(row=0, column=2, padx=5, pady=5)
        Button(self.frame4, text='Clear', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, command = self.Clear).grid(row=0, column=3, padx=5, pady=5)
        Button(self.frame4, text='Exit', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, width=5,command=self.root.destroy).grid(row=0, column=4, padx=5, pady=5)
        self.Tree.bind("<Double-Button-1>", self.get_Cursor)
        self.Fetch()

    def ExtractEntry(self, event):
        self.ExpenseDate.set(self.cal.get_date())
        self.cal.destroy()

    def getPDate(self):
        self.cal = Calendar(self.frame2, selectmode='day', year=2020, month=5, day=22)
        self.cal.place(x=80, y=10)
        self.root.bind("<Return>", self.ExtractEntry)

    def ColorChange(self):
        colors = ['Red', 'Blue', 'Purple', 'Orange', 'Green', 'Maroon']
        if self.count >= len(colors):
            self.count = 0
        self.text.config(fg = f"{colors[self.count]}")
        self.count += 1
        self.text.after(500, self.ColorChange)

    def getConnection(self):
        connect = cx_Oracle.connect('system/69-Gilani-53@localhost:1521/orcl')
        return connect

    def insert(self):
        try:
            am = self.Amount.get()
            am = str(am)
            a1 = am.split(',')[0]
            b1 = am.split(',')[1]
            if len(b1) > 2:
                b1 = b1[0:2]
            am = f"{a1},{b1}"
            did = self.DealerID.get()
            ed = self.ExpenseDate.get()
            et = self.ExpenseType.get().upper()
            # am = self.Amount.get()
            pt = self.PaymentType.get().upper()
            rmk = self.Remark.get().upper()
            connection = self.getConnection()
            cursor = connection.cursor()
            query = f"INSERT INTO DEALER (DEALERID, EXPENSEDATE, EXPENSETYPE, AMOUNT, PAYMENTTYPE, REMARK) VALUES ('{did}', TO_DATE('{ed}', 'MM/DD/YY'), '{et}','{am}', '{pt}', '{rmk}')"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            self.Fetch()
            self.Clear()
        except Exception as e:
            tmsg.showerror("Invalid Entities", f"Check Dealer ID Or Error Due To {e}")

    def Clear(self):
        self.DealerID.set("")
        self.ExpenseType.set("")
        self.ExpenseDate.set("")
        self.Amount.set("")
        self.PaymentType.set("")
        self.Remark.set("")
        self.searchby.set("")
        self.searchE.set("")

    def Fetch(self):
        connection = self.getConnection()
        cursor = connection.cursor()
        query = "SELECT DEALERID, TO_CHAR(EXPENSEDATE, 'MM/DD/YY') AS EXPENSEDATE, EXPENSETYPE, AMOUNT, PAYMENTTYPE, REMARK FROM DEALER ORDER BY DEALERID ASC"
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
                query = f"DELETE FROM DEALER WHERE DEALERID = '{rows[0]}'"
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
                self.Clear()
        except:
            tmsg.showerror("Deletion Error", "No Dealer ID Is Selected In The Field")

    def Update(self):
        try:
            did = self.DealerID.get()
            ed = self.ExpenseDate.get()
            et = self.ExpenseType.get().upper()
            am = self.Amount.get()
            pt = self.PaymentType.get().upper()
            rmk = self.Remark.get().upper()
            connection = self.getConnection()
            query = f"UPDATE DEALER SET EXPENSEDATE = TO_DATE('{ed}', 'MM/DD/YY'), EXPENSETYPE = '{et}', AMOUNT = '{am}', PAYMENTTYPE = '{pt}', REMARK = '{rmk}' WHERE DEALERID = '{did}'"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.Fetch()
            self.Clear()
            tmsg.showinfo("Updated", "Dealer Detail Updated Successfully")
        except Exception as e:
            tmsg.showerror("Update Error", "No Dealer ID Is Selected In The Field For Updating")

    def Search(self):
        try:
            connection = self.getConnection()
            query = "SELECT * FROM DEALER WHERE " + str(self.searchby.get()) + " = '" + str(self.searchE.get()).upper() + "'"
            if self.searchby.get().upper() == 'EXPENSEDATE':
                query = f"SELECT DEALERID, TO_CHAR(EXPENSEDATE, 'MM/DD/YY') AS EXPENSEDATE, EXPENSETYPE, AMOUNT, PAYMENTTYPE, REMARK FROM DEALER WHERE {self.searchby.get().upper()} = TO_DATE('{self.search.get()}', 'DD-MM-YYYY')"
            else:
                query = f"SELECT DEALERID, TO_CHAR(EXPENSEDATE, 'MM/DD/YY') AS EXPENSEDATE, EXPENSETYPE, AMOUNT, PAYMENTTYPE, REMARK FROM DEALER WHERE {self.searchby.get().upper()} = '{self.search.get().upper()}'"
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

    def get_Cursor(self, event):
        try:
            cursor = self.Tree.focus()
            items = self.Tree.item(cursor)
            row = items['values']
            self.DealerID.set(row[0])
            self.ExpenseDate.set(row[1])
            self.ExpenseType.set(row[2])
            self.Amount.set(row[3])
            self.PaymentType.set(row[4])
            self.Remark.set(row[5])
        except Exception as e:
            pass



if __name__ == "__main__":
    root = Tk()
    dealer = Dealer(root)
    root.mainloop()