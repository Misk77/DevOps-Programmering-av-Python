from tkinter import *
import mysql
import mysql.connector
import time
from mysql.connector import errorcode


def database():
    _firstName = firstName.get()
    _lastName = lastName.get()
    _email = email.get()
    _age = age.get()
    _yrke = yrke.get()
    _country = country.get()
    _hobbies = hobbies.get()
    _lenght = lenght.get()
    _sex = sex.get()
    _date = date.get()
    _profileid = profileid.get()
    connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')
    with connection:
        cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXIST profiles(firstname TEXT,firstname TEXT,email TEXT,age INT,yrke TEXT,country TEXT,hobbies TEXT, lenght INT, sex TEXT, date INT,profilesid INT')
    cursor.execute(
        'INSERT INTO profiles (firstname,firstname,email,age,yrke,country,hobbies,lenght,sex,date,profileid) VALUES (?,?,??,?,?,?,?,?,?,?)',
        (firstName, lastName, email, age, yrke, country, hobbies, lenght, sex, date, profileid))
    connection.commit()


# def manuelInsert():
root = Tk()
root.geometry('500x500')
root.title('Manuel Insert into profiles')

firstName = StringVar()
lastName = StringVar()
email = StringVar()
age = IntVar()
yrke = StringVar()
country = StringVar()
hobbies = StringVar()
lenght = IntVar()
sex = IntVar()
date = IntVar()
profileid = IntVar()

labeltitle = Label(root, text="Insert Manuel into profiles", width=20, font=('bold', 20))
labeltitle.place(x=90, y=53)

labelFirstName = Label(root, text="First Name", width=20, font=('bold', 10))
labelFirstName.place(x=80, y=130)
entryFirstName = Entry(root, text=firstName)
entryFirstName.place(x=240, y=130)

labelLastName = Label(root, text="Last Name", width=20, font=('bold', 10))
labelLastName.place(x=75, y=150)
entryLastName = Entry(root, text=lastName)
entryLastName.place(x=240, y=150)

labelemail = Label(root, text="Email", width=20, font=('bold', 10))
labelemail.place(x=70, y=170)
entrylabelemail = Entry(root, text=email)
entrylabelemail.place(x=240, y=170)

labelage = Label(root, text="Age", width=20, font=('bold', 10))
labelage.place(x=50, y=210)
entryage = Entry(root, text=age)
entryage.place(x=240, y=210)

labelyrke = Label(root, text="yrke", width=20, font=('bold', 10))
labelyrke.place(x=50, y=230)
entryyrke = Entry(root, text=yrke)
entryyrke.place(x=240, y=230)

labelcountry = Label(root, text="country", width=20, font=('bold', 10))
labelcountry.place(x=50, y=250)
# entrycountry = Entry(root, text=country)
# entrycountry.place(x=240, y=250)
listett = ['Sverige', 'Finland', 'Norge', 'Danrmark', 'Island']
droplist = OptionMenu(root, country, *listett)
droplist.config(width=10)
country.set('Välj ditt land')
droplist.place(x=240, y=250)

labelhobbies = Label(root, text="hobbies", width=20, font=('bold', 10))
labelhobbies.place(x=50, y=270)
entryhobbies = Entry(root, text=hobbies)
entryhobbies.place(x=240, y=270)

labellenght = Label(root, text="lenght", width=20, font=('bold', 10))
labellenght.place(x=50, y=290)
entrylenght = Entry(root, text=lenght)
entrylenght.place(x=240, y=290)

labelsex = Label(root, text="sex", width=20, font=('bold', 10))
labelsex.place(x=50, y=310)
# entrysex = Entry(root, text=sex)
# entrysex.place(x=240, y=310)
Radiobutton(root, text='Male', padx=5, variable=sex, value=1).place(x=200, y=310)
Radiobutton(root, text='Female', padx=5, variable=sex, value=2).place(x=260, y=310)
Radiobutton(root, text='Other', padx=5, variable=sex, value=3).place(x=330, y=310)

labeldate = Label(root, text="date", width=20, font=('bold', 10))
labeldate.place(x=50, y=330)
entrydate = Entry(root, text=date)
entrydate.place(x=240, y=330)

labelprofiles_id = Label(root, text="profiles_id", width=20, font=('bold', 10))
labelprofiles_id.place(x=50, y=350)
entryprofiles_id = Entry(root, text=profileid)
entryprofiles_id.place(x=240, y=350)

Button(root, text='Submit', width=20, bg='green', fg='white', command=database).place(x=270, y=370)

root.mainloop()
