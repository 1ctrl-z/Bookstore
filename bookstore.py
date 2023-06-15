import sqlite3

# Connect to the database and create a cursor
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

def add_new():

    """
    This function adds a new book to a database if it doesn't already exist.
    """

    while True:
        try:
            book_id = int(input("Enter the ID of the book: "))
            break
        except ValueError:
            print("Invalid Entry, please try again")

    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    existing_book = cursor.fetchone()

    if existing_book:
        print("Book with the same ID already exists.")
    else:
        book_title = input("Enter the Title of the book: ")
        book_author = input("Enter the Author of the book: ")
        while True:
            try:
                book_qty = int(input("Enter the Quantity of the book: "))
                break
            except ValueError:
                print("Invalid Entry, please try again")

        cursor.execute('INSERT INTO books VALUES (?, ?, ?, ?)', (book_id, book_title, book_author, book_qty))
        db.commit()
        print('Book inserted successfully.')

def update_book():

    """
    This function updates the information of a book in a database based on user input.
    """

    while True:
        try:
            book_id = int(input("Enter the ID of the book you want to update: "))
            break
        except ValueError:
            print("Invalid Entry, please try again")

    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if book:
        title = input("Enter the new title of the book: ")
        author = input("Enter the new author of the book: ")
        while True:
            try:
                qty = int(input("Enter the new quantity of the book: "))
                break
            except ValueError:
                print("Invalid Entry, please try again")

        cursor.execute("UPDATE books SET title=?, author=?, qty=? WHERE id=?", (title, author, qty, book_id))
        db.commit()
        print("Book updated successfully!")
    else:
        print("Book not found!")

def delete_book():

    """
    This function deletes a book from a database based on the user input of the book's ID.
    """

    while True:
        try:
            book_id = int(input("Enter the ID of the book you want to delete: "))
            break
        except ValueError:
            print("Invalid Entry, please try again")

    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if book:
        cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        db.commit()
        print("Book deleted successfully!")
    else:
        print("Book not found!")

def search_book():
    book_title = input("Enter the title of the book you want to search for: ")

    cursor.execute("SELECT * FROM books WHERE title=?", (book_title,))
    books = cursor.fetchall()

    if books:
        print("Matching books found:")
        for book in books:
            print(f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nQuantity: {book[3]}\n")
    else:
        print("No matching books found!")

def view_all_books():

    """
    This function retrieves all books from a database and prints their details.
    """

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if books:
        print("\nAll books in the database:\n")
        for book in books:
            print(f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nQuantity: {book[3]}\n")
    else:
        print("No books found in the database.")

# Creating the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
''')

# Defining the current book data
book_info = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
]
cursor.executemany('INSERT INTO books VALUES (?, ?, ?, ?)', book_info)

print("\nWelcome to the Bookstore Clerk Program")
menu_ = '''\nSelect one of the following options below:
    1. Add new book
    2. Update book information
    3. Delete book
    4. Search for a book
    5. View all books
    0. Exit
    : '''

# This is a loop that displays a menu of options to the user and waits for their input. Depending on
# the input, it calls one of the functions defined earlier in the code (`add_new()`, `update_book()`,
# `delete_book()`, `search_book()`, `view_all_books()`) or exits the loop if the input is "0". If the
# input is not recognised, it prints an error message and displays the menu again. This loop allows
# the user to interact with the program and perform various operations on the book database.
while True:
    menu = input(menu_)

    if menu == "1":
        add_new()
    elif menu == "2":
        update_book()
    elif menu == "3":
        delete_book()
    elif menu == "4":
        search_book()
    elif menu == "5":
        view_all_books()
    elif menu == "0":
        break
    else:
        print("Invalid choice. Please try again.")

# `db.close()` is closing the connection to the SQLite database.
db.close()
