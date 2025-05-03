class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        self.__available = True
        print(f"You have returned '{self.title}'")

    def is_available(self):
        return self.__available

    def display(self):
        status = "Available" if self.__available else "Borrowed"
        print(f"{self.title} by {self.author} - {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        with open("books.txt", "a") as file:
            file.write(f"{title.strip()}|{author.strip()}|True\n")
        print(f"Added '{title}' by {author} to the library.")

    def show_books(self):
        print("\nLibrary Collection:")
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    title, author, available = line.strip().split("|")
                    print(f"Title: {title}, Author: {author}, Available: {available}")
        except FileNotFoundError:
            print("No books available yet.")

    def borrow_books(self, title):
        updated_lines = []
        found = False

        with open("books.txt", "r") as file:
            for line in file:
                t, a, avail = line.strip().split("|")
                if t.strip() == title.strip():
                    if avail.strip() == "True":
                        updated_lines.append(f"{t.strip()}|{a.strip()}|False\n")
                        print(f"You have borrowed '{title}'")
                    else:
                        updated_lines.append(line)
                        print(f"Sorry, '{title}' is already borrowed.")
                    found = True
                else:
                    updated_lines.append(line)

        with open("books.txt", "w") as file:
            file.writelines(updated_lines)

        if not found:
            print(f"'{title}' not found in library.")

    def return_book(self, title):
        updated_lines = []
        found = False

        with open("books.txt", "r") as file:
            for line in file:
                t, a, avail = line.strip().split("|")
                if t.strip() == title.strip():
                    if avail.strip() == "False":
                        updated_lines.append(f"{t.strip()}|{a.strip()}|True\n")
                        print(f"You have returned '{title}'")
                    else:
                        updated_lines.append(line)
                        print(f"'{title}' was not borrowed.")
                    found = True
                else:
                    updated_lines.append(line)

        with open("books.txt", "w") as file:
            file.writelines(updated_lines)

        if not found:
            print(f"'{title}' not found in library.")


# Menu-driven interaction
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    try:
        choice = int(input("What operation do you want to perform? "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == 2:
        library.show_books()
    elif choice == 3:
        title = input("Enter book title to borrow: ")
        library.borrow_books(title)
    elif choice == 4:
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == 5:
        print("Exiting... Bye!!!")
        break
    else:
        print("Invalid choice. Try again.")
