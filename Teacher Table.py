from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
import random
import datetime
from tkinter import messagebox
import pymysql as sql


top = Tk()
top.title("Welcome")
top.geometry('1400x700')

img=ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\Blue and White Illustration Sea Desktop Wallpaper.png")
l=Label(top,image=img)
l.pack()

def show():
    for i in tv.get_children():
        tv.delete(i)

    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    q = "select * from teacher"
    cur.execute(q)
    result = cur.fetchall()
    for col in result:
        id=col[0]
        name=col[0]
        course=col[2]
        exp=col[3]
        tv.insert("",'end',values=(id,name,course,exp))

tv = ttk.Treeview(top,height=15)
tv['columns']=('id','name','course','exp')
tv.column('#0', width=0, stretch=NO)
tv.column('id', anchor=CENTER, width=250)
tv.column('name', anchor=CENTER, width=250)
tv.column('course', anchor=CENTER, width=250)
tv.column('exp', anchor=CENTER, width=250)

tv.heading('id', text='id', anchor=CENTER)
tv.heading('name', text='name', anchor=CENTER)
tv.heading('course', text='course', anchor=CENTER)
tv.heading('exp', text='exp', anchor=CENTER)
tv.place(x=120,y=150)

B2 = Button(top, text='ShowData', font=('Arial 18 bold'),command=show)
B2.place(x=400, y=500)

top.mainloop()