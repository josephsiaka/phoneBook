from tkinter import *
import sqlite3
import queries
from add_contact import AddContact
from update_contact import Update
from display_contact import Display
from tkinter import messagebox


conn = sqlite3.connect("phonebook.sqlite3")
cur = conn.cursor()

# to create table
cur.execute(queries.CREATE_TABLE)
conn.commit()


class Mycontacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("My Contacts")

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='plum')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/user.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=27)

        self.heading = Label(self.top, text='My Contacts',
                             font='arial 34 bold', bg='white', fg='black')
        self.heading.place(x=230, y=40)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0, column=0, padx=(40, 0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        contacts = cur.execute(queries.FETCH_ALL).fetchall()
        count = 0
        for contact in contacts:
            self.listBox.insert(count, str(contact[0]) + ". " + contact[1] + " " + contact[2])
            count += 1

        self.scroll.grid(row=0, column=1, sticky=N+S)

        # buttons

        button_add = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.add_contact)
        button_add.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        button_update = Button(self.bottom, text='Update', width=12, font='Sans 12 bold',
                               command=self.update_contact)
        button_update.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        button_display = Button(self.bottom, text='Display', width=12, font='Sans 12 bold',
                                command=self.display_contact)
        button_display.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        button_delete = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold',
                               command=self.delete_contact)
        button_delete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

    def add_contact(self):
        AddContact()
        self.destroy()
        return

    def update_contact(self):
        selected_item = self.listBox.curselection()
        contact = self.listBox.get(selected_item)
        contact_id = contact.split(".")[0]
        Update(contact_id)
        self.destroy()
        return

    def display_contact(self):
        selected_item = self.listBox.curselection()
        contact = self.listBox.get(selected_item)
        contact_id = contact.split(".")[0]
        Display(contact_id)
        self.destroy()
        return

    def delete_contact(self):
        selected_item = self.listBox.curselection()
        contact = self.listBox.get(selected_item)
        contact_id = contact.split(".")[0]

        contact_ID = contact_id
        answer = messagebox.askquestion('Warning', 'Are you sure you want to delete? ')
        if answer == 'yes':
            try:
                cur.execute(queries.DELETE, contact_ID)
                conn.commit()
                messagebox.showinfo("Success", "Contact deleted successfully", command=self.my_contacts())
                self.destroy()

            except Exception as e:
                messagebox.showinfo("Info", str(e))

    def my_contacts(self):
        Mycontacts()
        return










