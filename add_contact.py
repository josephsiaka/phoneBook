from tkinter import *
from tkinter import messagebox
import sqlite3
import queries

conn = sqlite3.connect("phonebook.sqlite3")
cur = conn.cursor()


class AddContact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Add New Contact")

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='plum')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/user.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=35)

        self.heading = Label(self.top, text='Add New Contact',
                             font='arial 28 bold', bg='white', fg='black')
        self.heading.place(x=230, y=50)

        # firstName
        self.label_firstname = Label(self.bottom, text='First Name', font='arial 15 bold', fg='black', bg='white')
        self.label_firstname.place(x=40, y=40)

        self.entry_firstname = Entry(self.bottom, width=30, bd=4)
        self.entry_firstname.place(x=150, y=40)

        # lastName
        self.label_lastname = Label(self.bottom, text='Last Name', font='arial 15 bold', fg='black', bg='white')
        self.label_lastname.place(x=40, y=80)

        self.entry_lastname = Entry(self.bottom, width=30, bd=4)
        self.entry_lastname.place(x=150, y=80)

        # email
        self.label_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='black', bg='white')
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.place(x=150, y=120)

        # phone number
        self.label_phone = Label(self.bottom, text='Phone No.', font='arial 15 bold', fg='black', bg='white')
        self.label_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.place(x=150, y=160)

        # address
        self.label_address = Label(self.bottom, text="Address", font='arial 15 bold', fg='black', bg='white')
        self.label_address.place(x=40, y=200)

        self.entry_address = Entry(self.bottom, width=30, bd=4)
        self.entry_address.place(x=150, y=200)

        # button
        button = Button(self.bottom, text='Add contact', command=self.add_contact)
        button.place(x=250, y=260)

    def add_contact(self):
        first_name: str = self.entry_firstname.get()
        last_name: str = self.entry_lastname.get()
        number = self.entry_phone.get()
        email: str = self.entry_email.get()
        address: str = self.entry_address.get()

        if first_name and last_name and number and email and address != "":
            try:
                p = int(number)
            except:
                messagebox.showerror('Error', 'phone number is not valid')
                return
            try:
                cur.execute(queries.INSERT, (first_name, last_name, number, email, address))
                conn.commit()
                messagebox.showinfo('Success', "contact added successfully")
                self.destroy()
                return

            except EXCEPTION as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror('Error', "All fields must be filled", icon='warning')