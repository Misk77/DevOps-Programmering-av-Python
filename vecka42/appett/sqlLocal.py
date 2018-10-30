import mysql
import mysql.connector
from mysql.connector import errorcode
from appett.funktioner import on_closing

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
from tkinter import *

__author__ = 'Michel Skoglund'


def sqlConnector():
    root = Tk()
    try:
        connect = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='')
        label = Label(root, text=str(2 * '\n') + "Det Funkar!! Du har lyckats att koppla Dig till Din databas!" + str(
            2 * '\n'))
        label.pack()

    except mysql.connector.Error as e:

        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            label = Label(root, text=str(2 * '\n') + "Kopplingen fungerar inte!" + str(2 * '\n'))
            label.pack()


        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            label = Label(root, text=str(2 * '\n') + "Databas namn hittades inte!!" + str(2 * '\n'))
            label.pack()


        else:
            label = Label(root, text=str(e))
            label.pack()

    root.mainloop()


# SQl create Database
def createDatabase():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' CREATE DATABASE profiles;  '''
        label = Label(root, text='{}'.format(sql_insert_query))
        label.pack()

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Databasen skapades")
        label.pack()



    except mysql.connector.Error as error:

        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Databasen skapades misslyckades " + str(error))
        label.pack()


    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()

    root.mainloop()


# SQl DROP DATABASE


def dropDatabase():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' DROP DATABASE profiles;  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Databasen deleted")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Databasen delete misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# Drop table

def dropTables():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='root',
                                             passwd='root',
                                             host='localhost',
                                             db='')

        sql_insert_query = ''' 
DROP TABLE profiles;
  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="DROP TABLE profiles lyckades local{}".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="DROP TABLE misslyckades {} local".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad local")
            label.pack

    root.mainloop()


# Sql create Tables -
def createTables():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='profiles',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' 
CREATE  TABLE profiles
( first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email VARCHAR(60) NOT NULL,
age VARCHAR(15) NOT NULL,
yrke VARCHAR(30)NOT NULL,
country VARCHAR(30)NOT NULL,
hobbies VARCHAR(30)NOT NULL,
lenght VARCHAR(30)NOT NULL,
sex ENUM('M','F') NOT NULL,
date_entered TIMESTAMP,
profiles_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)
default character set= utf8;
  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="CREATED TABLE profiles skapades {}".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="CREATED TABLE misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack

    root.mainloop()


# SQl insert -  insert.py


def insertQuery():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='profiles',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' INSERT INTO profiles VALUE 
('Michel','skoglund','michelskoglund@hotmail.com','41','student','sweden','gitarrer','178','M',NOW(),NULL); '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Profil har lagrats i profiles tabellen {}".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Lagring misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()

    root.mainloop()


# SQl show databases -  show databases.py


def showDb():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='profiles',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' show databases; '''

        cursor = connection.cursor()

        cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        label = Label(root, text="SHOW databases körs")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="SHOW databases misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# USE  profiles

def useProfiles():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' USE profiles; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Database changed,  {}".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="USE profiles  misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


def selectDB():
    from tkinter import ttk

    root = Tk()

    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             database='profiles',
                                             password='root')

        sql_insert_query = ''' SELECT DATABASE (); '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()
        choices = ['GB', 'MB', 'KB']
        variable = StringVar(root)
        variable.set('GB')

        w = Checkbutton(root, values=choices)
        w.pack();

        label = Label(root, text="SELECT DATABASE profiles")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="SELECT DATABASE  misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


def describeTable():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             database='profiles',
                                             password='root')

        sql_insert_query = ''' DESCRIBE profiles; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        label = Label(root, text="DESCRIBE profile")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="DESCRIBE profiles misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# Read from Ddatabase
def readFromDB():
    root = Tk()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='profiles',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' SELECT * FROM profiles '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        for row in cursor.fetchall():
            label = Label(root, text=str(row))
            label.pack()

            label = Label(root, text="Reading Database now")
            label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Read from Database  misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()
