"""
program: project_gui.py
Author: Kelly Smith
Last day updated: 12/01/19

Program to create a GUI for input into the SURS contact database
:param notes - Notes about the client contact
:param contact_mode - How the client was contacted
:param person_contacted - Client contacted
:param  contact_date - Date of contact
:param  engage_id  - Engagement ID from Salesforce - Not all contacts will have an engagement ID
:param  contact_made - Was contact made - Yes or No
:param   staff - Staff person making the contact
:return Information will be entered into Contactdatabase.db
"""
import tkinter
import sqlite3
from project_code.error_class import Yesno, NotAlpha, Dateformat, NotAlphaTwo

root = tkinter.Tk()
root.title("Entry for Client Contact")
root.geometry("500x500")
root.configure(background='blue')
conn = sqlite3.connect('Conactdatabase.db')
c = conn.cursor()
contact_date = ''
contact_made = ''
contact_mode = ''
person_contacted = ''
engage_id = ''
notes = ''
staff = ''


def submit():
    conn = sqlite3.connect('Conactdatabase.db')
    c = conn.cursor()
    global contact_date, contact_made, contact_mode, person_contacted, engage_id, notes, staff

    def engage_na():
        engage_id = engage_id_text.get()
        if engage_id == '':
            engage_id = 'N/A'
        return engage_id

    def date():
        contact_date = contact_date_text.get()
        if len(contact_date) != 8:
            raise Dateformat
        else:
            return contact_date

    def made():
        contact_made = contact_made_text.get()
        if not contact_made == 'Yes' or contact_made == 'No':
            raise Yesno
        else:
            return contact_made

    def client():
        person_contacted = person_contacted_text.get()
        if not person_contacted.isalpha():
            raise NotAlpha
        else:
            return person_contacted

    def employee():
        staff = staff_text.get()
        if not staff.isalpha():
            raise NotAlphaTwo
        else:
            return staff

    notes = notes_text.get()
    contact_mode = contact_mode_text.get()
    person_contacted = client()
    contact_date = date()
    engage_id = engage_na()
    contact_made = made()
    staff = employee()
    c.execute(
        "INSERT INTO contact (contactdate, contactmade, contactmode, personcontacted, engagementid, notes, staff) VALUES (%r, %r, %r, %r, %r, %r, %r)" % (
            contact_date, contact_made, contact_mode, person_contacted, engage_id, notes, staff))
    conn.commit()
    conn.close()
    print(f'New Record: Date: {contact_date} Engaged: {contact_made} Via: {contact_mode} Client: {person_contacted} Engagement ID: {engage_id} Notes: {notes} Staff: {staff}')


def query():
    conn = sqlite3.connect('Conactdatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact")
    records = c.fetchall()
    print_records = ''
    for record in records[-1]:
        print_records += str(record) + "\n"
    query_label = tkinter.Label(root, bg='blue', fg='white', text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    conn.commit()
    conn.close()


# entry boxes
contact_date_text = tkinter.Entry(root, width=15)
contact_date_text.grid(row=1, column=1)
contact_made_text = tkinter.Entry(root, width=15)
contact_made_text.grid(row=2, column=1)
contact_mode_text = tkinter.Entry(root, width=15)
contact_mode_text.grid(row=3, column=1)
person_contacted_text = tkinter.Entry(root, width=15)
person_contacted_text.grid(row=4, column=1)
engage_id_text = tkinter.Entry(root, width=15)
engage_id_text.grid(row=5, column=1)
notes_text = tkinter.Entry(root, width=15)
notes_text.grid(row=6, column=1)
staff_text = tkinter.Entry(root, width=15)
staff_text.grid(row=7, column=1)
# labels for entry boxes
contact_date_label = tkinter.Label(root, bg='blue', fg='white', text="Date of contact")
contact_date_label.grid(row=1, column=0)
contact_made_label = tkinter.Label(root, bg='blue', fg='white', text="Was contact made (Yes or No)")
contact_made_label.grid(row=2, column=0)
contact_mode_label = tkinter.Label(root, bg='blue', fg='white', text="How was contact made")
contact_mode_label.grid(row=3, column=0)
person_contacted_label = tkinter.Label(root, bg='blue', fg='white', text="Person you spoke with")
person_contacted_label.grid(row=4, column=0)
engage_id_label = tkinter.Label(root, bg='blue', fg='white', text="Engagement ID")
engage_id_label.grid(row=5, column=0)
notes_label = tkinter.Label(root, bg='blue', fg='white', text="Notes")
notes_label.grid(row=6, column=0)
staff_label = tkinter.Label(root, bg='blue', fg='white', text="Your name")
staff_label.grid(row=7, column=0)
# buttons
submit_btn = tkinter.Button(root, text="Add Record", command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
query_btn = tkinter.Button(root, text="Show Record", command=query)
query_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=5, ipadx=100)
quit_btn = tkinter.Button(root, text="Exit", command=quit)
quit_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
root.mainloop()
