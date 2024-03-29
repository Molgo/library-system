class User():

    user_list = []
    count = 1

    def __init__(self, name, user_id) -> None:
        self.__name = name
        self.__user_id = user_id
        
    def get_name(self):
        return self.__name
    
    def get_user_id(self):
        return self.__user_id
    
    @classmethod
    def get_user_list(cls):
        return cls.user_list

    @classmethod
    def register_user(cls):
        print("\nEnter the information of the user being added:")
        name = input("Name: ")
        user_id = cls.count
        cls.count += 1
        user = User(name=name, user_id=user_id)
        cls.user_list.append(user)
        return 
      
    @classmethod
    def show_users(cls):
        if User.get_user_list() == []:
            print("\nNo users to view")
        else:
            for index, user in enumerate(User.get_user_list(), start=1):
                print(f"\n{index} - Name: {user.get_name()}")
                print(f"    ID: {user.get_user_id()}")
            return
    
    @classmethod
    def remove_user(cls):
        if User.get_user_list() == []:
            print("\nNo users to remove")
        else:
            User.show_users()
            r = input("\nEnter the name or ID of the user to remove: ")
            flag = False
            if r.isdigit():
                for user in User.get_user_list():
                    if user.get_user_id() == int(r):
                        cls.user_list.remove(user)
                        print(f"\nUser {user.get_name()} has been removed")
                        flag = True
                        break     
            else:
                for user in User.get_user_list():
                    if user.get_name().upper() == r.upper():
                        cls.user_list.remove(user)
                        print(f"\nUser {user.get_name()} has been removed")
                        flag = True
                        break
            if not flag:
                print("\nUser not found")

class Book():

    loaned_books_list = []
    returned_books_list = []

    def __init__(self, name, author, year, available) -> None:
        self.__name = name
        self.__author = author
        self.__year = year
        self.available = available
    
    def get_name(self):
        return self.__name
    
    def get_author(self):
        return self.__author
    
    def get_year(self):
        return self.__year
    
    def get_available(self):
        return self.available
    
    @classmethod
    def get_loan_list(cls):
        return cls.loaned_books_list
    
    @classmethod
    def get_return_list(cls):
        return cls.returned_books_list
    
    @classmethod
    def add_book(cls):
        print("\nEnter the information of the book being added:")
        name = input("Name: ")
        author = input("Author: ")
        year = input("Year: ")
        while not year.isdigit() or int(year) > 2024 or int(year) < 0:
            print("\nInvalid option. Try again")
            year = input("Year: ")
        book = Book(name=name, year=int(year), author=author, available=True)
        cls.returned_books_list.append(book)
        return
    
    @classmethod
    def show_books(cls):
        if Book.get_return_list() + Book.get_loan_list() == []:
            print("\nNo books to view")
        else:
            for index, book in enumerate(Book.get_return_list() + Book.get_loan_list(), start=1):
                availability = "Available" if book.get_available() == True else "Unavailable"
                print(f"\n{index} - Name: {book.get_name()}")
                print(f"    Author: {book.get_author()}")
                print(f"    Year: {book.get_year()}")
                print(f"    Availability: {availability}")
        return
    
    @classmethod
    def returned_books(cls):
        if Book.get_return_list() == []:
            print("\nNo returned books")
        else:
            for index, book in enumerate(Book.get_return_list(), start=1):
                availability = "Available" if book.get_available() == True else "Unavailable"
                print(f"\n{index} - Name: {book.get_name()}")
                print(f"    Author: {book.get_author()}")
                print(f"    Year: {book.get_year()}")
                print(f"    Availability: {availability}")
        return
    
    @classmethod
    def loaned_books(cls):
        if Book.get_loan_list() == []:
            print("\nNo loaned books")
        for index, book in enumerate(Book.get_loan_list(), start=1):
            availability = "Available" if book.get_available() == True else "Unavailable"
            print(f"\n{index} - Name: {book.get_name()}")
            print(f"    Author: {book.get_author()}")
            print(f"    Year: {book.get_year()}")
            print(f"    Availability: {availability}\n")
        return
    
    @classmethod
    def remove_book(cls):
        if Book.get_return_list() + Book.get_loan_list() == []:
            print("\nNo books to remove")
        else:
            Book.show_books()
            r = input("\nEnter the name of the book to be removed: ")
            flag = False
            for book in Book.get_return_list() + Book.get_loan_list():
                if book.get_name().upper() == r.upper():
                    flag = True
                    if book.get_available() == False:
                        cls.loaned_books_list.remove(book)
                    else:
                        cls.returned_books_list.remove(book)
                    print(f"\nThe book {book.get_name()} has been removed")
                    break
            if not flag:
                    print(f"\nBook not found")     
        return

    @classmethod
    def loan_book(cls):
        if Book.get_return_list() == []:
            print("\nNo available books to loan")
        else:
            name = input("\nEnter the name of the book to be loaned: ")
            flag = False
            for book in Book.get_return_list():
                if book.get_name().upper() == name.upper():
                    flag = True
                    if book.get_available() == True:
                        book.available = False
                        cls.returned_books_list.remove(book)
                        cls.loaned_books_list.append(book) 
                        print(f"\nThe book {book.get_name()} has been loaned")
                    else:
                        print(f"\nThe book {book.get_name()} is already marked as loaned")
            if not flag:
                print(f"\nBook not found")
        return

    @classmethod
    def return_book(cls):
        if Book.get_loan_list() == []:
            print("\nNo available books to return")
        else:
            name = input("\nEnter the name of the book to be returned: ")
            flag = False
            for book in Book.get_loan_list():
                if book.get_name().upper() == name.upper():
                    flag = True
                    if book.get_available() == False:
                        book.available = True
                        cls.loaned_books_list.remove(book) 
                        cls.returned_books_list.append(book)
                        print(f"\nThe book {book.get_name()} has been returned")
                    else:
                        print(f"\nThe book {book.get_name()} is already marked as returned")
            if not flag:
                print(f"\nBook not found")
        return