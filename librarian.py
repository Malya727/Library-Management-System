import getpass
import details as dt
from prettytable import PrettyTable
import datetime

def Add_Book():
    Name = input("Enter Book Name :")
    Id = input("Enter Book ID :")
    Price = input("Enter Book Price :")
    Author = input("Enter Book Author :")
    Availablity = input("Enter Book Count in Library :")
    result = Name + '|' + Id + '|' + Price + '|' + Author + '|' + Availablity + '$'
    file = open("Book_Details.txt","a")
    file.write(result)
    file.close()
    after_login()

def Update_Book():
    book_id = input("Enter Book ID :")
    result = dt.get_book_by_id(book_id)
    if len(result) == 0:
        print("Book Details Not Found")
    else:
        X = PrettyTable()
        X.field_names = ["Name" , "Book ID" , "Cost" , "Author" , "Stock in Library"]
        X.add_row(result)
        print(X)
        data = ["1.Update Book Name" , "2.Update Cost" , "3.Update Author Name" , "4.Update Stock in Library"]
        table = dt.get_pretty_table(data)
        print(table)
        ch = int(input("Enter Choice :"))
        if ch == 1:
            Name = input("Enter New Name :")
            result[0] = Name
        elif ch == 2:
            Cost = input("Enter Cost :")
            result[2] = Cost
        elif ch == 3:
            Author = input("Enter Author Name :")
            result[3] = Author
        elif ch == 4:
            stock = input("Enter Stock in Library :")
            result[4] = stock
        f = open("Book_Details.txt" , "r")
        data = f.read()
        f.close()
        res_lst = []
        li = data.split('$')
        li.pop()
        for l in li:
            li2 = l.split('|')
            if book_id == li2[1]:
                res_lst.append('|'.join(result))
            else:
                res_lst.append(l)
        book = '$'.join(res_lst) + '$'
        file = open("Book_Details.txt" , "w")
        file.write(book)
        file.close()
        after_login()

def Issue_Book():
    usn = input("Enter USN :")
    book_id = input("Enter Book ID :")
    stu_details = dt.get_student_by_usn(usn)
    book_details = dt.get_book_by_id(book_id)
    if len(stu_details) == 0:
        print("No Student Found")
        Issue_Book()
    elif len(book_details) == 0:
        print("No Book Details")
        Issue_Book()
    if int(stu_details[8]) < 1:
        print("He Took 2 Books and not allowed to take more books")
        Issue_Book()
    elif int(book_details[4]) < 1:
        print("Book is out of stock in our Library!")
        Issue_Book()
    today = datetime.date.today()
    valid = today + datetime.timedelta(days = 7)
    week = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
    if week[valid.weekday()] == "Sunday":
        valid = today + datetime.timedelta(days = 8)
    
    data = usn + '|' + book_id + '|' + str(today) + '|' + str(valid) + '$'
    f = open("book_issue.txt" , "a")
    f.write(data)
    f.close()
    dt.decrease_student_book_count_by_one(usn)
    dt.decrease_book_count_in_stock_by_one(book_id)
    print("----------Book Issued Successfully ----------")
    after_login()



def Return_Book():
    pass

def Missplace_Book():
    pass

def Student_Details():
    pass

def Collect_Due():
    pass

def main_function():
    print("--------- Welcome Librarian ----------")
    username = input("Enter Your Username :")
    password = getpass.getpass("Enter Your Password :")
    if username == "admin" and password == "admin":
        after_login()
    else:
        print("Sorry! Invalid Password")
        main_function()

def after_login():
    data = ["1.Add Book","2.Update Book","3.Issue a Book",
            "4.Update Book return Status","5.Rise Missplace of a Book Issue",
            "6.Check Student Details","7.Collect Due from Student","8.Logout"]
    print("---------- Login Success ----------")
    table = dt.get_pretty_table(data)
    print(table)
    ch = int(input("Enter Your choice :"))
    if ch == 1:
        Add_Book()
    elif ch == 2:
        Update_Book()
    elif ch == 3:
        Issue_Book()
    elif ch == 4:
        Return_Book()
    elif ch == 5:
        Missplace_Book()
    elif ch == 6:
        Student_Details()
    elif ch == 7:
        Collect_Due()
    else:
        exit()