import mysql.connector

def createTableBooks(connection):
    # connection = mysql.connector.connect(host='localhost', database='books', user='root', password='manu')

    createBooksQuery = connection.cursor()
    createBooksQuery.execute("CREATE TABLE Books (BookID int(255) NOT NULL, "
                             "BookName varchar(100) NOT NULL, "
                             "AuthorName varchar(100) NOT NULL, "
                             "NoOfCopies int(10) NOT NULL, "
                             "BooksAvailable int(10) NOT NULL, "
                             "BooksIssued int(10) NOT NULL) ")

    print("Table Create Successfully!!")


def addBooks(connection, bookName, authorName, noOfCopies, booksAvailable, booksIssued):
    # connection = mysql.connector.connect(host='localhost', database='books', user='root', password='manu')

    addBooksQuery = connection.cursor()

    sql = "INSERT INTO Books (BookID, BookName, AuthorName, NoOfCopies, BooksAvailable, BooksIssued) Values (%s, %s, %s, %s, %s, %s)"
    val = ("1", bookName, authorName, noOfCopies, booksAvailable, booksIssued)

    addBooksQuery.execute(sql, val)
    connection.commit()

    print(addBooksQuery.rowcount, "Book Added Successfully!!")


def deleteBooks(connection):
    # connection = mysql.connector.connect(host='localhost', database='books', user='root', password='manu')

    deleteBookQuery = connection.cursor()

    sql = "DELETE FROM Books where BookID =" + "1"

    deleteBookQuery.execute(sql)
    connection.commit()

    print(deleteBookQuery.rowcount, "Records Deleted!")


def updateBook(connection):
    # connection = mysql.connector.connect(host='localhost', database='books', user='root', password='manu')

    updateBookQuery = connection.cursor()

    bookname = 'James Gosling Java'
    sql = "UPDATE Books SET BookName = '" + bookname + "'WHERE BookID =" + "1"

    updateBookQuery.execute(sql)
    connection.commit()

    print(updateBookQuery.rowcount, "Book Updated Successfully!!")


def bookDetails(connection):
    bookDetailsQuery = connection.cursor()

    sql = "SELECT * from Books"

    bookDetailsQuery.execute(sql)




