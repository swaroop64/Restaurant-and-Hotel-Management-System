from tkinter import *
import random
from datetime import datetime
from PIL import Image, ImageTk  # type: ignore

root = Tk()
root.geometry('1200x650+100+20')
root.title('Restaurant Management System')

f = Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400, width=300, relief=RAISED)
f1.pack(side=LEFT, fill='both', expand=1)

f2 = Frame(root, bd=5, height=400, width=300, relief=RAISED)

image = Image.open('restaurant.jpeg')
tk_image = ImageTk.PhotoImage(image.resize((300, 120)))

lbl_info = Label(f, font=('aria', 30, 'bold'), text='Restaurant Billing System', image=tk_image, fg='white', bg='brown', width=1150, compound='left')
lbl_info.grid(row=0, column=0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand = StringVar()
CustomerID = StringVar()
OrderID = StringVar()
CustomerName = StringVar()
ContactInfo = StringVar()
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

# Create labels and entry fields for customer details

lbl_CustomerName = Label(f1, font=('aria', 20, 'bold'), text='Name', width=12, fg='blue4', bd=10, anchor='w')
lbl_CustomerName.grid(row=0, column=0)
txt_CustomerName = Entry(f1, font=('ariel', 20, 'bold'), textvariable=CustomerName, bd=6, width=8, bg='misty rose')
txt_CustomerName.grid(row=0, column=1)

lbl_ContactInfo = Label(f1, font=('aria', 20, 'bold'), text='Contact', width=12, fg='blue4', bd=10, anchor='w')
lbl_ContactInfo.grid(row=0, column=2)
txt_ContactInfo = Entry(f1, font=('ariel', 20, 'bold'), textvariable=ContactInfo, bd=6, width=8, bg='misty rose')
txt_ContactInfo.grid(row=0, column=3)

# Create labels and entry fields for menu items

lbl_Idly = Label(f1, font=('aria', 20, 'bold'), text='Idly\t: Rs 40 (ID: 1)', width=20, fg='blue4', bd=10, anchor='w')
lbl_Idly.grid(row=1, column=0)
txt_Idly = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Idly, bd=6, width=8, bg='misty rose')
txt_Idly.grid(row=1, column=1)

lbl_Dosa = Label(f1, font=('aria', 20, 'bold'), text='Dosa\t: Rs 50 (ID: 2)', width=20, fg='blue4', bd=10, anchor='w')
lbl_Dosa.grid(row=2, column=0)
txt_Dosa = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Dosa, bd=6, width=8, bg='misty rose')
txt_Dosa.grid(row=2, column=1)

lbl_Poori = Label(f1, font=('aria', 20, 'bold'), text='Poori\t: Rs 45 (ID: 3)', width=20, fg='blue4', bd=10, anchor='w')
lbl_Poori.grid(row=3, column=0)
txt_Poori = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Poori, bd=6, width=8, bg='misty rose')
txt_Poori.grid(row=3, column=1)

lbl_Coffee = Label(f1, font=('aria', 20, 'bold'), text='Coffee\t: Rs 30 (ID: 4)', width=20, fg='blue4', bd=10, anchor='w')
lbl_Coffee.grid(row=4, column=0)
txt_Coffee = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Coffee, bd=6, width=8, bg='misty rose')
txt_Coffee.grid(row=4, column=1)

lbl_Tea = Label(f1, font=('aria', 20, 'bold'), text='Tea\t: Rs 25 (ID: 5)', width=20, fg='blue4', bd=10, anchor='w')
lbl_Tea.grid(row=5, column=0)
txt_Tea = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Tea, bd=6, width=8, bg='misty rose')
txt_Tea.grid(row=5, column=1)

lbl_Vada = Label(f1, font=('aria', 20, 'bold'), text='Vada\t: Rs 30 (ID: 6)', width=20, fg='blue4', bd=10, anchor='w')
lbl_Vada.grid(row=6, column=0)
txt_Vada = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Vada, bd=6, width=8, bg='misty rose')
txt_Vada.grid(row=6, column=1)

lbl_Pongal = Label(f1, font=('aria', 20, 'bold'), text='Pongal\t: Rs 50 (ID: 7)', width=20, fg='blue4', bd=10, anchor='w')
lbl_Pongal.grid(row=7, column=0)
txt_Pongal = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Pongal, bd=6, width=8, bg='misty rose')
txt_Pongal.grid(row=7, column=1)

