import tkinter.ttk
from tkinter import *
import tkinter.messagebox as tmsg
import cx_Oracle
import ctypes

class Stock:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Information")
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
        Label(self.frame2, text = "STOCK INFORMATION", font = "Conicsansms 18 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 30)
        Label(self.frame2, text = "Stock No", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 30, anchor = NW)
        Label(self.frame2, text = "Stock Name", font = "Conicsansms 12 bold", bg = "Cyan", fg = "Blue").pack(padx = 5, pady = 30, anchor = NW)
        self.StockNo = StringVar()
        self.STOCKNAME = StringVar()
        self.StockNoE = Entry(self.frame2, textvariable = self.StockNo, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 125, width = 190)
        self.STOCKNAMEE = Entry(self.frame2, textvariable = self.STOCKNAME, font = "Conicsansms 10 bold", fg = "Blue").place(x = 130, y = 215, width = 190)

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
        self.searchby['values'] = ['StockNo', 'StockName']
        self.searchby.place(x = 100, y = 10, width = 130)
        self.searchE = Entry(self.frame4, textvariable = self.search, font = "Conicsansms 10 bold", fg = "Blue")
        self.searchE.place(x = 240, y = 10, width = 140)
        Button(self.frame4, text = "Search", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Search).place(x = 390, y = 9, width = 100, height = 25)
        Button(self.frame4, text = "Show All", font = "Conicsansms 12 bold", fg = "Cyan", bg = "Blue", cursor = "hand2", bd = 5, relief = SUNKEN, command = self.Fetch).place(x = 500, y = 9, width = 100, height = 25)
        scrollX = Scrollbar(self.frame4, orient = HORIZONTAL)
        scrollX.place(x = 5, y = 345, width = 580)
        scrollY = Scrollbar(self.frame4, orient = VERTICAL)
        scrollY.place(x = 590, y = 50, height = 300)
        self.Tree = tkinter.ttk.Treeview(self.frame4, xscrollcommand = scrollX.set, yscrollcommand = scrollY.set, column = ('Stock No', 'Stock Name'))
        self.Tree.heading('Stock No', text = 'Stock No')
        self.Tree.heading('Stock Name', text = 'Stock Name')
        self.Tree['show'] = ['headings']
        self.Tree.column('Stock No', width = 80)
        self.Tree.column('Stock Name', width = 80)
        self.Tree.place(x = 5, y = 50, width = 580, height = 290)
        scrollX.config(command = self.Tree.xview)
        scrollY.config(command = self.Tree.yview)
        self.Tree.bind("<Double-Button-1>", self.get_Cursor)
        self.Fetch()



        ##################################

    def MovingText(self):
        a = "Add Stock Information Here"
        if self.count >= len(a):
            self.count = 0
            self.words = ""
        # self.words += a[self.count]
        # self.count += 1
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
            StockNo = self.StockNo.get()
            STOCKNAME = (self.STOCKNAME.get()).upper()
            connection = self.getConnection()
            cursor = connection.cursor()
            query = f"INSERT INTO STOCK (STOCKNO, STOCKNAME) VALUES ('{StockNo}', '{STOCKNAME}')"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            self.Fetch()
            self.Clear()
        except Exception as e:
            tmsg.showerror("Invalid Entities", f"Check StockNo No Or Error Due To {e}")

    def get_Cursor(self, event):
        try:
            cursor = self.Tree.focus()
            items = self.Tree.item(cursor)
            row = items['values']
            self.StockNo.set(row[0])
            self.STOCKNAME.set(row[1])
        except Exception as e:
            pass

    def Fetch(self):
        connection = self.getConnection()
        cursor = connection.cursor()
        query = "SELECT STOCKNO, STOCKNAME FROM STOCK ORDER BY STOCKNO ASC"
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
                query = f"DELETE FROM STOCK WHERE STOCKNO = '{rows[0]}'"
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                cursor.close()
                self.Fetch()
                self.Clear()
        except Exception as e:
            tmsg.showerror("Deletion Error", f"No Stock Is Selected In The Field Or Error Due To {e}")

    def Clear(self):
        self.StockNo.set("")
        self.STOCKNAME.set("")
        self.Fetch()

    def Update(self):
        try:
            connection = self.getConnection()
            # query = f"UPDATE SALE SET SALE_STOCKNAME = '{self.STOCKNAME.get()}', Make = '{self.Make.get()}', ModelNo_NO = '{self.ModelNo.get()}', Year = '{self.Year.get()}', TotalCost = '{self.TotalCost.get()}', ID_PROOF_TYPE = '{self.PurchaseCost.get()}', ID_NUMBER = '{self.SalePrice.get()}', Profit = '{self.Profit.get()}' WHERE StockNo_NO = {self.StockNo.get()}"
            query = f"UPDATE STOCK SET STOCKNAME = '{self.STOCKNAME.get().upper()}' WHERE STOCKNO = '{self.StockNo.get()}'"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.Fetch()
            self.Clear()
            tmsg.showinfo("Updated", "Stock Updated Successfully")
        except Exception as e:
            tmsg.showerror("Update Error", f"No Stock Is Selected In The Field For Updating Or Error Due To {e}")

    def Search(self):
        try:
            connection = self.getConnection()
            # query = "SELECT STOCKNO, TO_CHAR(STOCKNAME, 'DD-MM-YYYY') AS STOCKNAME, MAKE, ModelNo, YEAR, TOTALCOST, PURCHASECOST, SALEPRICE, PROFIT, PAYMENTTYPE, TITLE, TAGS, CLIENTID FROM SALE WHERE " + str(self.searchby.get()) + " = '" + str(self.search.get()).upper() + "'"
            query = "SELECT * FROM STOCK WHERE " + str(self.searchby.get()) + " = '" + str(self.search.get()).upper() + "'"
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
    stock = Stock(root)
    root.mainloop()