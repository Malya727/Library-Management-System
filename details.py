from prettytable import PrettyTable

def get_student_by_usn(USN):
    f = open("students.txt" , "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if USN == li2[0]:
            return li2
    return []

def get_pretty_table(li):
    table = PrettyTable()
    table.field_names = ["Enter Your Choice"]
    for i in li:
        table.add_row([i])
    return table

def get_book_by_id(bookid):
    f = open("Book_Details.txt" , "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if bookid == li2[1]:
            return li2
    return [] 

def decrease_student_book_count_by_one(usn):
    f = open("students.txt" , "r")
    data = f.read()
    f.close()
    res = []
    li = data.split('$')
    li.pop()
    for l in li:
        li1 = l.split('|')
        if li1[0] == usn:
            li1[8] = str(int(li1[8]) - 1)
            res.append('|'.join(li1))
        else:
            res.append(l)
    result = '$'.join(res) + '$'
    f = open("students.txt" , "w")
    f.write(result)
    f.close()

def increase_student_book_count_by_one(usn):
    f = open("students.txt" , "r")
    data = f.read()
    f.close()
    res = []
    li = data.split('$')
    li.pop()
    for l in li:
        li1 = l.split('|')
        if li1[0] == usn:
            li1[8] = str(int(li1[8]) + 1)
            res.append('|'.join(li1))
        else:
            res.append(l)
    result = '$'.join(res) + '$'
    f = open("students.txt" , "w")
    f.write(result)
    f.close()

def decrease_book_count_in_stock_by_one(bookid):
    f = open("Book_Details.txt" , "r")
    data = f.read()
    f.close()
    res = []
    li = data.split('$')
    li.pop()
    for l in li:
        li1 = l.split('|')
        if li1[1] == bookid:
            li1[4] = str(int(li1[4]) - 1)
            res.append('|'.join(li1))
        else:
            res.append(l)
    result = '$'.join(res) + '$'
    f = open("Book_Details.txt" , "w")
    f.write(result)
    f.close()

def increase_book_count_in_stock_by_one(bookid):
    f = open("Book_Details.txt" , "r")
    data = f.read()
    f.close()
    res = []
    li = data.split('$')
    li.pop()
    for l in li:
        li1 = l.split('|')
        if li1[1] == bookid:
            li1[4] = str(int(li1[4]) + 1)
            res.append('|'.join(li1))
        else:
            res.append(l)
    result = '$'.join(res) + '$'
    f = open("Book_Details.txt" , "w")
    f.write(result)
    f.close()

def student_details_in_pretty_table(usn):
    stu_data = get_student_by_usn(usn)
    table = PrettyTable()
    table.field_names = ["USN" , "Name" , "Address" , "Phone Number" , "Total Due" , "Total Due Paid" , "Due Pending" , "Book Student Can Take"]
    table.add_row([stu_data[0] , stu_data[1] , stu_data[2] , stu_data[3] , stu_data[5] , stu_data[6] , stu_data[7] , stu_data[8]])
    return table