def generate_bill():
    bill_no = str(random.randint(15000, 50000))
    rand.set(bill_no)
    customer_id = str(random.randint(1000, 9999))
    order_id = str(random.randint(1000, 9999))
    CustomerID.set(customer_id)
    OrderID.set(order_id)
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

    costofdosa = qd * 50
    costofidly = qi * 40
    costofpoori = qp * 45
    costofcoffee = qc * 30
    costoftea = qt * 25
    costofvada = qv * 30
    costofpongal = qp * 50

    f2.pack(side=RIGHT, fill='both', expand=1)
    f2.configure(background='light yellow')

    lbl_bill = Label(f2, font=('aria', 18, 'bold'), text='Bill No.', bg='light yellow')
    lbl_bill.grid(row=1, column=0)
    txt_bill = Entry(f2, font=('ariel', 18, 'bold'), textvariable=rand, bd=6, width=18, bg='red')
    txt_bill.grid(row=1, column=1)

    lbl_date = Label(f2, font=('aria', 18, 'bold'), text='Date', bg='light yellow')
    lbl_date.grid(row=2, column=0)
    txt_date = Entry(f2, font=('ariel', 18, 'bold'), textvariable=date, bd=6, width=18, bg='misty rose')
    txt_date.grid(row=2, column=1)

    lbl_customer_id = Label(f2, font=('aria', 18, 'bold'), text='Customer ID', bg='light yellow')
    lbl_customer_id.grid(row=3, column=0)
    txt_customer_id = Entry(f2, font=('ariel', 18, 'bold'), textvariable=CustomerID, bd=6, width=18, bg='misty rose')
    txt_customer_id.grid(row=3, column=1)

    lbl_order_id = Label(f2, font=('aria', 18, 'bold'), text='Order ID', bg='light yellow')
    lbl_order_id.grid(row=4, column=0)
    txt_order_id = Entry(f2, font=('ariel', 18, 'bold'), textvariable=OrderID, bd=6, width=18, bg='misty rose')
    txt_order_id.grid(row=4, column=1)

    lbl_customer_name = Label(f2, font=('aria', 18, 'bold'), text='Customer Name', bg='light yellow')
    lbl_customer_name.grid(row=5, column=0)
    txt_customer_name = Entry(f2, font=('ariel', 18, 'bold'), textvariable=CustomerName, bd=6, width=18, bg='misty rose')
    txt_customer_name.grid(row=5, column=1)

    lbl_contact_info = Label(f2, font=('aria', 18, 'bold'), text='Contact Info', bg='light yellow')
    lbl_contact_info.grid(row=6, column=0)
    txt_contact_info = Entry(f2, font=('ariel', 18, 'bold'), textvariable=ContactInfo, bd=6, width=18, bg='misty rose')
    txt_contact_info.grid(row=6, column=1)

    lbl_cost = Label(f2, font=('aria', 18, 'bold'), text='Cost', bg='light yellow')
    lbl_cost.grid(row=7, column=0)
    txt_cost = Entry(f2, font=('ariel', 18, 'bold'), textvariable=Cost, bd=6, width=18, bg='misty rose')
    txt_cost.grid(row=7, column=1)

    lbl_service = Label(f2, font=('aria', 18, 'bold'), text='Service Charge', bg='light yellow')
    lbl_service.grid(row=8, column=0)
    txt_service = Entry(f2, font=('ariel', 18, 'bold'), textvariable=Service_Charge, bd=6, width=18, bg='misty rose')
    txt_service.grid(row=8, column=1)

    lbl_tax = Label(f2, font=('aria', 18, 'bold'), text='Tax', bg='light yellow')
    lbl_tax.grid(row=9, column=0)
    txt_tax = Entry(f2, font=('ariel', 18, 'bold'), textvariable=Tax, bd=6, width=18, bg='misty rose')
    txt_tax.grid(row=9, column=1)

    lbl_total = Label(f2, font=('aria', 18, 'bold'), text='Total', bg='light yellow')
    lbl_total.grid(row=10, column=0)
    txt_total = Entry(f2, font=('ariel', 18, 'bold'), textvariable=Total, bd=6, width=18, bg='red')
    txt_total.grid(row=10, column=1)

    Totalcost = costofcoffee + costofdosa + costofidly + costofpoori + costoftea + costofvada + costofpongal
    costofmeal = 'Rs.', str('%.2f' % Totalcost)
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
    CustomerID.set('')
    OrderID.set('')
    CustomerName.set('')
    ContactInfo.set('')
    f2.pack_forget()

btn_Total = Button(f1, bd=5, fg='black', font=('ariel', 16, 'bold'), width=14, text='CALCULATE BILL', bg='SteelBlue1', command=generate_bill)
btn_Total.grid(row=9, column=0, padx=10, pady=10)

btn_Reset = Button(f1, bd=5, fg='black', font=('ariel', 16, 'bold'), width=14, text='RESET', bg='SteelBlue1', command=reset)
btn_Reset.grid(row=9, column=1, padx=10, pady=10)

btn_Exit = Button(f1, bd=5, fg='black', font=('ariel', 16, 'bold'), width=14, text='EXIT', bg='SteelBlue1', command=qexit)
btn_Exit.grid(row=9, column=2, padx=10, pady=10)

root.mainloop()
