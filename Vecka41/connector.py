# connector - connect.py

__author__ = 'MichelSkoglund'

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connect = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        database='person')
    print(2 * '\n', "Det Funkar!! Du har lyckats att koppla Dig till Din databas!", 2 * '\n')

except mysql.connector.Error as e:

    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(2 * '\n', "Kopplingen fungerar inte!", 2 * '\n')

    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print(2 * '\n', "Databas namn hittades inte!!", 2 * '\n')

    else:
        print(e)

#--------------------------------------------------------------

# SQl insert -  insert.py

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='person',
                                         user='root',
                                         password='root')

    sql_insert_query = ''' INSERT INTO person                                                                                                                                                               
                              (name) VALUES ('Michel skoglund') '''

    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query)
    connection.commit()

    print("Namn lagrats i person tabellen")

except mysql.connector.Error as error:
    connection.rollback()  # rollback if any exception occured
    print("Lagring misslyckades {}".format(error))
finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL koppling nerkopplad")
