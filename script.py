from mylib import *

while True:
    print("\n----------------------------------------------------------------")
    print("Library")
    print("\n[1] - Add book")
    print("[2] - View books")
    print("[3] - View returned books")
    print("[4] - View loaned books")
    print("[5] - Remove book")
    print("[6] - Loan book")
    print("[7] - Return book")
    print("[8] - Add user")
    print("[9] - View users")
    print("[10] - Remove user")
    print("[11] - Exit")

    r = input("\nWhat option do you want to perform? ")
    while not r.isdigit() or int(r) not in range(1, 12):
        print("\nInvalid option. Try again")
        r = input("What option do you want to perform? ")

    if r == "1":
        Book.add_book()
    elif r == "2":
        Book.show_books()
    elif r == "3":
        Book.returned_books()
    elif r == "4":
        Book.loaned_books()
    elif r == "5":
        Book.remove_book()
    elif r == "6":
        Book.loan_book()
    elif r == "7":
        Book.return_book()
    elif r == "8":
        User.register_user()
    elif r == "9":
        User.show_users()
    elif r == "10":
        User.remove_user()
    elif r == "11":
        exit()
