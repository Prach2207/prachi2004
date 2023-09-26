from tkinter import *
from tkinter import messagebox
import mysql.connector

def viewmem():

    global id

    window=Tk()
    window.title('Library Management System')

    greet = Label(window, font = ('arial', 30, 'bold'), text = "View Members")
    greet.grid(row = 0,columnspan = 3)

    db = mysql.connector.connect(host ="localhost",user = "root",password = 'password',database='library')
    cursor = db.cursor()

    sqlquery= "select * from member ;"
    print(sqlquery)

    try:
        
        cursor.execute(sqlquery)
        
        # db.commit()
        L = Label(window, font = ('arial', 20), text = "%-10s%-20s%-20s%-20s"%('MID','Name','Age','Number' ))
        L.grid(row = 1,columnspan = 4)

        L = Label(window, font = ('arial', 20), text = "--------------------------------------------------------------------------------")
        L.grid(row = 2,columnspan = 4)

        x=4
        for i in cursor:
            L = Label(window, font = ('arial', 15), text = "%-10s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3]))
            L.grid(row = x,columnspan = 4)
            x+=1   

    except:
        messagebox.showinfo("Error","Cannot Fetch data.")
    
    print("view")
    pass