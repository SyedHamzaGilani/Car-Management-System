import tkinter.ttk
from tkinter import *
import cx_Oracle
import tkinter.messagebox as tmsg
import os
import ctypes
import tkcalendar


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Report")
        self.root.geometry("980x440+365+235")
        self.root.minsize(980, 440)
        self.root.maxsize(980, 440)
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default='media/logo.ico')
        self.i = 0
        self.frame1 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame1.place(x=5, y=5, width=970, height=45)
        self.text = Label(self.frame1, text="Sale And Purchase Report", fg = "Yellow", font="Courier 18 bold underline")
        self.text.pack()
        self.Changebg()
        self.frame2 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame2.place(x=5, y=57, width=970, height=200)
        Label(self.frame2, bg='Cyan').pack(pady=1)
        Label(self.frame2, text="Date From", font="Conicsansms 12 bold", fg="Blue", bg="Cyan").pack(padx= 230, pady=15, anchor=NW)
        Label(self.frame2, text="Date To", font="Conicsansms 12 bold", fg="Blue", bg="Cyan").pack(padx= 230, pady=15, anchor=NW)
        self.DateFrom = StringVar()
        self.DateFrom.set('5/28/22')
        self.DateTo = StringVar()
        self.DateTo.set('5/28/22')
        self.DateFromE = Entry(self.frame2, textvariable=self.DateFrom, font="Conicsansms 10 bold", fg="Blue").place(x=350, y=40, width=390)
        Button(self.frame2, text="Cal", font="Conicsansms 10 bold", fg="Cyan", bg = "Blue", command=self.getFDate).place(x=640, y=40, height=20, width = 100)
        self.DateToE = Entry(self.frame2, textvariable=self.DateTo, font="Conicsansms 10 bold", fg="Blue").place(x=350, y=95, width=390)
        Button(self.frame2, text="Cal", font="Conicsansms 10 bold", fg="Cyan", bg = "Blue", command=self.getTDate).place(x=640, y=95, height=20, width = 100)

        self.frame3 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        self.frame3.place(x=5, y=270, width=970, height=150)
        Button(self.frame3, text='Print (Purchase)', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, width=5, command = self.Purchase).place(x = 100, y = 60, width = 200)
        Button(self.frame3, text='Print (Sale)', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, width=5, command = self.Sale).place(x = 400, y = 60, width = 200)
        Button(self.frame3, text='Clear', font='Conicsansms 10 bold', fg='Cyan', bg='Blue', cursor = "hand2", bd=5, relief=SUNKEN, width=5, command = self.Clear).place(x = 700, y = 60, width = 200)

    def ExtractFEntry(self, event):
        self.DateFrom.set(self.calF.get_date())
        self.calF.destroy()

    def getFDate(self):
        try:
            self.calT.destroy()
        except:
            pass
        try:
            self.calF.destroy()
        except:
            pass
        self.calF = tkcalendar.Calendar(self.frame2, selectmode='day', year=2020, month=5, day=22)
        self.calF.place(x=400, y=10)
        self.root.bind("<Return>", self.ExtractFEntry)

    def ExtractTEntry(self, event):
        self.DateTo.set(self.calT.get_date())
        self.calT.destroy()

    def getTDate(self):
        try:
            self.calF.destroy()
        except:
            pass
        try:
            self.calT.destroy()
        except:
            pass
        self.calT = tkcalendar.Calendar(self.frame2, selectmode='day', year=2020, month=5, day=22)
        self.calT.place(x=400, y=10)
        self.root.bind("<Return>", self.ExtractTEntry)

    def Clear(self):
        self.DateFrom.set("")
        self.DateTo.set("")


    def Changebg(self):
        colors = ['red', 'green', 'Hot Pink', 'black', 'purple', 'Maroon']
        color = ['grey', 'pink', 'cyan', 'magenta']
        # color = ['Maroon', 'red', 'green', 'Hot Pink', 'black', 'purple']
        # colors = ['#314af7', '#f94b4b']
        # color = ['#f94b4b', '#314af7']
        if self.i >= len(colors) or self.i >= len(color):
            self.i = 0
        self.frame1.config(bg = f"{colors[self.i]}")
        self.text.config(bg = f"{colors[self.i]}")
        self.root.config(bg = f"{color[self.i]}")
        self.i += 1
        self.frame1.after(500, self.Changebg)


    def getconnection(self):
        connection = cx_Oracle.connect('system/69-Gilani-53@localhost:1521/orcl')
        return connection


    def Purchase(self):
        try:
            sdate = self.DateFrom.get()
            edate = self.DateTo.get()
            ms = sdate.split('/')[0]
            ds = sdate.split('/')[1]
            ys = sdate.split('/')[2]
            if len(ms) < 2:
                ms = f"0{ms}"
            if len(ds) < 2:
                ds = f"0{ds}"
            if len(ys) < 2:
                ys = f"0{ys}"
            sdate = f"{ms}/{ds}/{ys}"

            me = edate.split('/')[0]
            de = edate.split('/')[1]
            ye = edate.split('/')[2]
            if len(me) < 2:
                me = f"0{me}"
            if len(de) < 2:
                de = f"0{de}"
            if len(ye) < 2:
                ye = f"0{es}"
            edate = f"{me}/{de}/{ye}"
            connection = self.getconnection()
            cursor = connection.cursor()
            query = f"SELECT TO_CHAR(PURCHASEDATE, 'MM/DD/YY') AS PURCHASEPRICE, STOCKNO, MAKE, MODEL, PYEAR, VINNO, MILLAGE, PURCHASEPRICE, TITLE, BILLOFSALE, REMARK, CARLOCATION, PROBLEM1, PROBLEM2, PROBLEM3, CLIENTID FROM PURCHASE WHERE TO_CHAR(PURCHASEDATE, 'MM/DD/YY') >= '{sdate}' AND TO_CHAR(PURCHASEDATE, 'MM/DD/YY') <= '{edate}'"
            cursor.execute(query)
            rows = cursor.fetchall()
            with open("print(purchase).txt", "w") as f:
                for row in rows:
                    for i in row:
                        f.write(f"{i}, ")
                    f.write("\n")
                os.startfile('print(purchase).txt', 'print')
            connection.commit()
            cursor.close()
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")


    def Sale(self):
        try:
            sdate = self.DateFrom.get()
            edate = self.DateTo.get()
            ms = sdate.split('/')[0]
            ds = sdate.split('/')[1]
            ys = sdate.split('/')[2]
            if len(ms) < 2:
                ms = f"0{ms}"
            if len(ds) < 2:
                ds = f"0{ds}"
            if len(ys) < 2:
                ys = f"0{ys}"
            sdate = f"{ms}/{ds}/{ys}"

            me = edate.split('/')[0]
            de = edate.split('/')[1]
            ye = edate.split('/')[2]
            if len(me) < 2:
                me = f"0{me}"
            if len(de) < 2:
                de = f"0{de}"
            if len(ye) < 2:
                ye = f"0{es}"
            edate = f"{me}/{de}/{ye}"
            connection = self.getconnection()
            cursor = connection.cursor()
            query = f"SELECT STOCKNO, TO_CHAR(SALEDATE, 'MM/DD/YY') AS SALEDATE, MAKE, MODELNO, YEAR, TOTALCOST, PURCHASECOST, SALEPRICE, PROFIT, PAYMENTTYPE, TITLE, TAGS, CLIENTID FROM SALE WHERE TO_CHAR(SALEDATE, 'MM/DD/YY') >= '{sdate}' AND TO_CHAR(SALEDATE, 'MM/DD/YY') <= '{edate}'"
            cursor.execute(query)
            rows = cursor.fetchall()
            with open("print(sale).txt", "w") as f:
                for row in rows:
                    for i in row:
                        f.write(f"{i}, ")
                    f.write("\n")
                os.startfile('print(sale).txt', 'print')
            connection.commit()
            cursor.close()
        except Exception as e:
            tmsg.showerror("Error", f"Error Due To {e}")


if __name__ == "__main__":
    root = Tk()
    report = Report(root)
    root.mainloop()