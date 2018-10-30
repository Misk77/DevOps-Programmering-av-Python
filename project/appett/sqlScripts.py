import mysql
import mysql.connector
from mysql.connector import errorcode

# showdatabases;
# use person;
# CREATE TABLE person(id INT NOT NULL AUTO_INCREMENT,name CHAR(255) NOT NULL,PRIMARY KEY (id)deafult charactet set= utf8);
# CREATE TABLE person(id INT NOT NULL AUTO_INCREMENT,name CHAR(255) NOT NULL,PRIMARY KEY (id));  ## Works
# show tables;

# create table person int auto_increment primary key, name varchar(255)default character set utf-8; #some wrongs
# desc person;
# show databases;
# use person;
# alter, ändra
# insert into tablename set name="Kalle karlsson";
# update tablename add column email varchar(255)

# connector - connect.py
# DBconnector - connect.py

__author__ = 'Michel Skoglund'


def sqlConnector():
    try:
        connect = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='')
        print(2 * '\n', "Det Funkar!! Du har lyckats att koppla Dig till Din databas!", 2 * '\n')

    except mysql.connector.Error as e:

        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(2 * '\n', "Kopplingen fungerar inte!", 2 * '\n')

        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print(2 * '\n', "Databas namn hittades inte!!", 2 * '\n')

        else:
            print(e)


# SQl create Database
def createDatabase():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' CREATE DATABASE person;  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        print("Databasen skapades")

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Databasen skapades misslyckades {}".format(error))
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")


# SQl DROP DATABASE


def dropDatabase():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' DROP DATABASE person;  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        print("Databasen deleted")

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Databasen delete misslyckades {}".format(error))
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")


# Sql create Tables -
def createTables():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='person',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' create table person(id int not null auto_increment primary key,name varchar(255)) default character set= utf8;
  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        print("CREATED TABLE person skapades")

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Tables skapades misslyckades {}".format(error))
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")


# SQl insert -  insert.py


def insertQuery():
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
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")


# SQl show databases -  show databases.py


def showDb():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='person',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' show databases; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        print("show databases GÖRS")

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("show databases misslyckades {}".format(error))
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")


# USE  person

def usePerson():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' use person; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        print("Database changed, Use person now")

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("USE person  misslyckades {}".format(error))
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")


# Read from Ddatabase
def readFromDB():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='person',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' Select * FROM person '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        for row in cursor.fetchall():
            print(row)

        print("Reading Database now")

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Read from Ddatabase  misslyckades {}".format(error))
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL koppling nerkopplad")
