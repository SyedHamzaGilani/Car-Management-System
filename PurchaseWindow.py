import tkinter.ttk
from tkinter import *
import tkinter.messagebox as tmsg
import cx_Oracle
import ctypes
import tkcalendar

class Purchase:
    def __init__(self, root):
        self.root = root
        self.root.title("Purchase Information")
        # self.Theme()
        self.count = 0
        self.words = ""
        self.c = 0
        self.bg = 0
        self.Changebg()
        # self.Theme()
        self.root.geometry("980x660+365+35")
        self.root.minsize(980, 660)
        self.root.maxsize(980, 660)
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
        self.frame2.place(x = 5, y = 60, width = 340, height = 540)
        Label(self.frame2, text = "Purchase Date", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Stock No", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Make", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Model", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "P_Year", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Vin No", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Millage", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Purchase Price", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Title", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Bill Of Sale", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Remark", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Car Location", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Problem 1", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Problem 2", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Problem 3", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Client ID", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        self.PurchaseDate = StringVar()
        self.StockNo = StringVar()
        self.Make = StringVar()
        self.Model = StringVar()
        self.PYear = StringVar()
        self.PYear.set('2006')
        self.VinNo = StringVar()
        self.Millage = StringVar()
        self.Millage.set('$000,00')
        self.PurchasePrice = StringVar()
        self.PurchasePrice.set('$000,00')
        self.Title = StringVar()
        self.BillOfSale = StringVar()
        self.Remark = StringVar()
        self.CarLocation = StringVar()
        self.Problem1 = StringVar()
        self.Problem1.set('None')
        self.Problem2 = StringVar()
        self.Problem2.set('None')
        self.Problem3 = StringVar()
        self.Problem3.set('None')
        self.ClientID = StringVar()
        self.PurchaseDateE = Entry(self.frame2, textvariable = self.PurchaseDate, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 5, width = 190)
        Button(self.frame2, text = "Cal", font = "Conicsansms 10 bold", fg = "Blue", command = self.getPDate).place(x = 288, y = 5, height = 20)
        self.StockNoE = tkinter.ttk.Combobox(self.frame2, textvariable = self.StockNo, font = "Conicsansms 10 bold")
        cc = self.getConnection()
        cr = cc.cursor()
        query = "SELECT STOCKNO FROM STOCK"
        cr.execute(query)
        rr = cr.fetchall()
        self.StockNoE['values'] = rr
        self.StockNoE.place(x = 130, y = 35, width = 190)
        connection = self.getConnection()
        cursor = connection.cursor()
        query = "SELECT MAKE FROM MAKEE"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.MakeE = tkinter.ttk.Combobox(self.frame2, textvariable = self.Make, font = "Conicsansms 10 bold")
        # self.MakeE['values'] = ['Acura', 'Chevy', 'Chrysler', 'Dodge', 'Ford', 'GMC', 'Honda', 'Mazda', 'Mitsubishi', 'Saturn', 'Toyota']
        # self.MakeE.set('Honda')
        self.MakeE['values'] = rows
        self.MakeE.place(x = 130, y = 65, width = 190)
        cursor1 = connection.cursor()
        query1 = "SELECT MODEL FROM MODELL"
        cursor1.execute(query1)
        rows1 = cursor1.fetchall()
        self.ModelE = tkinter.ttk.Combobox(self.frame2, textvariable = self.Model, font = "Conicsansms 10 bold")
        # self.ModelE['values'] = ['Explorer', 'Expedition', 'VUE', 'MDX', 'Fusion', 'Corolla', 'Montero', 'Acadia', 'Captiva', 'Element', 'CX-9']
        # self.ModelE.set('Element')
        self.ModelE['values'] = rows1
        self.ModelE.place(x = 130, y = 100, width = 190)
        self.PYearE = tkinter.ttk.Combobox(self.frame2, textvariable = self.PYear, font = "Conicsansms 10 bold")
        self.PYearE['values'] = ['1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        self.PYearE.set('2006')
        self.PYearE.place(x = 130, y = 135, width = 190)
        self.VinNoE = Entry(self.frame2, textvariable = self.VinNo, font = "Conicsansms 10 bold", fg = "Blue")
        self.VinNoE.place(x = 130, y = 170, width = 190)
        self.MillageE = Entry(self.frame2, textvariable = self.Millage, font = "Conicsansms 10 bold", fg = "Blue")
        self.MillageE.place(x = 130, y = 205, width = 190)
        self.PurchasePriceE = Entry(self.frame2, textvariable = self.PurchasePrice, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 235, width = 190)
        self.TitleE = tkinter.ttk.Checkbutton(self.frame2, text='Title', variable=self.Title, onvalue= True, offvalue= False).place(x = 130, y = 265, width = 190)
        self.BillOfSaleE = tkinter.ttk.Checkbutton(self.frame2, text='Bill Of Sale', variable=self.BillOfSale, onvalue= True, offvalue= False).place(x = 130, y = 295, width = 190)
        self.RemarkE = Entry(self.frame2, textvariable=self.Remark, font="Conicsansms 10 bold", fg="Blue")
        self.RemarkE.place(x=130, y=330, width=190)
        self.CarLocationE = Entry(self.frame2, textvariable=self.CarLocation, font="Conicsansms 10 bold", fg="Blue")
        self.CarLocationE.place(x=130, y=370, width=190)
        self.Problem1E = Entry(self.frame2, textvariable=self.Problem1, font="Conicsansms 10 bold", fg="Blue")
        self.Problem1E.place(x=130, y=400, width=190)
        self.Problem2E = Entry(self.frame2, textvariable=self.Problem2, font="Conicsansms 10 bold", fg="Blue")
        self.Problem2E.place(x=130, y=430, width=190)
        self.Problem3E = Entry(self.frame2, textvariable=self.Problem3, font="Conicsansms 10 bold", fg="Blue")
        self.Problem3E.place(x=130, y=465, width=190)
        self.ClientIDE = tkinter.ttk.Combobox(self.frame2, textvariable=self.ClientID, font="Conicsansms 10 bold")
        cc = self.getConnection()
        cr = cc.cursor()
        qu = 'SELECT IDNUMBER FROM CLIENT'
        cr.execute(qu)
        rc = cr.fetchall()
        self.ClientIDE['values'] = rc
        self.ClientIDE.place(x=130, y=500, width=190)

        ##############################################################

        self.frame3 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame3.place(x = 5, y = 605, width = 340, height = 50)
        Button(self.frame3, text = 'Add', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, width = 5, command = self.insert).grid(row = 0, column = 0, padx = 5, pady = 5)
        Button(self.frame3, text = 'Update', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Update).grid(row = 0, column = 1, padx = 5, pady = 5)
        Button(self.frame3, text = 'Delete', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Delete).grid(row = 0, column = 2, padx = 5, pady = 5)
        Button(self.frame3, text = 'Clear', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Clear).grid(row = 0, column = 3, padx = 5, pady = 5)
        Button(self.frame3, text = 'Exit', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, width = 5, command = self.root.destroy).grid(row = 0, column = 4, padx = 5, pady = 5)

        ##############################################################

        self.frame4 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame4.place(x = 355, y = 60, width = 620, height = 595)
        Label(self.frame4, text = "Search By", font = "Conicsansms 12 bold", bg = 'Cyan', fg = "Blue").place(x = 5, y = 9)
        self.searchby = StringVar()
        self.search = StringVar()
        self.searchby = tkinter.ttk.Combobox(self.frame4, textvariable = self.searchby, font = "Conicsansms 10 bold")
        self.searchby['values'] = ['StockNo']
        # self.searchby.set("PurchaseDate")
        self.searchby.place(x = 100, y = 10, width = 130)
        self.searchE = Entry(self.frame4, textvariable = self.search, font = "Conicsansms 10 bold", fg = "Blue")
        self.searchE.place(x = 240, y = 10, width = 140)
        # Button(self.frame4, text = "Cal", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.getDate).place(x = 390, y = 9,height = 25)
        Button(self.frame4, text = "Search", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Search).place(x = 390, y = 9, height = 25, width = 100)
        Button(self.frame4, text = "Show All", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Fetch).place(x = 500, y = 9, height = 25, width = 100)
        scrollX = Scrollbar(self.frame4, orient = HORIZONTAL)
        scrollX.place(x = 5, y = 565, width = 580)
        scrollY = Scrollbar(self.frame4, orient = VERTICAL)
        scrollY.place(x = 590, y = 50, height = 520)
        self.Tree = tkinter.ttk.Treeview(self.frame4, xscrollcommand = scrollX.set, yscrollcommand = scrollY.set, column = ('Purchase Date', 'StockNo', 'Make', 'Model', 'PYear', 'VinNo', 'Millage', 'Purchase Price', 'Title', 'Bill Of Sale', 'Remark', 'Car Location', 'Problem 1', 'Problem 2', 'Problem 3', 'Client ID'))
        self.Tree.heading('Purchase Date', text = 'Purchase Date')
        self.Tree.heading('StockNo', text = 'StockNo')
        self.Tree.heading('Make', text = 'Make')
        self.Tree.heading('Model', text = 'Model')
        self.Tree.heading('PYear', text = 'PYear')
        self.Tree.heading('VinNo', text = 'VinNo')
        self.Tree.heading('Millage', text = 'Millage')
        self.Tree.heading('Purchase Price', text = 'Purchase Price')
        self.Tree.heading('Title', text = 'Title')
        self.Tree.heading('Bill Of Sale', text = 'Bill Of Sale')
        self.Tree.heading('Remark', text = 'Remark')
        self.Tree.heading('Car Location', text = 'Car Location')
        self.Tree.heading('Problem 1', text = 'Problem 1')
        self.Tree.heading('Problem 2', text = 'Problem 2')
        self.Tree.heading('Problem 3', text = 'Problem 3')
        self.Tree.heading('Client ID', text = 'Client ID')
        self.Tree['show'] = ['headings']
        self.Tree.column('Purchase Date', width = 100)
        self.Tree.column('StockNo', width = 100)
        self.Tree.column('Make', width = 50)
        self.Tree.column('Model', width = 50)
        self.Tree.column('PYear', width = 50)
        self.Tree.column('VinNo', width = 80)
        self.Tree.column('Millage', width = 80)
        self.Tree.column('Purchase Price', width = 100)
        self.Tree.column('Title', width = 150)
        self.Tree.column('Bill Of Sale', width = 10)
        self.Tree.column('Remark', width = 10)
        self.Tree.column('Car Location', width = 150)
        self.Tree.column('Problem 1', width = 150)
        self.Tree.column('Problem 2', width = 150)
        self.Tree.column('Problem 3', width = 150)
        self.Tree.column('Client ID', width = 50)
        self.Tree.place(x = 5, y = 50, width = 580, height = 510)
        scrollX.config(command = self.Tree.xview)
        scrollY.config(command = self.Tree.yview)
        self.Tree.bind("<Double-Button-1>", self.get_Cursor)
        self.Fetch()


        ##################################



    def MovingText(self):
        a = "Add Purchase Information Here"
        if self.count >= len(a):
            self.count = 0
            self.words = ""
        self.words += a[self.count]
        self.count += 1
        colors = ['Red', 'Blue', 'Purple', 'Orange', 'Green', 'Maroon']
        if self.c >= len(colors):
            self.c = 0
        self.text.config(text = a, fg = f"{colors[self.c]}")
        self.c += 1
        self.text.after(500, self.MovingText)

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
            mil = self.Millage.get()
            mil = str(mil)
            x = mil.split(',')[0]
            y = mil.split(',')[1]
            if len(y) > 2:
                y = y[0:2]
            mil = f"{x},{y}"
            pp = self.PurchasePrice.get()
            pp = str(pp)
            a = pp.split(',')[0]
            b = pp.split(',')[1]
            if len(b) > 2:
                b = b[0:2]
            pp = f"{a},{b}"
            pd = self.PurchaseDate.get()
            sno = self.StockNo.get()
            mk = self.Make.get().upper()
            md = self.Model.get().upper()
            py = self.PYear.get()
            vn = self.VinNo.get()
            # mil = self.Millage.get()
            # pp = self.PurchasePrice.get()
            tit = self.Title.get()
            bos = self.BillOfSale.get()
            rmk = self.Remark.get().upper()
            cloc = self.CarLocation.get().upper()
            p1 = self.Problem1.get().upper()
            p2 = self.Problem2.get().upper()
            p3 = self.Problem3.get().upper()
            cid = self.ClientID.get()
            connection = self.getConnection()
            cursor = connection.cursor()
            query = f"INSERT INTO PURCHASE (PURCHASEDATE, STOCKNO, MAKE, MODEL, PYEAR, VINNO, MILLAGE, PURCHASEPRICE, TITLE, BILLOFSALE, REMARK, CARLOCATION, PROBLEM1, PROBLEM2, PROBLEM3, CLIENTID) VALUES (TO_DATE('{pd}', 'MM/DD/YY'), '{sno}', '{mk}', '{md}', '{py}', '{vn}', '{mil}', '{pp}', {tit}, {bos}, '{rmk}', '{cloc}', '{p1}', '{p2}', '{p3}', '{cid}')"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            self.Fetch()
            self.Clear()
        except Exception as e:
            tmsg.showerror("Invalid Entities", f"Check Stock Number Or Error Due To {e}")

    def get_Cursor(self, event):
        try:
            cursor = self.Tree.focus()
            items = self.Tree.item(cursor)
            row = items['values']
            self.PurchaseDate.set(row[0])
            self.StockNo.set(row[1])
            self.Make.set(row[2])
            self.Model.set(row[3])
            self.PYear.set(row[4])
            self.VinNo.set(row[5])
            self.Millage.set(row[6])
            self.PurchasePrice.set(row[7])
            self.Title.set(row[8])
            self.BillOfSale.set(row[9])
            self.Remark.set(row[10])
            self.CarLocation.set(row[11])
            self.Problem1.set(row[12])
            self.Problem2.set(row[13])
            self.Problem3.set(row[14])
            self.ClientID.set(row[15])
        except Exception as e:
            pass

    # def ExtractSearch(self, event):
    #     print("Calling")
    #     # self.searchby.set(self.cal.get_date())
    #     self.search.set(self.cal.get_date())
    #     print(self.cal.get_date())
    #     self.cal.destroy()

    def ExtractEntry(self, event):
        self.PurchaseDate.set(self.cal.get_date())
        self.cal.destroy()

    def getPDate(self):
        self.cal = tkcalendar.Calendar(self.frame2, selectmode='day', year=2020, month=5, day=22)
        self.cal.place(x=80, y=5)
        self.root.bind("<Return>", self.ExtractEntry)

    # def getDate(self):
    #     self.cal = Calendar(self.frame4, selectmode='day', year=2020, month=5, day=22)
    #     self.cal.place(x=240, y=10)
    #     self.root.bind("<Return>", self.ExtractSearch)

    def Fetch(self):
        # if self.searchby.get() == "PurchaseDate":
        #     self.cal = Calendar(self.frame4, selectmode='day', year=2020, month=5, day=22)
        #     self.cal.place(x=240, y=10)
        connection = self.getConnection()
        cursor = connection.cursor()
        query = "SELECT TO_CHAR(PURCHASEDATE, 'MM/DD/YY HH24:MI') AS PURCHASEDATE, STOCKNO, MAKE, MODEL, PYEAR, VINNO, MILLAGE, PURCHASEPRICE, TITLE, BILLOFSALE, REMARK, CARLOCATION, PROBLEM1, PROBLEM2, PROBLEM3, CLIENTID  FROM PURCHASE ORDER BY STOCKNO ASC"
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
                query = f"DELETE FROM PURCHASE WHERE STOCKNO = '{rows[1]}'"
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
                self.Clear()
        except Exception as e:
            tmsg.showerror("Deletion Error", f"No Stock Number Is Selected In The Field Or Error Due To {e}")

    def Clear(self):
        self.PurchaseDate.set("")
        self.StockNo.set("")
        self.Make.set("")
        self.Model.set("")
        self.PYear.set("")
        self.VinNo.set("")
        # self.Millage.set("")
        # self.PurchasePrice.set("")
        self.Title.set("")
        self.BillOfSale.set("")
        self.Remark.set("")
        self.CarLocation.set("")
        # self.Problem1.set("")
        # self.Problem2.set("")
        # self.Problem3.set("")
        self.ClientID.set("")
        self.searchby.set("")
        self.search.set("")
        self.Fetch()

    def Update(self):
        try:
            pd = self.PurchaseDate.get()
            sno = self.StockNo.get()
            mk = self.Make.get().upper()
            md = self.Model.get().upper()
            py = self.PYear.get()
            vn = self.VinNo.get()
            mil = self.Millage.get()
            pp = self.PurchasePrice.get()
            tit = self.Title.get()
            bos = self.BillOfSale.get()
            rmk = self.Remark.get().upper()
            cloc = self.CarLocation.get().upper()
            p1 = self.Problem1.get().upper()
            p2 = self.Problem2.get().upper()
            p3 = self.Problem3.get().upper()
            cid = self.ClientID.get()
            connection = self.getConnection()
            # query = f"UPDATE CUSTOMER SET CUSTOMER_StockNo = '{self.StockNo.get()}', Make = '{self.Make.get()}', Model_NO = '{self.Model.get()}', PYear = '{self.PYear.get()}', VinNo = '{self.VinNo.get()}', ID_PROOF_TYPE = '{self.Millage.get()}', ID_NUMBER = '{self.PurchasePrice.get()}', Title = '{self.Title.get()}' WHERE REF_NO = {self.PurchaseDate.get()}"
            query = f"UPDATE PURCHASE SET PURCHASEDATE = TO_DATE('{pd}', 'MM/DD/YY'), MAKE = '{mk}', MODEL = '{md}', PYEAR = '{py}', VINNO = '{vn}', MILLAGE = '{mil}', PURCHASEPRICE = '{pp}', TITLE = {tit}, BILLOFSALE = {bos}, REMARK = '{rmk}', CARLOCATION = '{cloc}', PROBLEM1 = '{p1}', PROBLEM2 = '{p2}', PROBLEM3 = '{p3}', CLIENTID = '{cid}' WHERE STOCKNO = '{sno}'"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.Fetch()
            self.Clear()
            tmsg.showinfo("Updated", "Purchase Is Updated Successfully")
        except Exception as e:
            tmsg.showerror("Update Error", f"No Stock Number Is Selected In The Field For Updating Or Error Due To {e}")

    def Search(self):
        try:
            connection = self.getConnection()
            # query = "SELECT TO_CHAR(PURCHASEDATE, 'DD-MM-YYYY') AS PURCHASEDATE, STOCKNO, MAKE, MODEL, PYEAR, VINNO, MILLAGE, PURCHASEPRICE, TITLE, BILLOFSALE, REMARK, CARLOCATION, PROBLEM1, PROBLEM2, PROBLEM3, CLIENTID  FROM PURCHASE WHERE " + str(self.searchby.get()) + " = '" + str(self.search.get()).upper() + "'"
            if self.searchby.get().upper() == 'PURCHASEDATE':
                query = f"SELECT TO_CHAR(PURCHASEDATE, 'MM/DD/YY') AS PURCHASEDATE, STOCKNO, MAKE, MODEL, PYEAR, VINNO, MILLAGE, PURCHASEPRICE, TITLE, BILLOFSALE, REMARK, CARLOCATION, PROBLEM1, PROBLEM2, PROBLEM3, CLIENTID  FROM PURCHASE WHERE {self.searchby.get().upper()} = TO_DATE('{self.search.get()}', 'MM/DD/YY')"
            else:
                query = f"SELECT TO_CHAR(PURCHASEDATE, 'MM/DD/YY') AS PURCHASEDATE, STOCKNO, MAKE, MODEL, PYEAR, VINNO, MILLAGE, PURCHASEPRICE, TITLE, BILLOFSALE, REMARK, CARLOCATION, PROBLEM1, PROBLEM2, PROBLEM3, CLIENTID  FROM PURCHASE WHERE {self.searchby.get().upper()} = '{self.search.get().upper()}'"
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
            tmsg.showerror("Search Error", f"Search Field Is Empty, Please Fill The Search Entry Or Error Due To {e}")



if __name__ == "__main__":
    root = Tk()
    purchase = Purchase(root)
    root.mainloop()