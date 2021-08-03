from tkinter import *
from mycontacts import Mycontacts
from add_contact import AddContact


class Application(object):
    def __init__(self, master):
        self.master = master
        # frames

        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#03befc')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120, y=5)

        self.heading = Label(self.top, text='My Phonebook',
                             font='arial 34 bold', bg='white', fg='black')
        self.heading.place(x=270, y=40)

        # button1(My contacts)
        self.contactsButton = Button(self.bottom, text=" My Contacts ", fg="#03befc", font='arial 16 bold',
                                     command=self.my_contacts)
        self.contactsButton.place(x=270, y=45)

        # button2(Add Contacts)
        self.addButton = Button(self.bottom, text=" Add Contacts ", fg="#03befc", font='arial 16 bold',
                                command=self.add_contacts)
        self.addButton.place(x=267, y=95)

    def my_contacts(self):
        Mycontacts()
        return

    def add_contacts(self):
        AddContact()
        return


def main():
    root = Tk()
    app = Application(root)
    root.title("Phonebook App")
    root.geometry("650x650+350+200")
    root.mainloop()


if __name__ == '__main__':
    main()
