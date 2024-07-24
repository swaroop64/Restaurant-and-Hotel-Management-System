# Restaurant-and-Hotel-Management-System
# Overview

This project is a desktop application designed for managing restaurant billing using a graphical user interface (GUI) created with the Tkinter library in Python. The application allows restaurant staff to input customer details, order quantities for various menu items, calculate the total bill, and generate a detailed receipt. It also includes features to reset the form and exit the application.

# Key Features

Customer Details Input: Fields are used to enter the customer's name and contact information.

Menu Item Input: Entry fields are used to input the quantity of each menu item ordered by the customer.

Billing Information: Automatic generation of bill number, customer ID, and order ID.

Cost Calculation: Calculation of the total cost of the order, including individual item costs, service charges, and taxes.

Receipt Generation: Display of the generated bill with all relevant details, such as customer name, contact info, order ID, date, and total cost.

Form Reset: Option to clear all input fields and reset the form.

Exit Application: Option to close the application.

# Technologies Used

Python: The programming language used to develop the application.

Tkinter: The standard Python library used for creating the GUI.

PIL (Pillow): A Python Imaging Library used for handling images in the application.

Random: Used to generate random numbers for bill, customer, and order IDs.

Datetime: Used for getting and formatting the current date and time.

# Functionality Breakdown

# GUI Setup:

The main window is created and configured with a specific size and title.
Frames are used to organize the layout of the application.
# Image and Title:
An image is loaded and resized using PIL.
A label is created to display the title of the application along with the image.

# Input Fields:
Labels and entry fields are created for customer details and menu items.
StringVar variables are used to store and manage the input data.

# Bill Generation:
The generate_bill function calculates the total cost, service charge, and tax.
Random numbers are generated for the bill number, customer ID, and order ID.
A receipt with all details is displayed in a new frame.

# Reset and Exit:
The reset function clears all input fields and hides the bill frame.
The qexit function closes the application.

This restaurant billing system is a practical tool for managing orders and generating bills efficiently in a restaurant setting. The use of a GUI makes it user-friendly and accessible for restaurant staff.







