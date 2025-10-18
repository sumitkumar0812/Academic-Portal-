from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
import random
import datetime
from tkinter import messagebox


top = Tk()
top.title("Welcome")
top.geometry('1400x700')

def ShowPassword():
    if E3.cget('show')=="*":
        E3.config(show="")
    else:
        E3.config(show="*")

def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    cur.execute("select * from admin where name=%s and password=%s",(E2.get(),E3.get()))
    result =cur.fetchone()
    if result == None:
        messagebox.showinfo("Result",'Login fail')
    else:
        top.destroy()
        import home


img=ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\Blue and White Illustration Sea Desktop Wallpaper.png")
l=Label(top,image=img)
l.pack()

l = Label(top, text='Welcome Students Portal', bg='black', fg='white', font=('Arial 25 bold'))
l.place(x=450 ,y=30)


l3 = Label(top, text='Name', bg='black', fg='white', font=('Arial 20 bold'))
l3.place(x=200, y=150)

E2 = Entry(top, font=('Arial 20 bold'))
E2.place(x=350, y=150)

l4 = Label(top, text='Password', bg='black', fg='white', font=('Arial 20 bold'))
l4.place(x=200, y=200)

E3 = Entry(top, font=('Arial 20 bold'),show='*')
E3.place(x=350, y=200)


B2 = Button(top, text='Login', font=('Arial 20 bold'),command=Login)
B2.place(x=350, y=250)

c=Checkbutton(top,command=ShowPassword)
c.place(x=670,y=210)

top.config(bg='grey')
top.mainloop()
