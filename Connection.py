import mysql.connector
from mysql.connector import Error


def sqlConnection(hostname, db, username, pswd):
    try:
        connection = mysql.connector.connect(host=hostname, database=db, user=username, password=pswd)

        if connection.is_connected():
            print("Connection is Successful")
            return connection
        else:
            print("Connection Failed!")
    except Error as e:
        print("Error Occurred in MySQL: ", e)


def sqlConnectionClose(connection):
    if connection.is_connected():
        connection.close()
        print("My SQL Connection is Closed!")
    else:
        print("SQL Connection is Not Open!")
