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
            "CREATE TABLE profile(registration_no text PRIMARY KEY, full_name text,age int, state text, department text, religion text)")
        con.commit()
    except Error:
        print(Error)


# sql_table(con)


# Add student data to the table
def add_student(con):
    cursorObj = con.cursor()

    reg_no = input("enter your registration number  .. ")
    full_name = input("enter your full name.. ")
   
    age = int(input("enter your age .. "))
    state = input("enter your state  .. ")
    department = input("enter your department  .. ")
    religion = input("enter your state  .. ")
    entities = (reg_no, full_name,
                age, state, department, religion)

    cursorObj.execute(
        'INSERT INTO profile(registeraton_no, full_name, age, state, department, religion ) VALUES(?, ?, ?, ?, ?, ?)',
        entities)
    con.commit()


# Update student record

# update student name
def update_name(con):
    cursorObj = con.cursor()
    regno = input("Enter Student Registration Number ")
    name = input(" Enter Student New  name")
    cursorObj.execute(
        'UPDATE  profile  SET full_name= ?  WHERE registration_no= ?', (name, regno))
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
    
     press 1 to add a student
     press 2 to update student record 
     press 3 to delete a student 
     press 4 to view all student 

     '''
    )
    option = int(input(" ..... "))

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
        welcome to student update 
        press 1 to update student name 
        press 2 to update student age 
        press 3 to update student state 
        press 4 to update student department
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
print("Thanks")
exit(0)
