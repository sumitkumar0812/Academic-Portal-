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


def showcourse():
    h = []
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    v = "select coursename from coursefee"
    cur.execute(v)
    s2 = cur.fetchall()
    for i in s2:
        n = i[0]
        h.append(n)
    return h


s = showcourse()


def show():
    for i in tv.get_children():
        tv.delete(i)

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    q="select * from student"
    cur.execute(q)
    result=cur.fetchall()
    for col in result:
        id=col[0]
        name=col[1]
        lastname=col[2]
        phoneno=col[3]
        course=col[4]
        dob=col[5]
        gender=col[6]
        Email=col[7]
        RgDate=col[8]
        Address=col[9]
        DepositeFee=col[10]
        PendingFee=col[11]
        DepositeDate=col[12]
        tv.insert("",'end',values=(id,name,lastname,phoneno,course,dob,gender,Email,RgDate,Address,DepositeFee,PendingFee,DepositeDate))

def Search():
    for i in tv.get_children():
        tv.delete(i)

    p=S1.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    q = "select * from student where name=%s or course=%s"
    t=(p,p)
    cur.execute(q,t)
    result = cur.fetchall()
    for col in result:
        id = col[0]
        name = col[1]
        lastname = col[2]
        phoneno = col[3]
        course = col[4]
        dob = col[5]
        gender = col[6]
        Email = col[7]
        RgDate = col[8]
        Address = col[9]
        DepositeFee=col[10]
        PendingFee=col[11]
        DepositeDate=col[12]
        tv.insert("", 'end', values=(id, name, lastname, phoneno, course, dob, gender, Email, RgDate, Address,DepositeFee,PendingFee,DepositeDate))

def Delete():
    p = S1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    q="delete from student where name=%s or course=%s "
    t=(p,p)
    result=cur.execute(q,p)
    if(result>0):
        messagebox.showinfo("Result","Record delete successfully")
    else:
        messagebox.showinfo("Result", "Record not delete ")
    db.commit()

def Update():
    id = S1.get()
    name=S10.get().strip() or None
    pn=S11.get().strip() or None


    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
    cur = db.cursor()
    v=(name,pn,id)
    q="update student set name=COALESCE(%s,name),phoneno=COALESCE(%s,phoneno) where id=%s"

    result = cur.execute(q,v)
    if (result > 0):
        messagebox.showinfo("Result", "Record update successfully")
    else:
        messagebox.showinfo("Result", "Record not update ")
    db.commit()

def UpdateFees():
    top2 = Toplevel(top)
    top2.geometry('900x600')
    img = ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\Blue and White Illustration Sea Desktop Wallpaper.png")

    L1 = Label(top2, image=img)
    L1.pack()

    def insertfee():
        r=[]
        name = E1.get()
        pn= E2.get()
        c = cb.get()
        fees = E3.get()
        format = '%m/%d/%y'
        k4 = cal.get()
        date = datetime.datetime.strptime(k4, format)
        n = date.strftime('%y-%m-%d')

        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
        cur = db.cursor()
        q ="select fee from coursefee where coursename =%s"
        cur.execute(q,c)
        result= cur.fetchone()
        t=result[0]
        print(t)

        cur2=db.cursor()
        q2="select pendingfee from student where phoneno=%s"
        cur2.execute(q2, pn)
        result2=cur2.fetchone()
        t2=result2[0]
        print(t2)

        cur3 = db.cursor()
        q3 = "select depositefee from student where phoneno=%s"
        cur3.execute(q3, pn)
        result3 = cur3.fetchone()
        t3 = result3[0]


        if t2 is not None:
            df2 = t3 + int(fees)
            pf2 = t2- int(fees)

            q4="update student set pendingfee=%s,depositefee=%s,DepositeDate=%s where phoneno=%s"
            b = (pf2, df2, n, pn)

            result3= cur.execute(q4,b)
            if (result3 >0):
                messagebox.showinfo("Result", " your Record update successfully")
            else:
                messagebox.showinfo("Result", "Not update Record")

        else:
            pf=t -int(fees)
            q5="update student set DepositeFee=%s, Pendingfee=%s ,DepositeDate=%s where phoneno=%s"
            b=(fees,pf,n,pn)

            result3=cur.execute(q5,b)
            if (result3 >0):
                messagebox.showinfo("Result", " your Record update successfully")
            else:
                messagebox.showinfo("Result", "Not update Record")



        db.commit()

    L=Label(top2,text='Feeform', font=('Arial 25 bold'))
    L.place(x=400, y=50)

    L1=Label(top2, text='Name', font=('Arial 15 bold'))
    L1.place(x=200, y=150)
    E1 = Entry(top2, font='Arial 15 bold')
    E1.place(x=350, y=150)

    L2 = Label(top2, text='PhoneNo', font=('Arial 15 bold'))
    L2.place(x=200, y=200)
    E2 = Entry(top2, font='Arial 15 bold')
    E2.place(x=350, y=200)

    L3 = Label(top2, text='Course', font=('Arial 15 bold'))
    L3.place(x=200, y=250)
    cb = ttk.Combobox(top2, value=s, font=('Arial 15 bold'))
    cb.place(x=350, y=250)
    cb.current(0)

    L4 = Label(top2, text='FeesAmt', font=('Arial 15 bold'))
    L4.place(x=200, y=300)
    E3 = Entry(top2, font='Arial 15 bold')
    E3.place(x=350, y=300)

    L5 = Label(top2, text='FeesDate', font=('Arial 15 bold'))
    L5.place(x=200, y=350)
    cal = DateEntry(top2, width=20, bg='darkblue', fg='white', year=2010, font=('Arial 15 bold'))
    cal.place(x=350, y=350)

    b9 = Button(top2, text='SubmitFees', fg='white', bg='#6b6a67', bd=0, font=("", 15, "bold"),command=insertfee)
    b9.place(x=350, y=410)


    top2.mainloop()

