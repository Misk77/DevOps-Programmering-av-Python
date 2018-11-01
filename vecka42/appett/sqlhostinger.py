import mysql
import mysql.connector
from mysql.connector import errorcode
from tkinter import *
import sshtunnel

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
"""

MySQL server hostname is: sql150.main-hosting.eu.
DATABASE                USERNAME
u209758462_miskb	u209758462_misk7
host: sql150.main-hosting.eu.

Email: michelskoglund@hotmail.se

"""

__author__ = 'Michel Skoglund'


def sqlhostingConnector():
    root = Tk()
    try:
        connect = mysql.connector.connect(
            user='u209758462_misk7',
            passwd='mi235277sk',
            host='sql150.main-hosting.eu',
            db='')
        label = Label(root, text=str(
            2 * '\n') + "Det Funkar!! Du har lyckats att koppla Dig till Din databas! på hosting.eu" + str(
            2 * '\n'))
        label.pack()

    except mysql.connector.Error as e:

        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            label = Label(root,
                          text=str(
                              2 * '\n') + "Kopplingen fungerar inte!\n hosting.eu" + str(
                              2 * '\n'))
            label.pack()


        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            label = Label(root, text=str(
                2 * '\n') + "Databas namn hittades inte!! \nhosting.eu" + str(2 * '\n'))
            label.pack()


        else:
            label = Label(root, text='\n' + str(e))
            label.pack()

    root.mainloop()


# SQl create Database # Cant create database at db4free  No Privileges
def sqlhostingCreateDatabase():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='')

        sql_insert_query = ''' CREATE DATABASE u209758462_miskb;  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Databasen skapades hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Databasen skapades misslyckades hosting.eu." + str(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# SQl DROP DATABASE


def sqlhostingDropDatabase():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' DROP DATABASE u209758462_miskb;  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Databasen deleted hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Databasen delete misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# Sql create Tables -
def sqlhostingCreateTables():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

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

        label = Label(root, text="CREATED TABLE profiles skapades {} hosting.eu.".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="CREATED TABLE profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack
    root.mainloop()


# DROP TABLE
def sqlhostingDropTables():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' 
DROP TABLE profiles;
  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="DROP TABLE profiles lyckades {} hosting.eu.".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="DROP TABLE misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad ")
            label.pack

    root.mainloop()


# SQl insert -  insert.py


def sqlhostingInsertQuery():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' INSERT INTO profiles VALUE 
('Michel','skoglund','michelskoglund@hotmail.com','41','student','sweden','gitarrer','178','M',NOW(),NULL); '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="profiles VALUE  har lagrats i tabellen hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Lagring i profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()

    root.mainloop()


# SQl show databases -  show databases.py


def sqlhostingShowDb():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='')

        sql_insert_query = ''' show databases; '''

        cursor = connection.cursor()

        cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        label = Label(root, text="SHOW databases körs hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="SHOW databases misslyckades {} db4free.nethosting.eu.")
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()


# USE  database miskdb

def sqlhostingUsedatabase():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' USE u209758462_miskb	; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Database changed, USE miskdb now hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="USE Database miskdb misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu.MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


def sqlhostingSelectDB():
    from tkinter import ttk

    root = Tk()

    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

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

        label = Label(root, text="SELECT DATABASE miskdb hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="SELECT DATABASE miskdb misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


def sqlhostingDescribeTable():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' DESCRIBE profiles; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        label = Label(root, text="DESCRIBE profile db4free.net")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="DESCRIBE profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# Read from Ddatabase
def sqlhostingReadFromDB():
    root = Tk()
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

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

            label = Label(root, text="Reading profiles now dhosting.eu.")
            label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Reading profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
