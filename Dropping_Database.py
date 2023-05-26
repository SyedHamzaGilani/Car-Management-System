import tkinter.messagebox

import cx_Oracle
import tkinter
root = tkinter.Tk()

def dropping(event):
    connection = cx_Oracle.connect("system/Reem2009!@localhost:1521/orcl")
    cursor = connection.cursor()
    # try:
        #
        # cursor.execute(query)
        # connection.commit()
        # cursor.close()
        # tkinter.messagebox.showinfo("Good Job", "MAKEE Database Dropped Successfully!")
    # except:
    #     pass
    # try:
        #
        # cursor.execute(query)
        # connection.commit()
        # cursor.close()
        # tkinter.messagebox.showinfo("Good Job", "MODELL Database Dropped Successfully!")
    # except:
    #     pass
    # try:
        #
        # cursor.execute(query)
        # connection.commit()
        # cursor.close()
        # tkinter.messagebox.showinfo("Good Job", "DEALER Database Dropped Successfully!")
    # except:
    #     pass
    # try:
        #
        # cursor.execute(query)
        # connection.commit()
        # cursor.close()
        # tkinter.messagebox.showinfo("Good Job", "PURCHASE Database Dropped Successfully!")
    # except:
    #     pass
    # try:
        #
        # cursor.execute(query)
        # connection.commit()
        # cursor.close()
        # tkinter.messagebox.showinfo("Good Job", "SALE Database Dropped Successfully!")
    # except:
    #     pass
    # try:
        #
        # cursor.execute(query)
        # connection.commit()
        # cursor.close()
        # tkinter.messagebox.showinfo("Good Job", "STOCK Database Dropped Successfully!")
    # except:
    #     pass
    # try:
        #
        # cursor.execute(query)
        # connection.commit()
        # cursor.close()
        # tkinter.messagebox.showinfo("Good Job", "CLIENT Database Dropped Successfully!")
    # except:
    #     pass
    try:
        query1 = "DROP TABLE MAKEE"
        query2 = "DROP TABLE MODELL"
        query3 = "DROP TABLE DEALER"
        query4 = "DROP TABLE PURCHASE"
        query5 = "DROP TABLE SALE"
        query6= "DROP TABLE STOCK"
        query7 = "DROP TABLE CLIENT"
        query8 = "DROP TABLE LOGIN"
        cursor.execute(query1)
        cursor.execute(query2)
        cursor.execute(query3)
        cursor.execute(query4)
        cursor.execute(query5)
        cursor.execute(query6)
        cursor.execute(query7)
        cursor.execute(query8)
        connection.commit()
        cursor.close()
        tkinter.messagebox.showinfo("Good Job", "All Databases Dropped Successfully!")
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"Database Does Not Exist, Error Due To {e}")

root.geometry("500x500")
tkinter.Label(root, text = "Press Enter To Drop Databases", fg = "Blue", bg = "Cyan", font = "Courier 20 bold").pack(pady = 200)
root.bind('<Return>', dropping)
root.config(bg = "Cyan")
root.mainloop()
