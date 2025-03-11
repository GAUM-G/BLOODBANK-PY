# importing modules
from tkinter import *
import mysql.connector
from tkinter import messagebox  # for pops and dialog box

# setting database connection
db = mysql.connector.connect(host="localhost", user="root", password='root', database='db')
cursor = db.cursor()  # points towards db database

# declaring main project window for Python Blood Bank Management System
window = Tk()
window.title("Blood Bank Management System")
window.iconbitmap('C:\\Users\\Dell\\OneDrive\\Desktop\\PROJECTS\SEM3\\Python\\OIP.ico')
window.resizable(0, 0)

# Label is a widget in tkinter that implements display box where we can place text
greet = Label(window, font=('arial', 20, 'bold'), text="BloodBank", bg="blue", fg="white", padx=10, pady=10, bd=5)
greet.grid(row=0, columnspan=5)

# function that alters the database and increases the units of the blood group
def Donate_dbase():
    global bgrp
    global bunits
    units = bunits.get()
    try:
        # setting database connection
        dbase = mysql.connector.connect(host="localhost", user="root", password='root', database='db')
        cursor = dbase.cursor()
        # storing sql query in a variable named sqlquery
        sqlquery = "SELECT units FROM BloodBank WHERE Blood_Grp=%s"
        cursor.execute(sqlquery, (bgrp,))
        for i in cursor:
            # units holds the increased amount of the blood group
            units = str(int(i[0]) + int(units))
        # sql query to update the units of blood group
        sqlquery = "UPDATE BloodBank SET units=%s WHERE Blood_Grp=%s"
        cursor.execute(sqlquery, (units, bgrp))
        # saving the changes in the database
        dbase.commit()
        # displaying the message box showing "Blood Donated Successfully"
        messagebox.showinfo('Success', "Blood Donated Successfully")
    except mysql.connector.Error as err:
        messagebox.showinfo("Error", f"Cannot access Database: {err}")
    finally:
        cursor.close()
        dbase.close()


# method to ask the units of blood that the user wants to donate
def donate(*args, **kwargs):
    global bgrp
    global bunits
    bgrp = args[0]
    # initializing a separate tkinter window
    donate_window = Tk()
    donate_window.title('Blood Donation Management System')
    donate_window.resizable(0, 0)
    # displaying message "Donate Blood"
    greet = Label(donate_window, font=('arial', 20, 'bold'), text="Donate Blood")
    greet.grid(row=0, columnspan=3)
    # ----------bunits------------------
    L = Label(donate_window, font=('arial', 10, 'bold'), text="Enter No. of Units: ")
    L.grid(row=4, column=1)
    L = Label(donate_window, font=('arial', 10, 'bold'), text="   ")
    L.grid(row=4, column=2)
    bunits = Entry(donate_window, width=5, font=('arial', 10))
    bunits.grid(row=4, column=3)
    # creating a submit button to donate the blood
    submitbtn = Button(donate_window, text="Submit", command=Donate_dbase, bg="Firebrick", fg="white", font=('arial', 10))
    submitbtn.grid(row=8, columnspan=3)


# method that alters the database and decreases the units of the blood group if the requested amount is available
def Request_dbase():
    global bgrp
    global bunits
    units = bunits.get()
    try:
        # setting database connection
        dbase = mysql.connector.connect(host="localhost", user="root", password='root', database='db')
        cursor = dbase.cursor()
        # storing sql query in a variable named sqlquery
        sqlquery = "SELECT units FROM BloodBank WHERE Blood_Grp=%s"
        cursor.execute(sqlquery, (bgrp,))
        for i in cursor:
            if int(i[0]) >= int(units):
                # units holds the updated amount of blood
                units = str(int(i[0]) - int(units))
                # sql query to update the units of blood group
                sqlquery = "UPDATE BloodBank SET units=%s WHERE Blood_Grp=%s"
                cursor.execute(sqlquery, (units, bgrp))
                # committing the changes in the database
                dbase.commit()
                # displaying the message box showing "Blood Request Successfully"
                messagebox.showinfo('Success', "Blood Request Successful")
            else:
                messagebox.showinfo("Not Available", "Enter less unit")
    except mysql.connector.Error as err:
        messagebox.showinfo("Not Available", f"Cannot access Database: {err}")
    finally:
        cursor.close()
        dbase.close()


# method to ask the units of blood that the user wants
def request(*args, **kwargs):
    global bgrp
    global bunits
    bgrp = args[0]
    # initializing a separate tkinter window
    request_window = Tk()
    request_window.title('Blood Donation Management System')
    request_window.resizable(0, 0)
    # displaying message "Request Blood"
    greet = Label(request_window, font=('arial', 20, 'bold'), text="Request Blood")
    greet.grid(row=0, columnspan=3)
    # ----------bunits------------------
    L = Label(request_window, font=('arial', 10, 'bold'), text="Enter Units Required: ")
    L.grid(row=4, column=1)
    L = Label(request_window, font=('arial', 10, 'bold'), text="   ")
    L.grid(row=4, column=2)
    bunits = Entry(request_window, width=5, font=('arial', 10))
    bunits.grid(row=4, column=3)
    # creating a submit button to request the blood
    submitbtn = Button(request_window, text="Submit", command=Request_dbase, bg="Firebrick", fg="white", font=('arial', 10))
    submitbtn.grid(row=8, columnspan=3)


# displaying all the records of the bloodbank table
sqlquery = "SELECT * FROM BloodBank"

try:
    cursor.execute(sqlquery)
    # displaying the table head
    L = Label(window, font=('arial', 12, 'bold'), text="Blood group", padx=20, pady=10)
    L.grid(row=1, column=1)  # Blood group label
    L = Label(window, font=('arial', 12, 'bold'), text="Units", padx=20, pady=10)
    L.grid(row=1, column=2)  # Units label
    x = 2  # Start from row 2
    for i in cursor:
        L = Label(window, font=('arial', 10), text=i[0])
        L.grid(row=x, column=1, padx=20, pady=5)  # Blood group center align
        L = Label(window, font=('arial', 10), text=i[1])
        L.grid(row=x, column=2, padx=20, pady=5)  # Units center align
        # creating buttons for donating and requesting blood
        d = Button(window, text="Donate", command=lambda arg=i[0], kw="donate": donate(arg, o1=kw),
                   padx=10, pady=10, bg="Firebrick", fg="white", font=('arial', 10))
        d.grid(row=x, column=3)
        r = Button(window, text="Request", command=lambda arg=i[0], kw="request": request(arg, o1=kw),
                   padx=10, pady=10, bg="firebrick", fg="white", font=('arial', 10))
        r.grid(row=x, column=4)
        x += 1  # Move to next row for next record
except mysql.connector.Error as err:
    messagebox.showinfo("Error", f"Cannot Fetch data: {err}")
finally:
    cursor.close()
    db.close()

# end tkinter loop
window.mainloop()
