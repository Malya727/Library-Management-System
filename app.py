import student as st
import librarian as lb
import details as dt

def main_function():
    print("---------- Welcome to Library ----------")
    table = dt.get_pretty_table(["1.Librarian" , "2.Student"])
    print(table)
    choice = int(input("Enter Your Choice :"))
    if choice == 1:
        #calls library function
        lb.main_function()
    elif choice == 2:
        st.main_function()
    else:
        print("Invalid Choice!")
        exit()

if __name__ == "__main__":
    main_function()

