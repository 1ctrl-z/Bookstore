# Bookstore

The given code is an example of a simple Bookstore Clerk program that allows the user to perform various operations on a book database using SQLite. Here's a breakdown of the code:

Importing the required module: sqlite3
Connecting to the database and creating a cursor
Defining functions for different operations:

add_new(): Prompts the user to enter the details of a new book and adds it to the database if it doesn't already exist.
update_book(): Prompts the user to enter the ID of a book they want to update and allows them to modify its information.
delete_book(): Prompts the user to enter the ID of a book they want to delete and removes it from the database.
search_book(): Prompts the user to enter the title of a book they want to search for and displays the matching books.
view_all_books(): Retrieves all books from the database and prints their details.

Creating the database table if it doesn't exist

Inserting initial book data into the database

Displaying the main menu and executing user-selected operations:

The program presents a menu of options to the user and waits for their input.
Depending on the input, the corresponding function is called to perform the desired operation.
If the input is not recognized, an error message is displayed, and the menu is shown again.
The loop continues until the user chooses to exit by entering "0".

Closing the database connection

Overall, the code provides a basic interface for managing a book database by allowing the user to add new books, update existing books, delete books, search for books, and view all books. It demonstrates the use of SQLite and provides a structure that can be expanded upon for more complex bookstore management functionality.
