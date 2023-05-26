import tkinter.ttk
from tkinter import *
import tkinter.messagebox as tmsg
import cx_Oracle
import ctypes
import tkcalendar

class Sale:
    def __init__(self, root):
        self.root = root
        self.root.title("Sale Information")
        # self.Theme()
        self.count = 0
        self.words = ""
        self.c = 0
        self.bg = 0
        self.Changebg()
        # self.Theme()
        self.root.geometry("980x550+365+135")
        self.root.minsize(980, 550)
        self.root.maxsize(980, 550)
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
        self.frame2.place(x = 5, y = 60, width = 340, height = 430)
        Label(self.frame2, text = "Stock No", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Sale Date", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Make", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Model No", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Year", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Total Cost", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Purchase Cost", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Sale Price", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Profit", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Payment Type", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Title", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Tags", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        Label(self.frame2, text = "Client ID", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 4, anchor = NW)
        self.StockNo = StringVar()
        self.SaleDate = StringVar()
        self.Make = StringVar()
        self.ModelNo = StringVar()
        self.Year = StringVar()
        self.Year.set('2006')
        self.TotalCost = StringVar()
        self.TotalCost.set('$000,00')
        self.PurchaseCost = StringVar()
        self.PurchaseCost.set('$000,00')
        self.SalePrice = StringVar()
        self.SalePrice.set('$000,00')
        self.Profit = StringVar()
        self.Profit.set('$000,00')
        self.PaymentType = StringVar()
        self.Title = StringVar()
        self.Tag = StringVar()
        self.ClientID = StringVar()
        self.StockNoE = tkinter.ttk.Combobox(self.frame2, textvariable = self.StockNo, font = "Conicsansms 10 bold")
        cc = self.getConnection()
        cr = cc.cursor()
        query = "SELECT STOCKNO FROM STOCK"
        cr.execute(query)
        rr = cr.fetchall()
        cc.commit()
        cr.close()
        self.StockNoE.place(x = 130, y = 5, width = 190)
        self.StockNoE['values'] = rr
        self.SaleDateE = Entry(self.frame2, textvariable = self.SaleDate, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 35, width = 190)
        Button(self.frame2, text="Cal", font="Conicsansms 10 bold", fg="Blue", command=self.getPDate).place(x=288, y=35, height=20)
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
        self.ModelNoE = tkinter.ttk.Combobox(self.frame2, textvariable = self.ModelNo, font = "Conicsansms 10 bold")
        # self.ModelNoE['values'] = ['Explorer', 'Expedition', 'VUE', 'MDX', 'Fusion', 'Corolla', 'Montero', 'Acadia', 'Captiva', 'Element', 'CX-9']
        # self.ModelNoE.set('Element')
        self.ModelNoE['values'] = rows1
        self.ModelNoE.place(x = 130, y = 100, width = 190)
        self.YearE = tkinter.ttk.Combobox(self.frame2, textvariable = self.Year, font = "Conicsansms 10 bold")
        self.YearE['values'] = ['1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        self.YearE.place(x = 130, y = 135, width = 190)
        self.TotalCostE = Entry(self.frame2, textvariable = self.TotalCost, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 170, width = 190)
        self.PurchaseCostE = Entry(self.frame2, textvariable = self.PurchaseCost, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 205, width = 190)
        self.SalePriceE = Entry(self.frame2, textvariable = self.SalePrice, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 235, width = 190)
        self.ProfitE = Entry(self.frame2, font = "Conicsansms 10 bold",textvariable = self.Profit, fg = "Blue").place(x = 130, y = 265, width = 190)
        self.PaymentTypeE = tkinter.ttk.Combobox(self.frame2, font = "Conicsansms 10 bold",textvariable = self.PaymentType)
        self.PaymentTypeE['values'] = ["Cash", "Visa", "Check"]
        self.PaymentTypeE.set("Cash")
        self.PaymentTypeE.place(x = 130, y = 300, width = 190)
        self.TitleE = tkinter.ttk.Checkbutton(self.frame2, text='Title', variable=self.Title, onvalue=True, offvalue=False, command=None).place(x=130, y=335, width=190)
        self.TagE = tkinter.ttk.Checkbutton(self.frame2, text='Tag', variable=self.Tag, onvalue=True, offvalue=False, command=None).place(x=130, y=365,width=190)
        self.ClientIDE = tkinter.ttk.Combobox(self.frame2, font = "Conicsansms 10 bold",textvariable = self.ClientID)
        cc = self.getConnection()
        cr = cc.cursor()
        query = "SELECT IDNUMBER FROM CLIENT"
        cr.execute(query)
        rr = cr.fetchall()
        cc.commit()
        cr.close()
        self.ClientIDE['values'] = rr
        self.ClientIDE.place(x=130, y=395,width=190)

        ##############################################################

        self.frame3 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame3.place(x = 5, y = 495, width = 340, height = 50)
        Button(self.frame3, text = 'Add', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, width = 5, command = self.insert).grid(row = 0, column = 0, padx = 5, pady = 5)
        Button(self.frame3, text = 'Update', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Update).grid(row = 0, column = 1, padx = 5, pady = 5)
        Button(self.frame3, text = 'Delete', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Delete).grid(row = 0, column = 2, padx = 5, pady = 5)
        Button(self.frame3, text = 'Clear', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Clear).grid(row = 0, column = 3, padx = 5, pady = 5)
        Button(self.frame3, text = 'Exit', font = 'Conicsansms 10 bold', fg = 'Cyan', bg = 'Blue', cursor = "hand2", bd = 5, relief = SUNKEN, width = 5, command = self.root.destroy).grid(row = 0, column = 4, padx = 5, pady = 5)

        ##############################################################

        self.frame4 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame4.place(x = 355, y = 60, width = 620, height = 485)
        Label(self.frame4, text = "Search By", font = "Conicsansms 12 bold", bg = 'Cyan', fg = "Blue").place(x = 5, y = 9)
        self.searchby = StringVar()
        self.search = StringVar()
        self.searchby = tkinter.ttk.Combobox(self.frame4, textvariable = self.searchby, font = "Conicsansms 10 bold")
        self.searchby['values'] = ['StockNo']
        self.searchby.place(x = 100, y = 10, width = 130)
        self.searchE = Entry(self.frame4, textvariable = self.search, font = "Conicsansms 10 bold", fg = "Blue")
        self.searchE.place(x = 240, y = 10, width = 140)
        Button(self.frame4, text = "Search", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Search).place(x = 390, y = 9, width = 100, height = 25)
        Button(self.frame4, text = "Show All", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Fetch).place(x = 500, y = 9, width = 100, height = 25)
        scrollX = Scrollbar(self.frame4, orient = HORIZONTAL)
        scrollX.place(x = 5, y = 455, width = 580)
        scrollY = Scrollbar(self.frame4, orient = VERTICAL)
        scrollY.place(x = 590, y = 50, height = 410)
        self.Tree = tkinter.ttk.Treeview(self.frame4, xscrollcommand = scrollX.set, yscrollcommand = scrollY.set, column = ('Stock No', 'Sale Date', 'Make', 'Model No', 'Year', 'Total Cost','Purchase Cost', 'Sale Price', 'Profit', 'Payment Type', 'Title', 'Tags', 'Client ID'))
        self.Tree.heading('Stock No', text = 'Stock No')
        self.Tree.heading('Sale Date', text = 'Sale Date')
        self.Tree.heading('Make', text = 'Make')
        self.Tree.heading('Model No', text = 'Model No')
        self.Tree.heading('Year', text = 'Year')
        self.Tree.heading('Total Cost', text = 'Total Cost')
        self.Tree.heading('Purchase Cost', text = 'Purchase Cost')
        self.Tree.heading('Sale Price', text = 'Sale Price')
        self.Tree.heading('Profit', text = 'Profit')
        self.Tree.heading('Payment Type', text = 'Payment Type')
        self.Tree.heading('Title', text = 'Title')
        self.Tree.heading('Tags', text = 'Tags')
        self.Tree.heading('Client ID', text = 'Client ID')
        self.Tree['show'] = ['headings']
        self.Tree.column('Stock No', width = 80)
        self.Tree.column('Sale Date', width = 80)
        self.Tree.column('Make', width = 80)
        self.Tree.column('Model No', width = 80)
        self.Tree.column('Year', width = 40)
        self.Tree.column('Total Cost', width = 100)
        self.Tree.column('Purchase Cost', width = 100)
        self.Tree.column('Sale Price', width = 100)
        self.Tree.column('Profit', width = 100)
        self.Tree.column('Payment Type', width = 100)
        self.Tree.column('Title', width = 40)
        self.Tree.column('Tags', width = 40)
        self.Tree.column('Client ID', width = 60)
        self.Tree.place(x = 5, y = 50, width = 580, height = 400)
        scrollX.config(command = self.Tree.xview)
        scrollY.config(command = self.Tree.yview)
        self.Tree.bind("<Double-Button-1>", self.get_Cursor)
        self.Fetch()



        ##################################

    def ExtractEntry(self, event):
        self.SaleDate.set(self.cal.get_date())
        self.cal.destroy()

    def getPDate(self):
        self.cal = tkcalendar.Calendar(self.frame2, selectmode='day', year=2020, month=5, day=22)
        self.cal.place(x=80, y=10)
        self.root.bind("<Return>", self.ExtractEntry)

    def MovingText(self):
        a = "Add Sale Information Here"
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
            TotalCost = self.TotalCost.get()
            TotalCost = str(TotalCost)
            x1 = TotalCost.split(',')[0]
            y1 = TotalCost.split(',')[1]
            if len(y1) > 2:
                y1 = y1[0:2]
            TotalCost = f"{x1},{y1}"
            PurchaseCost = self.PurchaseCost.get()
            PurchaseCost = str(PurchaseCost)
            a1 = PurchaseCost.split(',')[0]
            b1 = PurchaseCost.split(',')[1]
            if len(b1) > 2:
                b1 = b1[0:2]
            PurchaseCost = f"{a1},{b1}"
            SalePrice = self.SalePrice.get()
            SalePrice = str(SalePrice)
            x2 = SalePrice.split(',')[0]
            y2 = SalePrice.split(',')[1]
            if len(y2) > 2:
                y2 = y2[0:2]
            SalePrice = f"{x2},{y2}"
            Profit = self.Profit.get()
            Profit = str(Profit)
            a2 = Profit.split(',')[0]
            b2 = Profit.split(',')[1]
            if len(b2) > 2:
                b2 = b2[0:2]
            Profit = f"{a2},{b2}"
            StockNo = self.StockNo.get()
            SaleDate = (self.SaleDate.get()).upper()
            Make = self.Make.get().upper().upper()
            ModelNo = self.ModelNo.get().upper().upper()
            Year = self.Year.get()
            # TotalCost = self.TotalCost.get()
            # PurchaseCost = self.PurchaseCost.get()
            # SalePrice = self.SalePrice.get()
            # Profit = self.ProfitE.get("1.0", END)
            # Profit = self.Profit.get()
            payment = self.PaymentType.get().upper().upper()
            tit = self.Title.get()
            tg = self.Tag.get()
            cid = self.ClientID.get()
            connection = self.getConnection()
            cursor = connection.cursor()
            query = f"INSERT INTO SALE (STOCKNO, SALEDATE, MAKE, MODELNO, YEAR, TOTALCOST, PURCHASECOST, SALEPRICE, PROFIT, PAYMENTTYPE, TITLE, TAGS, CLIENTID) VALUES ('{StockNo}', TO_DATE('{SaleDate}', 'MM/DD/YY'), '{Make}', '{ModelNo}', '{Year}', '{TotalCost}', '{PurchaseCost}', '{SalePrice}', '{Profit}', '{payment}', {tit}, {tg}, '{cid}')"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            self.Fetch()
            self.Clear()
        except Exception as e:
            tmsg.showerror("Invalid Entities", f"Check Stock No Or Error Due To {e}")

    def get_Cursor(self, event):
        try:
            cursor = self.Tree.focus()
            items = self.Tree.item(cursor)
            row = items['values']
            self.StockNo.set(row[0])
            self.SaleDate.set(row[1])
            self.Make.set(row[2])
            self.ModelNo.set(row[3])
            self.Year.set(row[4])
            self.TotalCost.set(row[5])
            self.PurchaseCost.set(row[6])
            self.SalePrice.set(str(row[7]))
            self.Profit.set(row[8])
            self.PaymentType.set(row[9])
            self.Title.set(row[10])
            self.Tag.set(row[11])
            self.ClientID.set(row[12])
        except Exception as e:
            pass

    def Fetch(self):
        connection = self.getConnection()
        cursor = connection.cursor()
        query = "SELECT STOCKNO, TO_CHAR(SALEDATE, 'MM/DD/YY') AS SALEDATE, MAKE, ModelNo, YEAR, TOTALCOST, PURCHASECOST, SALEPRICE, PROFIT, PAYMENTTYPE, TITLE, TAGS, CLIENTID  FROM SALE ORDER BY STOCKNO ASC"
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
                # query = f"DELETE FROM SALE WHERE StockNo_NO = {rows[0]}"
                query = f"DELETE FROM SALE WHERE STOCKNO = '{rows[0]}'"
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
                self.Clear()
        except:
            tmsg.showerror("Deletion Error", "No Sale Is Selected In The Field")

    def Clear(self):
        self.StockNo.set("")
        self.SaleDate.set("")
        self.Make.set("")
        self.ModelNo.set("")
        self.Year.set("")
        # self.TotalCost.set("")
        # self.PurchaseCost.set("")
        # self.SalePrice.set(str(""))
        # self.Profit.set("")
        self.PaymentType.set("")
        self.Title.set("")
        self.Tag.set("")
        self.ClientID.set("")
        self.searchby.set("")
        self.search.set("")
        self.Fetch()

    def Update(self):
        try:
            TotalCost = self.TotalCost.get()
            TotalCost = str(TotalCost)
            x1 = TotalCost.split(',')[0]
            y1 = TotalCost.split(',')[1]
            if len(y1) > 2:
                y1 = y1[0:2]
            TotalCost = f"{x1},{y1}"
            PurchaseCost = self.PurchaseCost.get()
            PurchaseCost = str(PurchaseCost)
            a1 = PurchaseCost.split(',')[0]
            b1 = PurchaseCost.split(',')[1]
            if len(b1) > 2:
                b1 = b1[0:2]
            PurchaseCost = f"{a1},{b1}"
            SalePrice = self.SalePrice.get()
            SalePrice = str(SalePrice)
            x2 = SalePrice.split(',')[0]
            y2 = SalePrice.split(',')[1]
            if len(y2) > 2:
                y2 = y2[0:2]
            SalePrice = f"{x2},{y2}"
            Profit = self.Profit.get()
            Profit = str(Profit)
            a2 = Profit.split(',')[0]
            b2 = Profit.split(',')[1]
            if len(b2) > 2:
                b2 = b2[0:2]
            Profit = f"{a2},{b2}"
            StockNo = self.StockNo.get()
            SaleDate = (self.SaleDate.get()).upper()
            Make = self.Make.get().upper().upper()
            ModelNo = self.ModelNo.get().upper().upper()
            Year = self.Year.get()
            # TotalCost = self.TotalCost.get()
            # PurchaseCost = self.PurchaseCost.get()
            # SalePrice = self.SalePrice.get()
            # Profit = self.ProfitE.get("1.0", END)
            # Profit = self.Profit.get()
            payment = self.PaymentType.get().upper().upper()
            tit = self.Title.get()
            tg = self.Tag.get()
            cid = self.ClientID.get()
            connection = self.getConnection()
            # query = f"UPDATE SALE SET SALE_SaleDate = '{self.SaleDate.get()}', Make = '{self.Make.get()}', ModelNo_NO = '{self.ModelNo.get()}', Year = '{self.Year.get()}', TotalCost = '{self.TotalCost.get()}', ID_PROOF_TYPE = '{self.PurchaseCost.get()}', ID_NUMBER = '{self.SalePrice.get()}', Profit = '{self.Profit.get()}' WHERE StockNo_NO = {self.StockNo.get()}"
            query = f"UPDATE SALE SET SALEDATE = TO_DATE('{SaleDate}', 'MM/DD/YY'), MAKE = '{Make}', MODELNO = '{ModelNo}', YEAR = '{Year}', TOTALCOST = '{TotalCost}', PURCHASECOST = '{PurchaseCost}', SALEPRICE = '{SalePrice}', PROFIT = '{Profit}', PAYMENTTYPE = '{payment}', TITLE = {tit}, TAGS = {tg}, CLIENTID = '{cid}' WHERE STOCKNO = '{StockNo}'"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.Fetch()
            self.Clear()
            tmsg.showinfo("Updated", "Sale Updated Successfully")
        except Exception as e:
            tmsg.showerror("Update Error", "No Sale Is Selected In The Field For Updating")

    def Search(self):
        try:
            connection = self.getConnection()
            # query = "SELECT STOCKNO, TO_CHAR(SALEDATE, 'DD-MM-YYYY') AS SALEDATE, MAKE, ModelNo, YEAR, TOTALCOST, PURCHASECOST, SALEPRICE, PROFIT, PAYMENTTYPE, TITLE, TAGS, CLIENTID FROM SALE WHERE " + str(self.searchby.get()) + " = '" + str(self.search.get()).upper() + "'"
            if self.searchby.get().upper() == 'SALEDATE':
                query = f"SELECT STOCKNO, TO_CHAR(SALEDATE, 'MM/DD/YY') AS SALEDATE, MAKE, MODELNO, YEAR, TOTALCOST, PURCHASECOST, SALEPRICE, PROFIT, PAYMENTTYPE, TITLE, TAGS, CLIENTID  FROM SALE WHERE SALEDATE = TO_DATE('{self.search.get()}', 'DD-MM-YYYY')"
            else:
                query = f"SELECT STOCKNO, TO_CHAR(SALEDATE, 'MM/DD/YY') AS SALEDATE, MAKE, MODELNO, YEAR, TOTALCOST, PURCHASECOST, SALEPRICE, PROFIT, PAYMENTTYPE, TITLE, TAGS, CLIENTID  FROM SALE WHERE {self.searchby.get().upper()} = '{self.search.get().upper()}'"
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
    sale = Sale(root)
    root.mainloop()