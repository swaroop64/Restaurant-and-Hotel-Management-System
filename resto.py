from tkinter import*
import random
from datetime import datetime
from PIL import Image, ImageTk # type: ignore

root = Tk()
root.geometry('1200x650+100+20')
root.title('Restaurant Management System')

f = Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400, width=300, relief=RAISED)
f1.pack(side=LEFT,fill='both',expand=1)

f2 = Frame(root, bd=5, height=400, width=300, relief=RAISED)

image = Image.open('restaurant.jpeg')
# image = image.resize((1200, 650), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(image.resize((300, 120)))

lbl_info = Label(f, font=('aria', 30, 'bold'), text= 'Restaurant Billing System', image=tk_image, fg='white', bg='brown', width=1150, compound='left')
lbl_info.grid(row=0, column=0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand = StringVar()
Dosa = StringVar()
Idly = StringVar()
Poori = StringVar()
Vada = StringVar()
Pongal = StringVar()
Coffee = StringVar()
Tea = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Cost = StringVar()
date = StringVar()
time = StringVar()

#create a label for the items above

lbl_Idly = Label(f1, font=('aria', 20, 'bold'), text='Idly\t: Rs 40', width=12, fg='blue4', bd=10, anchor='w')
lbl_Idly.grid(row=1, column=0)
txt_Idly = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Idly, bd=6, width=8, bg='misty rose')
txt_Idly.grid(row=1, column=1)

lbl_Dosa = Label(f1, font=('aria', 20, 'bold'), text='Dosa\t: Rs 50', width=12, fg='blue4', bd=10, anchor='w')
lbl_Dosa.grid(row=2, column=0)
txt_Dosa = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Dosa, bd=6, width=8, bg='misty rose')
txt_Dosa.grid(row=2, column=1)

lbl_Poori = Label(f1, font=('aria', 20, 'bold'), text='Poori\t: Rs 45', width=12, fg='blue4', bd=10, anchor='w')
lbl_Poori.grid(row=3, column=0)
txt_Poori = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Poori, bd=6, width=8, bg='misty rose')
txt_Poori.grid(row=3, column=1)

lbl_Coffee = Label(f1, font=('aria', 20, 'bold'), text='Coffee\t: Rs 30', width=12, fg='blue4', bd=10, anchor='w')
lbl_Coffee.grid(row=4, column=0)
txt_Coffee = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Coffee, bd=6, width=8, bg='misty rose')
txt_Coffee.grid(row=4, column=1)

lbl_Tea = Label(f1, font=('aria', 20, 'bold'), text='Tea\t: Rs 25', width=12, fg='blue4', bd=10, anchor='w')
lbl_Tea.grid(row=5, column=0)
txt_Tea = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Tea, bd=6, width=8, bg='misty rose')
txt_Tea.grid(row=5, column=1)
                 
lbl_Vada = Label(f1, font=('aria', 20, 'bold'), text='Vada\t: Rs 30', width=12, fg='blue4', bd=10, anchor='w')
lbl_Vada.grid(row=6, column=0)
txt_Vada = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Vada, bd=6, width=8, bg='misty rose')
txt_Vada.grid(row=6, column=1)

lbl_Pongal = Label(f1, font=('aria', 20, 'bold'), text='Pongal\t: Rs 50', width=12, fg='blue4', bd=10, anchor='w')
lbl_Pongal.grid(row=7, column=0)
txt_Pongal = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Pongal, bd=6, width=8, bg='misty rose')
txt_Pongal.grid(row=7, column=1)

