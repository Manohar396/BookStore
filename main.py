import Connection
import Books
import os


def getLoginDetails():
    os.system('cls')
    print("---Welcome to VMR Books Store---")
    print("1. Login To Your Account")
    print("2. Exit")

    choice1 = input("Enter Your Choice (1 or 2): ")

    if choice1 == "1":
        userName = input("Enter User Name: ")
        userPassword = input("Enter Password: ")
        validateLibrarianDetails(userName, userPassword)
    else:
        exit(0)


def validateLibrarianDetails(userName, pswd):
    if userName == "Manohar" and pswd == "1234":
        print("User Logged In Successfully!!!")

    else:
        print("Login Failed!!")
        getLoginDetails()


def selectTransactionType(connection):
    os.system('cls')
    print("---Book Store Transactions---")
    print("1. Books Transaction")
    print("2. Customers Transaction")
    print("3. Sign-out")

    transactionTypeChoice = input("Enter Your Choice: ")

    if transactionTypeChoice == "1":
        booksTransactions(connection)
    elif transactionTypeChoice == "2":
        print("Development In Progress")
    elif transactionTypeChoice == "3":
        print("Signed-out Successfully!!!")
    else:
        print("Invalid Choice!!!")
        selectTransactionType()


def booksTransactions(connection):
    os.system('cls')
    print("---Book Transactions---")
    print("1. Add New Book")
    print("2. Update Book Details")
    print("3. List All Books")
    print("4. Delete Existing Book")
    print("5. Issue a Book to Customer")
    print("6. Search a Book")
    print("7. Exit")

    choice2 = input("Enter Your Choice: ")

    if choice2 == "1":
        print("---Adding New Book---")
        bookName = input("Enter Book Name: ")
        authorName = input("Enter Author Name: ")
        noOfCopies = input("Enter Total Copies: ")
        booksAvailable = input("Enter Total Books Available: ")
        booksIssued = input("Enter Total Books Issued: ")

        Books.addBooks(connection, bookName, authorName, noOfCopies, booksAvailable, booksIssued)
        booksTransactions(connection)

    elif choice2 == "2":
        print("---Updating Book Details---")
        bookID = input("Enter Book ID: ")

        print("---Update Transactions---")
        print("1. Update Book Name")
        print("2. Update Author Name")
        print("3. Updating Total Copies: ")
        print("4. Exit")
        updateBookChoice = input("Enter Your Choice: ")

        if updateBookChoice == "1":
            print("---Updating Book Name---")
            bookName = input("Enter Book Name: ")
            Books.updateBookName(connection, bookID, bookName)
            booksTransactions(connection)
        elif updateBookChoice == "2":
            print("---Updating Author Name---")
            authorName = input("Enter Author Name: ")
            Books.updateAuthorName(connection, bookID, authorName)
            booksTransactions(connection)
        elif updateBookChoice == "3":
            print("---Updating Total Copies---")
            noOfCopies = input("Enter Total Copies: ")
            Books.updateNoOfCopies(connection, bookID, noOfCopies)
            booksTransactions(connection)
        elif updateBookChoice == "4":
            booksTransactions(connection)
        else:
            print("Entered Invalid Choice!!!")
            booksTransactions(connection)

    elif choice2 == "7":
        selectTransactionType(connection)
    else:
        print("Enter Valid Choice!!!")
        booksTransactions(connection)


if __name__ == "__main__":
    host = 'localhost'
    database = 'books'
    username = 'root'
    password = 'manu'

    sqlConnection = Connection.sqlConnection(host, database, username, password)

    getLoginDetails()
    selectTransactionType(sqlConnection)

    Connection.sqlConnectionClose(sqlConnection)
