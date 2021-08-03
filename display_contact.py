from tkinter import *
import sqlite3


conn = sqlite3.connect("phonebook.sqlite3")
cur = conn.cursor()


class Display(Toplevel):
    def __init__(self, contact_id):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Display Contact")

        query = "select * from PHONEBOOK where id ='{}'".format(contact_id)
        result = cur.execute(query).fetchone()
        self.contact_id = contact_id
        contact_firstname = result[1]
        contact_lastname = result[2]
        contact_number = result[3]
        contact_email = result[4]
        contact_address = result[5]

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='plum')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/user.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=35)

        self.heading = Label(self.top, text='Contact Details',
                             font='arial 28 bold', bg='white', fg='black')
        self.heading.place(x=230, y=50)

        # firstName
        self.label_firstname = Label(self.bottom, text='First Name', font='arial 15 bold', fg='black', bg='white')
        self.label_firstname.place(x=40, y=40)

        self.entry_firstname = Entry(self.bottom, width=30, bd=4)
        self.entry_firstname.insert(0, contact_firstname)
        self.entry_firstname.config(state='disabled')
        self.entry_firstname.place(x=150, y=40)

        # lastName
        self.label_lastname = Label(self.bottom, text='Last Name', font='arial 15 bold', fg='black', bg='white')
        self.label_lastname.place(x=40, y=80)

        self.entry_lastname = Entry(self.bottom, width=30, bd=4)
        self.entry_lastname.insert(0, contact_lastname)
        self.entry_lastname.config(state='disabled')
        self.entry_lastname.place(x=150, y=80)

        # email
        self.label_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='black', bg='white')
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, contact_email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=150, y=120)

        # phone number
        self.label_phone = Label(self.bottom, text='Phone No.', font='arial 15 bold', fg='black', bg='white')
        self.label_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, contact_number)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=150, y=160)

        # address
        self.label_address = Label(self.bottom, text="Address", font='arial 15 bold', fg='black', bg='white')
        self.label_address.place(x=40, y=200)

        self.entry_address = Entry(self.bottom, width=30, bd=4)
        self.entry_address.insert(0, contact_address)
        self.entry_address.config(state='disabled')
        self.entry_address.place(x=150, y=200)