def generate_bill():
    bill_no = str(random.randint(15000, 50000))
    rand.set(bill_no)
    date.set(localtime)
    try: qd = int(Dosa.get())
    except: qd = 0
    try: qi = int(Idly.get())
    except: qi = 0
    try: qp = int(Poori.get())
    except: qp = 0
    try: qc = int(Coffee.get())
    except: qc = 0
    try: qt = int(Tea.get())
    except: qt = 0
    try: qv = int(Vada.get())
    except: qv = 0
    try: qp = int(Pongal.get())
    except: qp = 0

    
    costofdosa = qd*45
    costofidly = qi*40
    costofpoori = qp*40
    costofcoffee = qc*30
    costoftea = qt*25
    costofvada = qv*30
    costofpongal = qp*50
    # costofservice = Service_Charge.get()
    # costoftax = costofservice*0.18
    # costoftotal = "Rs", str('%.2f' % (costofdosa

    f2.pack(side=RIGHT, fill='both', expand=1)
    f2.configure(background='light yellow')

    lbl_bill = Label(f2, font=('aria', 18, 'bold'), text='Bill No.', bg='light yellow')                        
    lbl_bill.grid(row=1, column=0)
    txt_bill = Entry(f2,font=('ariel', 18, 'bold'), textvariable=rand, bd=6, width=18, bg='red')
    txt_bill.grid(row=1, column=1)

    lbl_date = Label(f2, font=('aria', 18, 'bold'), text='Date', bg='light yellow')                        
    lbl_date.grid(row=2, column=0)
    txt_date = Entry(f2,font=('ariel', 18, 'bold'), textvariable=date, bd=6, width=18, bg='misty rose')
    txt_date.grid(row=2, column=1)

    lbl_cost = Label(f2, font=('aria', 18, 'bold'), text='Cost', bg='light yellow')                        
    lbl_cost.grid(row=3, column=0)
    txt_cost = Entry(f2,font=('ariel', 18, 'bold'), textvariable=Cost, bd=6, width=18, bg='misty rose')
    txt_cost.grid(row=3, column=1)

    lbl_service = Label(f2, font=('aria', 18, 'bold'), text='Service Charge', bg='light yellow')                        
    lbl_service.grid(row=4, column=0)
    txt_service = Entry(f2,font=('ariel', 18, 'bold'), textvariable=Service_Charge, bd=6, width=18, bg='misty rose')
    txt_service.grid(row=4, column=1)

    lbl_tax = Label(f2, font=('aria', 18, 'bold'), text='Tax', bg='light yellow')                        
    lbl_tax.grid(row=5, column=0)
    txt_tax = Entry(f2,font=('ariel', 18, 'bold'), textvariable=Tax, bd=6, width=18, bg='misty rose')
    txt_tax.grid(row=5, column=1)

    lbl_total = Label(f2, font=('aria', 18, 'bold'), text='Total', bg='light yellow')                        
    lbl_total.grid(row=6, column=0)
    txt_total = Entry(f2,font=('ariel', 18, 'bold'), textvariable=Total, bd=6, width=18, bg='red')
    txt_total.grid(row=6, column=1)

    Totalcost= costofcoffee + costofdosa + costofidly + costofpoori + costoftea + costofvada + costofpongal
    costofmeal = 'Rs.', str('%.2f' %Totalcost)
    payTax = (Totalcost * 0.18)
    paidTax = 'Rs.', str('%.2f' % payTax)
    ser_charge = (Totalcost * 0.01)
    service = 'Rs.', str('%.2f' % ser_charge)
    overall = payTax + Totalcost + ser_charge
    total = 'Rs.', str('%.2f' % overall)

    Service_Charge.set(service)
    Cost.set(costofmeal)
    Tax.set(paidTax)
    Total.set(total)

def qexit():
    root.destroy()

def reset():
    Dosa.set('')
    Poori.set('')
    Idly.set('')
    Coffee.set('')
    Tea.set('')
    Vada.set('')
    Pongal.set('')
    date.set('')
    f2.pack_forget()

btn_Total = Button(f1, bd=5, fg='black', font=('ariel', 16, 'bold'), width=14, text='CALCULATE BILL', bg='SteelBlue1', command=generate_bill) 
btn_Total.grid(row=9, column=0, padx=10, pady=10)

btn_Reset = Button(f1, bd=5, fg='black', font=('ariel', 16, 'bold'), width=14, text='RESET', bg='SteelBlue1', command=reset)
btn_Reset.grid(row=9, column=1, padx=10, pady=10)

btn_Exit = Button(f1, bd=5, fg='black', font=('ariel', 16, 'bold'), width=14, text='EXIT', bg='SteelBlue1', command=qexit)
btn_Exit.grid(row=9, column=2, padx=10, pady=10)

root.mainloop()