import calendar
import random
import tkinter as tk
from threading import Thread
import ctypes
import pyttsx3
from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import time
from CalWindow import calWindow
import tkinter.messagebox as tmsg
from PurchaseWindow import Purchase
from StockWindow import Stock
from ClientWindow import Client
from SaleWindow import Sale
from DealerWindow import Dealer
from ReportWindow import Report
from SettingWindow import Setting
class Main:
    def __init__(self, root):
        self.root = root
        self.count = 0
        self.words = ""
        self.bg = 0
        self.pg = 0
        self.i = 0
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        self.root.state('zoomed')
        self.root.title("Cars Management System")
        # self.root.state("zoomed")
        self.root.geometry(f"{screenWidth}x{screenHeight}")
        self.root.minsize(screenWidth, screenHeight)
        myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.root.iconbitmap(default= 'media/logo.ico')
        # self.changebg()
        self.root.config(bg = "Blue")
        img1 = Image.open("Images/car3.jpg")
        img1 = img1.resize((730, 140), Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)
        img1 = Label(self.root, image = self.img1)
        # img1.place(x = 317, y = 5)
        img2 = Image.open("Images/Dealership.jpg")
        img2 = img2.resize((300, 140), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(img2)
        img2 = Label(self.root, image = self.img2)
        img2.place(x = 5, y = 5)
        img3 = Image.open("Images/Dealership.jpg")
        img3 = img3.resize((300, 140), Image.Resampling.LANCZOS)
        self.img3 = ImageTk.PhotoImage(img3)
        img3 = Label(self.root, image = self.img3)
        img3.place(x = 1057, y = 5)

        img = Image.open("Images/source.jpg")
        img = img.resize((735, 140), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        img = Label(self.root, image = self.img)
        img.place(x = 313, y = 5)

        #######################################################

        self.frame1 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame1.place(x = 5, y = 155, width = 1354, height = 45)
        self.text = Label(self.frame1, font = "Courier 18 bold underline", bg = "Cyan")
        self.MoveText()
        self.text.pack()

        #######################################################

        self.frame2 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame2.place(x = 5, y = 207, width = 350, height = 480)
        # Label(self.frame2, text = "<< Options >>", font = "Conicsansms 20 bold underline", bd = 5, relief = SUNKEN, fg = "Blue", bg = "Cyan").pack(fill = X, padx = 5, pady = 10)
        Button(self.frame2, text = "Stock Info", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Stock).pack(fill = X, padx = 5, pady = 5)
        Button(self.frame2, text = "Client Info", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Client).pack(fill = X, padx = 5, pady = 5)
        Button(self.frame2, text = "Purchase", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Purchase).pack(fill = X, padx = 5, pady = 5)
        Button(self.frame2, text = "Sale", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Sale).pack(fill = X, padx = 5, pady = 5)
        Button(self.frame2, text = "Dealer Expenses", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Dealer).pack(fill = X, padx = 5, pady = 5)
        Button(self.frame2, text = "Report", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Report).pack(fill = X, padx = 5, pady = 5)
        Button(self.frame2, text = "Setting", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Setting).pack(fill = X, padx = 5, pady = 5)
        Button(self.frame2, text = "Log Out", font = "Conicsansms 16 bold", bd = 5, relief = SUNKEN, fg = "Cyan", bg = "Blue", cursor = "hand2", command = self.Bye).pack(fill = X, padx = 5, pady = 5)
        # f2img = Image.open("Images/4.jpg")
        # f2img = f2img.resize((345, 200), Image.ANTIALIAS)
        # self.f2img = ImageTk.PhotoImage(f2img)
        # Label(self.frame2, image = self.f2img, bd = 5, relief = SUNKEN).pack(fill = X, padx = 5, pady = 2)
        self.changebg()

        #######################################################

        self.frame3 = Frame(self.root, bg = "Cyan", bd = 5, relief = SUNKEN)
        self.frame3.place(x = 365, y = 207, width = 995, height = 480)
        f3img = Image.open("Images/car4.jpg")
        f3img = f3img.resize((990, 475), Image.Resampling.LANCZOS)
        self.f3img = ImageTk.PhotoImage(f3img)
        self.changeingImages = Label(self.frame3, image = self.f3img)
        # self.TransitionsImages()
        self.changeingImages.pack()

        #######################################################

        self.frame4 = Frame(self.root, bg = 'Cyan', bd = 5, relief = SUNKEN)
        # self.frame4.pack(side = BOTTOM, anchor = SW, fill = X, padx = 5, pady = 10)
        self.frame4.place(x = 5, y = 690, width = screenWidth)
        Button(self.frame4, text = "SHOW CALANDER", fg = "Cyan", bg = "Blue",font = "Conicsansms 8 bold", bd = 4, relief = SUNKEN, cursor = "hand2", command = self.showCal).place(x = 1190, y = 2, width = 150)
        self.timestatus = Label(self.frame4, font = "Conicsansms 14 bold", bg = "Cyan", fg = "Blue")
        self.Clock()
        self.timestatus.pack()

        #######################################################

    def showCal(self):
        self.calWindow = Toplevel(self.root)
        self.cal = calWindow(self.calWindow)


    def changebg(self):
        # colors = ['Red', 'Blue', 'Purple', 'Orange', 'Green', 'Maroon']
        colors = ['Pink', 'Orange', 'Grey', 'white']
        colors = ['Black', 'White', 'Grey']
        colors = ['Red', 'Blue', 'Purple', 'Black','Hot Pink', 'Green', 'Maroon']
        # color = random.choice(colors)
        if self.bg >= len(colors):
            self.bg = 0
        self.frame2.config(bg=f"{colors[self.bg]}")
        self.bg += 1
        self.frame2.after(3900, self.changebg)


    def TransitionsImages(self):
        images = ['Images/Dealership.jpg', 'Images/car1.jpg', 'Images/car2.jpg', 'Images/car3.jpg', 'Images/car4.jpg', 'Images/car5.jpg', 'Images/car6.jpg', 'Images/car7.jpg', "Images/15.jpg", 'Images/source.jpg', 'Images/car8.jpg', 'Images/car9.jpg', 'Images/car10.jpg', 'Images/car11.jpg', 'Images/car12.jpg', 'Images/car13.jpg', 'Images/car14.jpg', 'Images/car15.jpg', ]
        if self.pg >= len(images):
            self.pg = 0
        f3img = Image.open(f"{images[self.pg]}")
        f3img = f3img.resize((990, 475), Image.Resampling.LANCZOS)
        self.f31img = ImageTk.PhotoImage(f3img)
        self.changeingImages.config(image = self.f31img)
        self.pg += 1


    def MoveText(self):
        t1 = "Welcome To Car Business"
        if self.count >= len(t1):
            self.count = 0
            self.words = ""
            self.i += 1
            self.TransitionsImages()
        self.words += t1[self.count]
        self.count += 1
        # colors = ['red', 'green', 'orange', 'Cyan', 'blue', 'maroon', 'purple']
        colors = ['Red', 'Blue', 'Purple', 'Black', 'Hot Pink', 'Green', 'Maroon']
        if self.i >= len(colors):
            self.i = 0
        color = random.choice(colors)
        self.text.config(text = self.words, fg = f"{colors[self.i]}")
        self.text.after(200, self.MoveText)

    def Clock(self):
        today = date.today()
        today = today.strftime("%d / %B / %Y")
        string = time.strftime(f"%I : %M : %S  %p (%A)  -  {today}")
        self.timestatus.config(text = string)
        self.timestatus.after(1000, self.Clock)

    def threading(self):
        self.x = Thread(target=self.talking)
        # self.x.start()

    def talking(self):
        engine = pyttsx3.init()
        text = "Thanks For Using Our Software, Good Bye, Take Care, See You Soon."

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()

    def Bye(self):
        self.root.destroy()
        self.threading()
        self.x.start()
        return True

    def Stock(self):
        try:
            self.newwindow6.destroy()
        except:
            pass
        self.newwindow6 = Toplevel(self.root)
        # self.voice("Customer Window is Appearing Now")
        self.stock = Stock(self.newwindow6)
        try:
            self.newwindow.destroy()
        except:
            pass
        try:
            self.newwindow1.destroy()
        except:
            pass
        try:
            self.newwindow2.destroy()
        except:
            pass
        try:
            self.newwindow3.destroy()
        except:
            pass
        try:
            self.newwindow4.destroy()
        except:
            pass
        try:
            self.newwindow5.destroy()
        except:
            pass
    def Client(self):
        try:
            self.newwindow.destroy()
        except:
            pass
        self.newwindow = Toplevel(self.root)
        # self.voice("Customer Window is Appearing Now")
        self.client = Client(self.newwindow)
        try:
            self.newwindow6.destroy()
        except:
            pass
        try:
            self.newwindow1.destroy()
        except:
            pass
        try:
            self.newwindow2.destroy()
        except:
            pass
        try:
            self.newwindow3.destroy()
        except:
            pass
        try:
            self.newwindow4.destroy()
        except:
            pass
        try:
            self.newwindow5.destroy()
        except:
            pass


    def Purchase(self):
        try:
            self.newwindow1.destroy()
        except:
            pass
        self.newwindow1 = Toplevel(self.root)
        # self.voice("Customer Window is Appearing Now")
        self.purchase = Purchase(self.newwindow1)
        try:
            self.newwindow6.destroy()
        except:
            pass
        try:
            self.newwindow.destroy()
        except:
            pass
        try:
            self.newwindow2.destroy()
        except:
            pass
        try:
            self.newwindow3.destroy()
        except:
            pass
        try:
            self.newwindow4.destroy()
        except:
            pass
        try:
            self.newwindow5.destroy()
        except:
            pass


    def Sale(self):
        try:
            self.newwindow2.destroy()
        except:
            pass
        self.newwindow2 = Toplevel(self.root)
        # self.voice("Room Window is Appearing Now")
        self.sale = Sale(self.newwindow2)
        try:
            self.newwindow6.destroy()
        except:
            pass
        try:
            self.newwindow1.destroy()
        except:
            pass
        try:
            self.newwindow.destroy()
        except:
            pass
        try:
            self.newwindow3.destroy()
        except:
            pass
        try:
            self.newwindow4.destroy()
        except:
            pass
        try:
            self.newwindow5.destroy()
        except:
            pass


    def Dealer(self):
        try:
            self.newwindow3.destroy()
        except:
            pass
        self.newwindow3 = Toplevel(self.root)
        # self.voice("Room Window is Appearing Now")
        self.dealer = Dealer(self.newwindow3)
        try:
            self.newwindow6.destroy()
        except:
            pass
        try:
            self.newwindow1.destroy()
        except:
            pass
        try:
            self.newwindow2.destroy()
        except:
            pass
        try:
            self.newwindow.destroy()
        except:
            pass
        try:
            self.newwindow4.destroy()
        except:
            pass
        try:
            self.newwindow5.destroy()
        except:
            pass

    def Report(self):
        try:
            self.newwindow4.destroy()
        except:
            pass
        self.newwindow4 = Toplevel(self.root)
        # self.voice("Room Window is Appearing Now")
        self.report = Report(self.newwindow4)
        try:
            self.newwindow1.destroy()
        except:
            pass
        try:
            self.newwindow2.destroy()
        except:
            pass
        try:
            self.newwindow3.destroy()
        except:
            pass
        try:
            self.newwindow.destroy()
        except:
            pass
        try:
            self.newwindow5.destroy()
        except:
            pass
        try:
            self.newwindow6.destroy()
        except:
            pass

    def Setting(self):
        try:
            self.newwindow5.destroy()
        except:
            pass
        self.newwindow5 = Toplevel(self.root)
        # self.voice("Room Window is Appearing Now")
        self.setting = Setting(self.newwindow5)
        try:
            self.newwindow1.destroy()
        except:
            pass
        try:
            self.newwindow2.destroy()
        except:
            pass
        try:
            self.newwindow3.destroy()
        except:
            pass
        try:
            self.newwindow.destroy()
        except:
            pass
        try:
            self.newwindow4.destroy()
        except:
            pass
        try:
            self.newwindow6.destroy()
        except:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    root.mainloop()