def Updatecourse():
    top5 = Toplevel(top)
    top5.geometry('900x600')

    img = ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\Blue and White Illustration Sea Desktop Wallpaper.png")
    L1 = Label(top5, image=img)
    L1.pack()

    def update():
        course = cb.get()
        fee = E2.get()

        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
        cur = db.cursor()

        b=(fee,course)
        q = "UPDATE coursefee SET fee = %s WHERE coursename = %s"
        result=cur.execute(q,b)
        if (result > 0):
            messagebox.showinfo("Result", "Record insert successfully")
        else:
            messagebox.showinfo("Result", "Record not insert successfully")
        db.commit()


    l1=Label(top5,text="UPDATED COURSE FEE",bg='black',fg='white', font=('Arial 20 bold'))
    l1.place(x=350,y=30)

    l2=Label(top5, text='COURSE',bg='black',fg='white',font=('Arial 20 bold'))
    l2.place(x=200,y=150)
    cb=ttk.Combobox(top5,value=s,font=('Arial 20 bold'))
    cb.place(x=400 ,y=150)
    cb.current(0)

    l2=Label(top5, text='UPDATED FEE',bg='black',fg='white',font=('Arial 20 bold'))
    l2.place(x=180,y=230)
    E2=Entry(top5,font='Arial 20 bold')
    E2.place(x=400,y=230)

    B2 = Button(top5, text='UPDATE', font=('Arial 19 bold'),command=update)
    B2.place(x=400, y=300)

    top5.mainloop()

def AddCourse():
    top4=Toplevel(top)
    top4.geometry('900x600')

    img = ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\Blue and White Illustration Sea Desktop Wallpaper.png")
    L1 = Label(top4, image=img)
    L1.pack()

    def insertCourse():
        k1=E1.get()
        k2=E2.get()

        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
        cur = db.cursor()
        q="insert into coursefee values('%s','%s')"%(k1,k2)
        result=cur.execute(q)
        if (result > 0):
            messagebox.showinfo("Result", "Record insert successfully")
        else:
            messagebox.showinfo("Result", "Record not insert successfully")
        db.commit()

    l1 = Label(top4, text='Course', font=('Arial 15 bold'))
    l1.place(x=150, y=200)

    E1 = Entry(top4, font=('Arial 15 bold'))
    E1.place(x=300, y=200)

    l1 = Label(top4, text='CourseFee', font=('Arial 15 bold'))
    l1.place(x=150, y=250)

    E2 = Entry(top4, font=('Arial 15 bold'))
    E2.place(x=300, y=250)

    b9 = Button(top4,text='Addcourse',fg='white',bg='#6b6a67',bd=0,font=("",15,'bold'),command=insertCourse)
    b9.place(x=300,y=300)

    top4.mainloop()

