from tkinter import *
from PIL import Image ,ImageTk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import random
import datetime
from tkinter import messagebox
import pymysql as sql

top=Tk()
top.title("welcome")
top.geometry('1400x700')

def showcourse():
    h=[]
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    v="select coursename from coursefee"
    cur.execute(v)
    s2=cur.fetchall()
    for i in s2:
        n=i[0]
        h.append(n)
    return h
s=showcourse()


def login():
    top.destroy()
    import login

def insert():
    s=random.randint(1000,10000)
    k1=E3.get()
    k2=E4.get()
    k3=E5.get()
    k4=cb.get()
    format='%m/%d/%y'
    k6=cal.get()
    date=datetime.datetime.strptime(k6,format)
    n=date.strftime('%y-%m-%d')
    k7=var.get()
    k8=E9.get()
    format='%m/%d/%y'
    k9=cal2.get()
    date=datetime.datetime.strptime(k9,format)
    n2=date.strftime('%y-%m-%d')
    k10=E11.get()
    db=sql.connect(host='localhost', user='root',password='sumit081204',db='project3pm')
    cur=db.cursor()
    q="insert into student(Id,Name,Lastname,PhoneNo,Course,Dob,Gender,Email,RgDate,Address)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (s,k1,k2,k3,k4,n,k7,k8,n2,k10)
    result=cur.execute(q)
    if(result>0):
        messagebox.showinfo("Result","Record insert successfully")
    else:
        messagebox.showinfo("Result","Record not insert successfully")
    E2.delete(0,'end')
    E3.delete(0, 'end')
    E4.delete(0, 'end')
    E5.delete(0, 'end')
    E9.delete(0, 'end')
    E11.delete(0, 'end')
    cb.delete(0, 'end')

    db.commit()



img=ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\flat-lay-workstation-with-copy-space-laptop.jpg")
l=Label(top,image=img)
l.pack()

var=StringVar()


l1=Label(top,text="WELCOME TO STUDENTS PORTAL",bg='grey',fg='black', font=('Arial 30 bold'))
l1.place(x=300,y=30)

l2=Label(top, text='ID',bg='black',fg='white',font=('Arial 20 bold'))
l2.place(x=200,y=100)
E2=Entry(top,font='Arial 20 bold')
E2.place(x=400,y=100)

l3=Label(top, text='NAME',bg='black',fg='white',font=('Arial 20 bold'))
l3.place(x=200,y=150)
E3=Entry(top,font='Arial 20 bold')
E3.place(x=400,y=150)

l4=Label(top, text='LASTNAME',bg='black',fg='white',font=('Arial 20 bold'))
l4.place(x=200,y=200)
E4=Entry(top,font='Arial 20 bold')
E4.place(x=400,y=200)

l5=Label(top, text='PhoneNo',bg='black',fg='white',font=('Arial 20 bold'))
l5.place(x=200,y=250)
E5=Entry(top,font='Arial 20 bold')
E5.place(x=400,y=250)

l6=Label(top, text='COURSE',bg='black',fg='white',font=('Arial 20 bold'))
l6.place(x=200,y=300)
cb=ttk.Combobox(top,value=s ,font=('Arial 20 bold'))
cb.place(x=400 ,y=300)
cb.current(0)

l7=Label(top, text='DOB',bg='black',fg='white',font=('Arial 20 bold'))
l7.place(x=200,y=350)
cal=DateEntry(top,width=20,bg='darkblue',fg='white', year=2010, font=('Arial 20 bold'))
cal.place(x=400,y=350)

l8=Label(top, text='GENDER',bg='black',fg='white',font=('Arial 20 bold'))
l8.place(x=200,y=400)

r1=Radiobutton(top, text='Male', value='Male', variable=var, font=('Arial 20 bold'))
r1.place(x=400,y=400)

r1=Radiobutton(top, text='Female', value='Female', variable=var, font=('Arial 20 bold'))
r1.place(x=500,y=400)

r1=Radiobutton(top, text='Others', value='Others', variable=var, font=('Arial 20 bold'))
r1.place(x=640,y=400)

l9=Label(top, text='Email',bg='black',fg='white',font=('Arial 20 bold'))
l9.place(x=200,y=450)
E9=Entry(top,font='Arial 20 bold')
E9.place(x=400,y=450)

l10=Label(top, text='RgDate',bg='black',fg='white',font=('Arial 20 bold'))
l10.place(x=200,y=500)
cal2=DateEntry(top,width=20,bg='darkblue',fg='white', year=2010, font=('Arial 20 bold'))
cal2.place(x=400,y=500)

l11=Label(top, text='Address',bg='black',fg='white',font=('Arial 20 bold'))
l11.place(x=200,y=550)
E11=Entry(top,font='Arial 20 bold')
E11.place(x=400,y=550)

B1=Button(top,text='submit', font=('Arial 18 bold'),command=insert)
B1.place(x=400, y=593)

B1=Button(top,text='Login', font=('Arial 18 bold'),command=login)
B1.place(x=550, y=593)




top.config(bg='grey')
top.mainloop()