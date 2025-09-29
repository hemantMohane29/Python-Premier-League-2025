import tkinter as tk
from tkinter import messagebox


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
        for i in range(len(self.issued_books)):
            if self.issued_books[i].title == book.title:
                self.issued_books.pop(i)
                break
        if days_held > 14:
            self.fine += (days_held - 14) * 2


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.students = []
        self.books = []
        self.logs = []

        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self.root, text="Library Management System", font=("Arial", 16, "bold")).pack(pady=10)

        btns = [
            ("Register Student", self.register_student_ui),
            ("Add Book", self.add_book_ui),
            ("Issue Book", self.issue_book_ui),
            ("Return Book", self.return_book_ui),
            ("Check Availability", self.check_availability_ui),
            ("Student Dashboard", self.student_dashboard_ui),
            ("Usage Report", self.usage_report_ui),
        ]

        for (text, command) in btns:
            tk.Button(self.root, text=text, width=25, command=command).pack(pady=4)

    def register_student_ui(self):
        self._clear()
        tk.Label(self.root, text="Register Student").pack()
        tk.Label(self.root, text="Roll No:").pack()
        roll = tk.Entry(self.root)
        roll.pack()
        tk.Label(self.root, text="Name:").pack()
        name = tk.Entry(self.root)
        name.pack()
        tk.Button(self.root, text="Register", command=lambda: self.register_student(roll.get(), name.get())).pack(pady=5)

    def add_book_ui(self):
        self._clear()
        tk.Label(self.root, text="Add Book").pack()
        tk.Label(self.root, text="Title:").pack()
        title = tk.Entry(self.root)
        title.pack()
        tk.Label(self.root, text="Subject:").pack()
        subject = tk.Entry(self.root)
        subject.pack()
        tk.Button(self.root, text="Add", command=lambda: self.add_book(title.get(), subject.get())).pack(pady=5)

    def issue_book_ui(self):
        self._clear()
        tk.Label(self.root, text="Issue Book").pack()
        tk.Label(self.root, text="Roll No:").pack()
        roll = tk.Entry(self.root)
        roll.pack()
        tk.Label(self.root, text="Book Title:").pack()
        title = tk.Entry(self.root)
        title.pack()
        tk.Button(self.root, text="Issue", command=lambda: self.issue_book(roll.get(), title.get())).pack(pady=5)

    def return_book_ui(self):
        self._clear()
        tk.Label(self.root, text="Return Book").pack()
        tk.Label(self.root, text="Roll No:").pack()
        roll = tk.Entry(self.root)
        roll.pack()
        tk.Label(self.root, text="Book Title:").pack()
        title = tk.Entry(self.root)
        title.pack()
        tk.Label(self.root, text="Days Held:").pack()
        days = tk.Entry(self.root)
        days.pack()
        tk.Button(self.root, text="Return", command=lambda: self.return_book(roll.get(), title.get(), days.get())).pack(pady=5)

    def check_availability_ui(self):
        self._clear()
        tk.Label(self.root, text="Check Book Availability").pack()
        tk.Label(self.root, text="Book Title:").pack()
        title = tk.Entry(self.root)
        title.pack()
        tk.Button(self.root, text="Check", command=lambda: self.check_availability(title.get())).pack(pady=5)

    def student_dashboard_ui(self):
        self._clear()
        tk.Label(self.root, text="Student Dashboard").pack()
        tk.Label(self.root, text="Roll No:").pack()
        roll = tk.Entry(self.root)
        roll.pack()
        tk.Button(self.root, text="View", command=lambda: self.view_dashboard(roll.get())).pack(pady=5)

    def usage_report_ui(self):
        self._clear()
        tk.Label(self.root, text="Usage Report", font=("Arial", 12, "bold")).pack()
        report = tk.Text(self.root, height=15, width=60)
        report.pack()
        report.insert(tk.END, "Roll\tBook\tAction\n")
        for log in self.logs:
            report.insert(tk.END, f"{log[0]}\t{log[1]}\t{log[2]}\n")

    def register_student(self, roll, name):
        self.students.append(Student(roll, name))
        messagebox.showinfo("Success", "Student Registered")

    def add_book(self, title, subject):
        self.books.append(Book(title, subject))
        messagebox.showinfo("Success", "Book Added")

    def issue_book(self, roll, title):
        student = self.find_student(roll)
        book = self.find_book(title)
        if student and book and book.available:
            student.issue_book(book)
            book.available = False
            self.logs.append([roll, title, "Issued"])
            messagebox.showinfo("Success", "Book Issued")
        else:
            messagebox.showerror("Error", "Issue Failed")

    def return_book(self, roll, title, days_held):
        student = self.find_student(roll)
        book = self.find_book(title)
        if student and book:
            book.available = True
            try:
                days = int(days_held)
            except:
                days = 0
            student.return_book(book, days)
            self.logs.append([roll, title, "Returned"])
            messagebox.showinfo("Success", "Book Returned")
        else:
            messagebox.showerror("Error", "Return Failed")

    def check_availability(self, title):
        book = self.find_book(title)
        if book:
            msg = "Available" if book.available else "Not Available"
        else:
            msg = "Book Not Found"
        messagebox.showinfo("Check Result", msg)

    def view_dashboard(self, roll):
        student = self.find_student(roll)
        if student:
            info = f"Name: {student.name}\nFine: {student.fine}\nBooks Issued:\n"
            for b in student.issued_books:
                info += f"- {b.title}\n"
            messagebox.showinfo("Dashboard", info)
        else:
            messagebox.showerror("Error", "Student not found")

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

    def _clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_main_menu()


# Run the GUI App
root = tk.Tk()
app = LibraryApp(root)
root.geometry("400x500")
root.mainloop()
