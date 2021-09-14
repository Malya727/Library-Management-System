import details as dt
import getpass
from prettytable import PrettyTable

def main_function():
    print("---------- Welcome Student ----------")
    table = dt.get_pretty_table(["1.Sign Up" , "2.Sign In"])
    print(table)
    ch = int(input("Enter Your Choice :"))
    if ch == 1:
        sign_up()
    elif ch == 2:
        sign_in()
    else:
        print("Invalid Choice!")
        exit()

def sign_up():
    Name = input("Enter Name :")
    USN = input("Enter USN :")
    Address = input("Enter Address :")
    Phone = input("Enter Phone Number :")
    password = input("Enter Password :")
    due_amout = 0
    due_paid = 0
    due_pending = 0
    books_carry = 2
    result = dt.get_student_by_usn(USN)
    if len(result) > 0:
        print("USN is Already Present Please Try Again!")
        sign_up()
    else:
        data = USN.upper() + '|' + Name + '|' + Address  + '|' + str(Phone) + '|' + password + '|' + str(due_amout) + '|' + str(due_paid) + '|' + str(due_pending) + '|' + str(books_carry) + '$'
        f = open("students.txt","a")
        f.write(data)
        f.close()
        main_function()


def sign_in():
    usn = input("Enter USN :")
    password = getpass.getpass("Enter Password :")
    result = dt.get_student_by_usn(usn.upper())
    if len(result) == 0:
        print("USN not Found!")
    elif result[0] == usn and result[4] == password:
        table = dt.student_details_in_pretty_table(usn)
        print("---------- Student Basic Informations are ----------")
        print(table)
        print("---------- Book Issued to Student from Library Are ----------")
        boolean,table = dt.get_book_issued_to_student_in_pretty_table(usn)
        if boolean:
            print(table)
        else:
            print("No Active Borrow History Present in Database!")
        print("Enter 1. Logout")
        inp = int(input("Enter Choice :"))
        if inp == 1:
            main_function()
    else:
        print("Invalid Password!")
        sign_in()

