# import tkinter
# import cx_Oracle
# root = tkinter.Tk()
# screenWidth = root.winfo_screenwidth()
# screenHeight = root.winfo_screenheight()
# root.geometry('850x550')
# root.minsize(850, 550)
# root.maxsize(850, 550)
# try:
#     con = cx_Oracle.connect("system/Reem2009!@localhost:1521/orcl")
#     cur = con.cursor()
#     query = "DROP TABLE PURCHASE"
#     cur.execute(query)
#     con.commit()
#     cur.close()
#     tkinter.Label(root, text = f"Purchase Altered", font = "Courier 30 bold", fg = "Blue").pack(pady = 50)
# except:
#     pass
# tkinter.Label(root, text = f"The Screen Width Is --> {screenWidth}", font = "Courier 30 bold", fg = "Blue").pack(pady = 50)
# tkinter.Label(root, text = f"The Screen Height Is --> {screenHeight}", font = "Courier 30 bold", fg = "Blue").pack(pady = 50)
# tkinter.Label(root, text = f"{screenWidth} X {screenHeight}", font = "Courier 30 bold", fg = "Blue").pack(pady = 50)
# root.mainloop()


import pyttsx3
engine = pyttsx3.init()
text = "ہیلو آپ کیسے ہیں؟"
print(text)
text1 = "Hello how are you?"
engine.say(text)
engine.say(text1)
print("Ok")
engine.runAndWait()
