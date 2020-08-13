import sqlite3
from tkinter import *


#tkinter stuff
root = Tk()
root.title('Schedulr')
root.geometry("400x400")

#submit function for database
def submit():
    #connect to database
    connect = sqlite3.connect('database.db')
   
    #create cursor, whatever that means, this has to done locally to the function as well
    cursor = connect.cursor()

    #Insert into table includes dummy variables that start with :, first part of line 25 comes from the dummy variable names
    #lines 25,26 are python dictionaries
    cursor.execute("INSERT INTO staff VALUES (:f_name, :l_name)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
        }
    
    )

    #commit or SAVE
    connect.commit()
    #close
    connect.close()

     #clear the text boxes first after submitted
    f_name.delete(0, END)
    l_name.delete(0, END)



#the show staff button
def query():
    connect = sqlite3.connect('database.db')

    #create cursor, whatever that means, this has to done locally to the function as well
    cursor = connect.cursor()

    #Query, oid is the primary key
    cursor.execute("SELECT *, oid FROM staff")
    #next we name a variable and give it the value from fetchall (meaning all entries from the table, in this case staff)
    entries = cursor.fetchall()
    #loop through results
    print_entries = ''
    for entry in entries:
        print_entries += str(entry) + "\n"

    query_label = Label(root, text=print_entries)
    query_label.grid(row=4, column=0, columnspan =2)

     #commit or SAVE
    connect.commit()


#XXXXXXXXXXXXXXXXXXXXXX  databases

#create database for the staff and their data
connect = sqlite3.connect('database.db')

#create cursor, whatever that means
cursor = connect.cursor()


#create staff table
#the "x6 are necessary to make the command multiline without breaking
cursor.execute(""" CREATE TABLE IF NOT EXISTS staff (
    last_name text,
    first_name text
)""")
#                             readd these after they have entry options 
    #nco null,  
    #etp null,
    #shu null,
    #cls null,
    #grade integer


#nco - yes or no, exception to policy (i.e. e5(p) working Escort 1), SHU y/n, CLS y/n, pay grade i.e. e5

cursor.execute(""" CREATE TABLE IF NOT EXISTS schedule (
    location text,
    nco null,
    cls null,
    shu null,
    etp null
)""")
#this table covers the requirements for the post, i.e. do you need to be an nco, will an etp count (Escort 1 or Booth as cpl), 

#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

#create box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

#create submit button
submit_button = Button(root, text="Add record to database", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#query button shows values
query_btn = Button(root, text="Show Staff", command=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#tkinter stuff ?
root.mainloop()

#commit or SAVE
connect.commit()
