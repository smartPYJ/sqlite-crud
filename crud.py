import sqlite3
from sqlite3 import Error


# create connection to SQLLITE database
def sql_connection():
    try:
        con = sqlite3.connect('student.db')
        return con
    except Error:
        print(Error)


con = sql_connection()


# Create a table to the database
def sql_table(con):
    try:
        cursorObj = con.cursor()
        cursorObj.execute(
            "CREATE TABLE profile(registration_no text PRIMARY KEY, surname text, firstname text,middlename text,age int, state text, department text, religion text)")
        con.commit()
    except Error:
        print(Error)


# sql_table(con)


# Add student data to the table
def add_student(con):
    cursorObj = con.cursor()

    reg_no = input("enter your registration number  .. ")
    firstname = input("enter your firstname.. ")
    surname = input("enter your surname.. ")
    middlename = input("enter your middle name.. ")
    age = int(input("enter your age .. "))
    state = input("enter your state  .. ")
    department = input("enter your department  .. ")
    religion = input("enter your state  .. ")
    entities = (reg_no, firstname, surname, middlename,
                age, state, department, religion)

    cursorObj.execute(
        'INSERT INTO profile(registeraton_no, surname, firstname, middlename, age, state, department, religion ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)',
        entities)
    con.commit()


# Update student record

# update student name
def update_name(con):
    cursorObj = con.cursor()
    regno = input("Enter Student Registration Number ")
    name = input(" Enter Student New  Firstname ")
    cursorObj.execute(
        'UPDATE  profile  SET name= ?  WHERE registration_no= ?', (name, regno))
    con.commit()


# update student age
def update_age(con):
    cursorObj = con.cursor()
    regno = input("Enter Student Registration Number ")
    age = int(input(" Enter Student new Age "))
    cursorObj.execute(
        'UPDATE  profile  SET age= ?  WHERE registration_no= ?', (age, regno))
    con.commit()


# update student department
def update_department(con):
    cursorObj = con.cursor()
    regno = input("Enter Student Registration Number ")
    dept = input(" Enter Student new department")
    cursorObj.execute(
        'UPDATE  profile  SET department= ?  WHERE registration_no= ?', (dept, regno))
    con.commit()


# update student state
def update_state(con):
    cursorObj = con.cursor()
    regno = input("Enter Student Registration Number:.. ")
    state = input(" Enter Student new state:.. ")
    cursorObj.execute(
        'UPDATE  profile  SET name= ?  WHERE registration_no= ?', (state, regno))
    con.commit()


# update student religion
def update_religion(con):
    cursorObj = con.cursor()
    regno = input("Enter Student Registration Number:..")
    religion = input(" Enter Student new religion:.. ")
    cursorObj.execute(
        'UPDATE  profile  SET name= ?  WHERE registration_no= ?', (religion, regno))
    con.commit()


# this function is to delete a user from the database

def delete_user(con):
    try:
        cursorObj = con.cursor()
        regnumber = input("Enter the Student Registration Number ")
        cursorObj.execute('DELETE form profile where registration_no =? )', [
            regnumber])
        con.commit()
        print("Succesfully... ")
    except Error:
        print(" User Registration number is invalid or does not exist")


def view_student(con):
    try:
        cusorObj = con.cursor()
        cusorObj.execute('SELECT * from profile')
        rows = cusorObj.fetchall()
        for row in rows:
            print(row)
        con.commit()
    except Error:
        print(Error)


def welcome():
    print(
        '''
    Welcome to SMART College International school managment system  \t
    Select an option from the list of options \t
     press 1 to add a student \t
     press 2 to update student record \t
     press 3 to delete a student \t
     press 4 to view all student \t 

     '''
    )
    option = int(input(" .....waiting for reply "))

    if option == 1:
        add_student(con)
    elif option == 2:
        update()
    elif option == 3:
        delete_user(con)
    elif option == 4:
        view_student(con)
    else:
        print("Wrong input ")


def update():
    print(
        '''
        welcome to student update \t
        press 1 to update student name \t
        press 2 to update student age \t
        press 3 to update student state \t
        press 4 to update student department\t
        press 5 to update student religion 

        '''
    )
    opt = int(input("Select an option:.."))
    if opt == 1:
        update_name(con)
    elif opt == 2:
        update_age(con)
    elif opt == 3:
        update_state(con)
    elif (opt == 4):
        update_department(con)
    elif (opt == 5):
        update_religion(con)
    else:
        print("Wrong Input ..")


print("Welcome ")
action = int(
    input("Choose an action \t Press 1  to manage database \t press 0 to exit"))
while (action != 0):
    welcome()
    action = int(
        input("Choose an action \t Press 1  to manage database \t press 0 to exit"))
print("Thank you for using SMART College Database ")
exit(0)
