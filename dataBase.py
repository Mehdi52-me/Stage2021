from tkinter import *
import sqlite3

root = Tk()
root.title('Message')
root.iconbitmap("C:\\Users\\sises\\Desktop\\stage d'été 2021\\icon.ico")
# root.geometry("360x350")

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create a cursor
c = conn.cursor()


# Create table

# c.execute(
    # """CREATE TABLE addresses (
#               first_name text,
#               last_name text,
#               e_mail text,
#               city text,
#               state text,
#               zipcode integer)"""
#               )


# Create Submit Func
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create a cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses Values ( :f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': mail.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    mail.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create Query Func
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the database

    # c.execute("SELECT *, oid FROM addresses")
    # records = c.fetchall()
    # print(records)

    # Loop Thru Results
    i = 12
    for row in c.execute("SELECT * from addresses"):
        print_records = row
        query_label = Label(root, text=print_records)
        query_label.grid(row=i, column=0, columnspan=2)
        i += 1

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


# Create Delete Func
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


# Create edit Func
def edit(args):
    pass


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 2))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, pady=2)
mail = Entry(root, width=30)
mail.grid(row=2, column=1, pady=2)
city = Entry(root, width=30)
city.grid(row=3, column=1, pady=2)
state = Entry(root, width=30)
state.grid(row=4, column=1, pady=2)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, pady=2)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 2), sticky=E)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0, pady=2, sticky=E)
mail_label = Label(root, text="E-Mail")
mail_label.grid(row=2, column=0, pady=2, sticky=E)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0, pady=2, sticky=E)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0, pady=2, sticky=E)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0, pady=2, sticky=E)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5, sticky=E)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=134)
# Commit changes
conn.commit()

# Close connection
conn.close()

mainloop()
