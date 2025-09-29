class Book:
    def __init__(self, title, subject):
        self.title = title
        self.subject = subject
        self.available = True
        self.reserved_by = None


class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.issued_books = []
        self.fine = 0

    def issue_book(self, book):
        self.issued_books.append(book)

    def return_book(self, book, days_held):
        index = -1
        for i in range(len(self.issued_books)):
            if self.issued_books[i].title == book.title:
                index = i
                break
        if index != -1:
            self.issued_books.pop(index)
        if days_held > 14:
            self.fine += (days_held - 14) * 2

    def display_dashboard(self):
        print("Roll No:", self.roll)
        print("Name:", self.name)
        print("Books Issued:")
        for b in self.issued_books:
            print(" -", b.title)
        print("Fine Due:", self.fine)


class Library:
    def __init__(self):
        self.books = []
        self.students = []
        self.logs = []

    def register_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        self.students.append(Student(roll, name))
        print("Student registered successfully!")

    def add_book(self):
        title = input("Enter Book Title: ")
        subject = input("Enter Subject: ")
        self.books.append(Book(title, subject))
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter Book Title to Remove: ")
        for i in range(len(self.books)):
            if self.books[i].title == title:
                self.books.pop(i)
                print("Book removed.")
                return
        print("Book not found!")

    def issue_book(self):
        roll = input("Enter Roll No: ")
        title = input("Enter Book Title: ")
        student = self.find_student(roll)
        book = self.find_book(title)
        if student and book:
            if book.available:
                book.available = False
                student.issue_book(book)
                self.logs.append([roll, title, "Issued"])
                print("Book issued!")
            else:
                print("Book not available!")
        else:
            print("Student or Book not found!")

    def return_book(self):
        roll = input("Enter Roll No: ")
        title = input("Enter Book Title: ")
        days = int(input("Enter Days Held: "))
        student = self.find_student(roll)
        book = self.find_book(title)
        if student and book:
            book.available = True
            student.return_book(book, days)
            self.logs.append([roll, title, "Returned"])
            print("Book returned!")
        else:
            print("Student or Book not found!")

    def reserve_book(self):
        roll = input("Enter Roll No: ")
        title = input("Enter Book Title: ")
        book = self.find_book(title)
        if book:
            if not book.available:
                book.reserved_by = roll
                print("Book reserved.")
            else:
                print("Book is available, no need to reserve.")
        else:
            print("Book not found!")

    def search_book(self):
        keyword = input("Enter keyword to search: ")
        found = False
        for b in self.books:
            if keyword in b.title or keyword in b.subject:
                found = True
                print("Found:", b.title, "| Available:", b.available)
        if not found:
            print("No book found.")

    def check_availability(self):
        title = input("Enter Book Title: ")
        book = self.find_book(title)
        if book:
            print("Available" if book.available else "Not Available")
        else:
            print("Book not found!")

    def student_dashboard(self):
        roll = input("Enter Roll No: ")
        student = self.find_student(roll)
        if student:
            student.display_dashboard()
        else:
            print("Student not found!")

    def usage_report(self):
        print("---- Library Usage Report ----")
        for log in self.logs:
            print("Roll:", log[0], "Book:", log[1], "Action:", log[2])

    def find_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                return s
        return None

    def find_book(self, title):
        for b in self.books:
            if b.title == title:
                return b
        return None


def menu():
    print("\n--- Library Management System ---")
    print("1. Register Student")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Reserve Book")
    print("7. Search Book")
    print("8. Check Book Availability")
    print("9. Student Dashboard")
    print("10. Library Usage Report")
    print("0. Exit")


lib = Library()
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        lib.register_student()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.issue_book()
    elif choice == "5":
        lib.return_book()
    elif choice == "6":
        lib.reserve_book()
    elif choice == "7":
        lib.search_book()
    elif choice == "8":
        lib.check_availability()
    elif choice == "9":
        lib.student_dashboard()
    elif choice == "10":
        lib.usage_report()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