def AddTeacher():
    top5=Toplevel(top)
    top5.geometry('900x600')

    img = ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\Blue and White Illustration Sea Desktop Wallpaper.png")
    L1 = Label(top5, image=img)
    L1.pack()

    b9 = Button(top5, text='ShowTeacher', fg='white', bg='#6b6a67', bd=0, font=("", 13, 'bold'))
    b9.place(x=430, y=350)

    def insertteacher():
        s = random.randint(1000, 10000)
        k1=E1.get()
        k2=cb.get()
        k3=E2.get()


        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='sumit081204', db='project3pm')
        cur = db.cursor()

        q="insert into teacher values('%s','%s','%s',%s)"%(s,k1,k2,k3)
        result=cur.execute(q)
        if (result > 0):
            messagebox.showinfo("Result", "Record insert successfully")
        else:
            messagebox.showinfo("Result", "Record not insert successfully")
        db.commit()

    l1 = Label(top5, text='AddTeacher', font=('Arial 15 bold'))
    l1.place(x=150, y=200)

    E1 = Entry(top5, font=('Arial 15 bold'))
    E1.place(x=300, y=200)

    l1 = Label(top5, text='Course', font=('Arial 15 bold'))
    l1.place(x=150, y=250)
    cb=ttk.Combobox(top5,value=s,font=('Arial 16 bold'))
    cb.place(x=300 ,y=250)
    cb.current(0)

    l1 = Label(top5, text='Exp', font=('Arial 15 bold'))
    l1.place(x=150, y=300)

    E2 = Entry(top5, font=('Arial 15 bold'))
    E2.place(x=300, y=300)

    b9 = Button(top5, text='AddTeacher', fg='white', bg='#6b6a67', bd=0, font=("", 13, 'bold'),command=insertteacher)
    b9.place(x=300, y=350)

    top5.mainloop()


img = ImageTk.PhotoImage(file=r"C:\Users\hp\Downloads\flat-lay-workstation-with-copy-space-laptop.jpg")
L1 = Label(top, image=img)
L1.pack()

l = Label(top, text='Welcome Home', bg='black', fg='white', font=('Arial 25 bold'))
l.place(x=500, y=20)

tv = ttk.Treeview(top,height=15)
tv['columns']=('id','name','lastname','phoneno','course','dob','gender','Email','RgDate','Address','DepositeFee','PendingFee','DepositeDate')
tv.column('#0', width=0, stretch=NO)
tv.column('id', anchor=CENTER, width=80)
tv.column('name', anchor=CENTER, width=80)
tv.column('lastname', anchor=CENTER, width=100)
tv.column('phoneno', anchor=CENTER, width=100)
tv.column('course', anchor=CENTER, width=80)
tv.column('dob', anchor=CENTER, width=100)
tv.column('gender', anchor=CENTER, width=80)
tv.column('Email', anchor=CENTER, width=130)
tv.column('RgDate', anchor=CENTER, width=100)
tv.column('Address', anchor=CENTER, width=100)
tv.column('DepositeFee', anchor=CENTER, width=100)
tv.column('PendingFee', anchor=CENTER, width=100)
tv.column('DepositeDate', anchor=CENTER, width=100)



tv.heading('id', text='id', anchor=CENTER)
tv.heading('name', text='name', anchor=CENTER)
tv.heading('lastname', text='lastname', anchor=CENTER)
tv.heading('phoneno', text='phoneno', anchor=CENTER)
tv.heading('course', text='course', anchor=CENTER)
tv.heading('dob', text='dob', anchor=CENTER)
tv.heading('gender', text='gender',anchor=CENTER)
tv.heading('Email', text='Email', anchor=CENTER)
tv.heading('RgDate', text='RgDate', anchor=CENTER)
tv.heading('Address', text='Address', anchor=CENTER)
tv.heading('DepositeFee', text='DepositeFee', anchor=CENTER)
tv.heading('PendingFee', text='PendingFee', anchor=CENTER)
tv.heading('DepositeDate', text='DeposietDate', anchor=CENTER)
tv.place(x=10,y=200)


B2 = Button(top, text='ShowData', font=('Arial 20 bold'),command=show)
B2.place(x=500, y=580)

S1=Entry(top,font=('Arial 20 bold'))
S1.place(x=150,y=150)

S11=Entry(top,font=('Arial 20 bold'))
S11.place(x=700,y=150)

S10=Entry(top,font=('Arial 20 bold'))
S10.place(x=150,y=100)

S2=Button(top,text='Search',fg='white', bg='#67686b',bd=0,font=("",13,'bold'),command=Search)
S2.place(x=480,y=150)

S3=Button(top,text='Delete',fg='white', bg='#67686b',bd=0,font=("",13,'bold'),command=Delete)
S3.place(x=565,y=150)

S4=Button(top,text='Update',fg='white', bg='#67686b',bd=0,font=("",13,'bold'),command=Update)
S4.place(x=480,y=100)

S5=Button(top,text='UpdateFees',fg='white', bg='#67686b',bd=0,font=("",15,'bold'),command=UpdateFees)
S5.place(x=680,y=585)

S6=Button(top,text='UpdateCourse',fg='white', bg='#67686b',bd=0,font=("",15,'bold'),command=Updatecourse)
S6.place(x=820,y=585)

S6=Button(top,text='AddCourse',fg='white', bg='#67686b',bd=0,font=("",15,'bold'),command=AddCourse)
S6.place(x=990,y=585)


S6=Button(top,text='AddTeacher',fg='white', bg='#67686b',bd=0,font=("",15,'bold'),command=AddTeacher)
S6.place(x=1120,y=585)
top.mainloop()


