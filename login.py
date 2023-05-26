from tkinter import *
from PIL import Image, ImageTk
import cx_Oracle
import tkinter.messagebox as tmsg
from Account import Account
from main import Main
from threading import Thread
import pyttsx3
import ctypes

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500+400+100")
        self.root.resizable(False, False)
        self.root.title("Login")
        self.c = 0
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default='media/logo.ico')
        img1 = Image.open("Images/Dealership.jpg")
        img1 = img1.resize((500, 500), Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        img1 = Label(self.root, image=self.img1)
        img1.place(x=0, y=0)
        frame1 = Frame(self.root, bg="Cyan", bd=5, relief=SUNKEN)
        frame1.place(x=50, y=50, width=400, height=410)
        self.label = Label(frame1, text = "Enter Login Details", bg="Cyan", font="Courier 20 bold underline")
        self.MovingText()
        # self.label.place(x = 110, y = 20)
        self.label.pack(side=TOP, pady=20, padx = 30)
        img2 = Image.open("Images/user.jpg")
        img2 = img2.resize((30, 30), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        img2 = Label(frame1, image=self.img2)
        img2.place(x=10, y=95)
        Label(frame1, text="User Name", bg="Cyan", fg="Red", font="Helvatica 12 bold").place(x=50, y=100)
        self.UserName = StringVar()
        self.PassWord = StringVar()
        Entry(frame1, textvariable=self.UserName, font="Helvatica 12 bold", fg='Blue').place(x=170, y=100)
        img3 = Image.open("Images/password.jpg")
        img3 = img3.resize((30, 30), Image.Resampling.LANCZOS)
        self.img3 = ImageTk.PhotoImage(img3)
        img3 = Label(frame1, image=self.img3)
        img3.place(x=10, y=165)
        Label(frame1, text="Password", bg="Cyan", fg="Red", font="Helvatica 12 bold").place(x=50, y=170)
        Entry(frame1, textvariable=self.PassWord, font="Helvatica 12 bold", fg='Blue').place(x=170, y=170)
        Button(frame1, text="Reset Password", font="Arial 13 bold", bg="Maroon", fg="Cyan", cursor = "hand2", command=self.Reset).place(x=5, y=240, width=385)
        Button(frame1, text="Clear Now", font="Arial 13 bold", bg="Green", fg="Cyan", cursor = "hand2", command=self.Clear).place(x=5, y=280, width=385)
        # Button(frame1, text = "Create New Account", font = "Arial 13 bold", bg = "Blue", fg = "Cyan", command = self.newAccount).place(x = 5, y = 300, width = 190)
        # Button(frame1, text = "Login Now", font = "Arial 13 bold", bg = "Blue", fg = "Cyan", command = self.Logged).place(x = 200, y = 300, width = 190)
        Button(frame1, text="Login Now", font="Arial 13 bold", bg="Blue", fg="Cyan", cursor = "hand2", command=self.Logged).place(x=5, y=320, width=385)
        Button(frame1, text="Exit", font="Arial 13 bold", bg="Red", fg="Yellow", cursor = "hand2", command=self.loggedOut).place(x=5, y=360, width=385)
        self.CreatingTable()

    def MovingText(self):
        colors = ['Red', 'Blue', 'Purple', 'Orange', 'Green', 'Maroon']
        if self.c >= len(colors):
            self.c = 0
        self.label.config(fg=f"{colors[self.c]}")
        self.c += 1
        self.label.after(500, self.MovingText)

    def Clear(self):
        self.UserName.set("")
        self.PassWord.set("")

    def loggedOut(self):
        self.root.destroy()

    def Logged(self):
        try:
            a = str(self.UserName.get().upper())
            b = str(self.PassWord.get())
            connection = self.Connection()
            cursor = connection.cursor()
            query = "SELECT * FROM LOGIN"
            cursor.execute(query)
            row = cursor.fetchall()
            print(row)
            for rows, rows1 in row:
                if a == rows and b == (rows1):
                    self.Clear()
                    # self.threading()
                    self.root.state("iconic")
                    self.mainWindow()
                    # self.root.state('withdrawn')
                    if Main.Bye is False:
                        self.root.destroy()
                    break
                else:
                    tmsg.showerror("Error", "Invalid UserName Or Password")

            connection.commit()
            cursor.close()
        except Exception as es:
            tmsg.showerror("Error", f"Error due to {es}")

    def Reset(self):
        self.newwindow = Toplevel(self.root)
        self.account = Account(self.newwindow)

    def Connection(self):
        connection = cx_Oracle.connect("system/Reem2009!@localhost:1521/orcl")
        return connection

    def threading(self):
        self.x = Thread(target=self.talking)
        # self.x.start()

    def talking(self):
        engine = pyttsx3.init()
        text = "You Have Successfully Logged In"
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 200)
        engine.say(text)
        engine.runAndWait()

    def mainWindow(self):
        self.newwindow1 = Toplevel(self.root)
        self.threading()
        self.main = Main(self.newwindow1)
        self.x.start()

    def getConnection(self):
        connection = cx_Oracle.connect("system/Reem2009!@localhost:1521/orcl")
        return connection

    def CreatingTable(self):
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            query = """
                    CREATE TABLE CLIENT
                    (
                    IDNUMBER VARCHAR2(50),
                    FIRSTNAME VARCHAR2(60),
                    LASTNAME VARCHAR2(70),
                    CITY VARCHAR2(30),
                    STATE VARCHAR2(15),
                    ZIPCODE VARCHAR2(20),
                    PHONENO VARCHAR2(20),
                    ADDRESS VARCHAR2(100),
                    CONSTRAINTS CLIENT_PK PRIMARY KEY (IDNUMBER)
                    )
                    """
            cursor.execute(query)
            connection.commit()
            cursor.close()
            tmsg.showinfo("Good Job", "Client Database Created Successfully")
        except Exception as e:
            pass

            #########################################
        try:
            connection1 = self.getConnection()
            cursor1 = connection.cursor()
            query1 = """
                    CREATE TABLE STOCK
                    (
                    STOCKNO VARCHAR2(60),
                    STOCKNAME VARCHAR2(100),
                    CONSTRAINTS STOCK_PK PRIMARY KEY (STOCKNO)
                    )
                    """
            cursor1.execute(query1)
            connection1.commit()
            cursor1.close()
            tmsg.showinfo("Good Job", "Stock Database Created Successfully")
        except Exception as e:
            pass

            #########################################################

        try:
            connection2 = self.getConnection()
            cursor2 = connection.cursor()
            query2 = """
                    CREATE TABLE PURCHASE
                    (
                    PURCHASEDATE DATE,
                    STOCKNO VARCHAR2(60),
                    MAKE VARCHAR2(30),
                    MODEL VARCHAR2(30),
                    PYEAR VARCHAR2(4),
                    VINNO VARCHAR2(60),
                    MILLAGE VARCHAR2(60),
                    PURCHASEPRICE VARCHAR2(60),
                    TITLE INT CHECK (TITLE IN (0, 1)),
                    BILLOFSALE INT CHECK (BILLOFSALE IN (0, 1)),
                    REMARK VARCHAR2(30),
                    CARLOCATION VARCHAR2(50),
                    PROBLEM1 VARCHAR2(50) DEFAULT 'NONE',
                    PROBLEM2 VARCHAR2(50) DEFAULT 'NONE',
                    PROBLEM3 VARCHAR2(50) DEFAULT 'NONE',
                    CLIENTID VARCHAR2(50),
                    CONSTRAINTS PURCHASE_PK PRIMARY KEY (STOCKNO, PURCHASEDATE, CLIENTID),
                    CONSTRAINTS PURCHASE_FK FOREIGN KEY (CLIENTID) REFERENCES CLIENT (IDNUMBER),
                    CONSTRAINTS PURCHASE_FK1 FOREIGN KEY (STOCKNO) REFERENCES STOCK(STOCKNO)
                    )
                    """
            cursor2.execute(query2)
            connection2.commit()
            cursor2.close()
            tmsg.showinfo("Good Job", "Purchase Database Created Successfully")
        except Exception as e:
            pass

            #################################################################

        try:
            connection3 = self.getConnection()
            cursor3 = connection.cursor()
            query3 = """
                    CREATE TABLE SALE
                    (
                    STOCKNO VARCHAR2(60),
                    SALEDATE DATE,
                    MAKE VARCHAR2(30),
                    MODELNO VARCHAR2(20),
                    YEAR VARCHAR2(4),
                    TOTALCOST VARCHAR2(60),
                    PURCHASECOST VARCHAR2(60),
                    SALEPRICE VARCHAR2(60),
                    PROFIT VARCHAR2(60),
                    PAYMENTTYPE VARCHAR2(20),
                    TITLE INT CHECK (TITLE IN (0, 1)),
                    TAGS INT CHECK (TAGS IN (0, 1)),
                    CLIENTID VARCHAR2(50),
                    CONSTRAINTS SALE_PK PRIMARY KEY (STOCKNO, CLIENTID, SALEDATE),
                    CONSTRAINTS SALE_FK FOREIGN KEY (CLIENTID) REFERENCES CLIENT (IDNUMBER),
                    CONSTRAINTS SALE_FK1 FOREIGN KEY (STOCKNO) REFERENCES STOCK (STOCKNO)
                    )
                    """
            cursor3.execute(query3)
            connection3.commit()
            cursor3.close()
            tmsg.showinfo("Good Job", "Sale Database Created Successfully")
        except Exception as e:
            pass

            ##############################################################

        try:
            connection4 = self.getConnection()
            cursor4 = connection.cursor()
            query4 = """
                    CREATE TABLE DEALER
                    (
                    DEALERID VARCHAR2(50),
                    EXPENSEDATE DATE,
                    EXPENSETYPE VARCHAR2(20),
                    AMOUNT VARCHAR2(60),
                    PAYMENTTYPE VARCHAR2(20),
                    REMARK VARCHAR2(50),
                    CONSTRAINTS DEALER_PK PRIMARY KEY (DEALERID, EXPENSEDATE, REMARK)
                    )
                    """
            cursor4.execute(query4)
            connection4.commit()
            cursor4.close()
            tmsg.showinfo("Good Job", "Dealer Database Created Successfully")
        except Exception as e:
            pass

            ############################################################

        try:
            connection5 = self.getConnection()
            cursor5 = connection.cursor()
            query5 = """
                    CREATE TABLE MAKEE
                    (
                    MAKE VARCHAR2(100)
                    )
                    """
            cursor5.execute(query5)
            connection5.commit()
            cursor5.close()
            make = ['Acura', 'Chevy', 'Chrysler', 'Dodge', 'Ford', 'GMC', 'Honda', 'Mazda', 'Mitsubishi', 'Saturn', 'Toyota']
            connection51 = cx_Oracle.connect('system/Reem2009!@localhost:1521/orcl')
            cursor51 = connection51.cursor()
            for i in make:
                query51 = f"INSERT INTO MAKEE (MAKE) VALUES ('{i}')"
                cursor51.execute(query51)
            connection51.commit()
            cursor51.close()
            tmsg.showinfo("Good Job", "Make Database Created Successfully")
        except Exception as e:
            pass

            ##########################################################

        try:
            connection6 = self.getConnection()
            cursor6 = connection.cursor()
            query6 = """
                    CREATE TABLE MODELL
                    (
                    MODEL VARCHAR2(100)
                    )
                    """
            cursor6.execute(query6)
            connection6.commit()
            cursor6.close()
            model = ['Explorer', 'Expedition', 'VUE', 'MDX', 'Fusion', 'Corolla', 'Montero', 'Acadia', 'Captiva','Element', 'CX-9']
            connection61 = cx_Oracle.connect('system/Reem2009!@localhost:1521/orcl')
            cursor61 = connection61.cursor()
            for i in model:
                query61 = f"INSERT INTO MODELL (MODEL) VALUES ('{i}')"
                cursor61.execute(query61)
            connection61.commit()
            cursor61.close()
            tmsg.showinfo("Good Job", "Model Database Created Successfully")
        except Exception as e:
            pass

            #############################################################

        try:
            connection6 = self.getConnection()
            cursor6 = connection.cursor()
            query6 = """
                    CREATE TABLE LOGIN(
                    USERNAME VARCHAR2(100),
                    PASSWORD VARCHAR2(100),
                    CONSTRAINTS LOGIN_PK PRIMARY KEY (USERNAME)
                    )
                    """
            cursor6.execute(query6)
            connection6.commit()
            cursor6.close()
            connection7 = self.getConnection()
            cursor7 = connection7.cursor()
            query7 = "INSERT INTO LOGIN (USERNAME, PASSWORD) VALUES ('SYSTEM', '@System')"
            cursor7.execute(query7)
            connection7.commit()
            cursor7.close()
            tmsg.showinfo("Good Job", "Login Database Created Successfully")
        except Exception as e:
            pass


if __name__ == '__main__':
    root = Tk()
    login = Login(root)
    root.mainloop()