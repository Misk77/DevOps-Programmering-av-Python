from tkinter import *
from tkinter import ttk
from appett.sqlLocal import sqlConnector, createDatabase, dropDatabase, insertQuery, showDb, createTables, \
    useProfiles, readFromDB, selectDB, describeTable, dropTables
from appett.sqldb4free import sqldb4freeConnector, sqldb4freecreateTables, sqldb4freeCreateDatabase, \
    sqldb4freeDescribeTable, sqldb4freedropDatabase, sqldb4freeInsertQuery, sqldb4freeReadFromDB, sqldb4freeSelectDB, \
    sqldb4freeShowDb, sqldb4freeUsedatabase, sqldb4freedropTables
from appett.sqlhostinger import sqlhostingConnector, sqlhostingCreateDatabase, sqlhostingCreateTables, \
    sqlhostingDescribeTable, sqlhostingDropDatabase, sqlhostingDropTables, sqlhostingInsertQuery, sqlhostingReadFromDB, \
    sqlhostingSelectDB, sqlhostingShowDb, sqlhostingUsedatabase
from appett.socketScrips import socket_connect, server, serverUI
from appett.webconnect import homeConnect, wordPressConnect, googleConnect, slackConnect, guiPthonkConnect, \
    soloLearnConnect, \
    unofficialWinBIN, downloadpage
from appett.cv2showImgVideo import fpsShow, showimage
from appett.ImportSubProcessFiles import Matrix, powershell
from appett.printoutgui import printSomething
from appett.funktioner import on_closing

# from appett.guiapp import Appgui

#   TKINTER SETTING  ###########################


root = Tk()
root.configure(background="black")
root.iconbitmap(default="Untitled.ico")
root.title("Michel´s Playground Title")
root.geometry("910x350")
guiframe = Frame(root)
guiframe.grid(row=0, column=2, columnspan=7, rowspan=7)
"""
guiframe2 = Frame(root)
labeltwo = ttk.Label(guiframe2,text="(use the exit or esc to quit)")
guiframe2.grid(row=0, column=0, )
labeltwo.config(font=("Inconsolata", 20))
"""

#  MY Canvas
# myBackgroundCanvas = Canvas(root, bg="black")
# myBackgroundCanvas.grid(row=0,column=0,columnspan=6)
# photobackground = PhotoImage(file="./Untitled.gif")
# myBackgroundCanvas.create_image(0, 100, image=photobackground)

# MIN LABEL
labelett = ttk.Label(text="Michel's Playground")
labelett.grid(row=0, column=0, padx=5, pady=5)
labelett.config(font=("Inconsolata", 20))

# Entry


menubar = Menu(root)
# Server options menu
servermenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Server Options", menu=servermenu)
servermenu.add_command(label="Start server", command=server)
servermenu.add_command(label="Socket connect", command=socket_connect)
servermenu.add_separator()
servermenu.add_command(label="Exit", command=root.quit)

# SQL options menu
sqlmenu = Menu(root, tearoff=0)
menubar.add_cascade(label="Sql menu", menu=sqlmenu)
# LOCAL SQL
sqllocal = Menu(sqlmenu, tearoff=False)
sqlmenu.add_cascade(label="Mysql LOCAL ", menu=sqllocal)
sqllocal.add_command(label="Connect LOCAL ", command=sqlConnector)
sqllocal.add_command(label="Create database profiles LOCAL", command=createDatabase)
sqllocal.add_command(label="Drop database profiles LOCAL", command=dropDatabase)
sqllocal.add_command(label="Insert table  LOCAL", command=insertQuery)
sqllocal.add_command(label="Show database  LOCAL", command=showDb)
sqllocal.add_command(label="Use profiles  LOCAL", command=useProfiles)
sqllocal.add_command(label="Select profiles LOCAL", command=selectDB)
sqllocal.add_command(label="Read database LOCAL", command=readFromDB)
sqllocal.add_command(label="Create table in profiles LOCAL", command=createTables)
sqllocal.add_command(label="Describe table LOCAL", command=describeTable)
sqllocal.add_command(label="DROP TABLE profiles mysql db4free.net", command=dropTables)
sqllocal.add_separator()
sqllocal.add_command(label="Exit", command=root.quit)
# SQL mysql db4free.net
sqldb4free = Menu(sqlmenu, tearoff=False)
sqlmenu.add_cascade(label="mysql db4free.net ", menu=sqldb4free)
sqldb4free.add_command(label="Connect mysql db4free.net ", command=sqldb4freeConnector)
# Create database  CANT be done in db4free.net  No Privileges
sqldb4free.add_command(label="Create database mysql db4free.net", command=sqldb4freeCreateDatabase)
sqldb4free.add_command(label="Drop database mysql db4free.net", command=sqldb4freedropDatabase)
sqldb4free.add_command(label="Insert table mysql db4free.net", command=sqldb4freeInsertQuery)
sqldb4free.add_command(label="Show database mysql db4free.net", command=sqldb4freeShowDb)
sqldb4free.add_command(label="Use Database miskdb mysql db4free.net", command=sqldb4freeUsedatabase)
sqldb4free.add_command(label="Select Database miskdb mysql db4free.net", command=sqldb4freeSelectDB)
sqldb4free.add_command(label="Read database mysql db4free.net", command=sqldb4freeReadFromDB)
sqldb4free.add_command(label="Create table in profiles mysql db4free.net", command=sqldb4freecreateTables)
sqldb4free.add_command(label="Describe table mysql db4free.net", command=sqldb4freeDescribeTable)
sqldb4free.add_command(label="DROP TABLE profiles mysql db4free.net", command=sqldb4freedropTables)
sqldb4free.add_separator()
sqldb4free.add_command(label="Exit", command=root.quit)
# SQL hostinger.com
sqlhosting = Menu(sqlmenu, tearoff=False)
sqlmenu.add_cascade(label="mysql hostinger.com ", menu=sqlhosting)
sqlhosting.add_command(label="Connect mysql hostinger.com ", command=sqlhostingConnector)
# Create database  CANT be done in db4free.net  No Privileges
sqlhosting.add_command(label="Create database mysql hostinger", command=sqlhostingCreateDatabase)
sqlhosting.add_command(label="Drop database mysql hostinger", command=sqlhostingDropDatabase)
sqlhosting.add_command(label="Insert table mysql hostinger", command=sqlhostingInsertQuery)
sqlhosting.add_command(label="Show database mysql hostinger", command=sqlhostingShowDb)
sqlhosting.add_command(label="Use Database miskdb mysql dhostinger", command=sqlhostingUsedatabase)
sqlhosting.add_command(label="Select Database miskdb mysql hostinger", command=sqlhostingSelectDB)
sqlhosting.add_command(label="Read database mysql hostinger", command=sqlhostingReadFromDB)
sqlhosting.add_command(label="Create table in profiles mysql hostinger", command=sqlhostingCreateTables)
sqlhosting.add_command(label="Describe table mysql hostinger", command=sqlhostingDescribeTable)
sqlhosting.add_command(label="DROP TABLE profiles hostinger", command=sqlhostingDropTables)
sqlhosting.add_separator()
sqlhosting.add_command(label="Exit", command=root.quit)

# HomePage options menu
homePage = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Homepages", menu=homePage)
homePage.add_command(label="Search Google ", command=googleConnect)
homePage.add_command(label="Visit My HomePage", command=homeConnect)
homePage.add_command(label="Slack", command=slackConnect)
homePage.add_command(label="Unofficial Win Binary package", command=unofficialWinBIN)
homePage.add_separator()
homePage.add_command(label="Exit", command=root.quit)

# Games options menu
gamemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game options", menu=gamemenu)
gamemenu.add_command(label="Guessing Game", command='')
gamemenu.add_command(label="Game 2", command='')
gamemenu.add_command(label="Game 2", command='')
gamemenu.add_command(label="Game 2", command='')
gamemenu.add_command(label="Game 2", command='')
gamemenu.add_command(label="Game 2", command='')
gamemenu.add_separator()
gamemenu.add_command(label="Exit", command=root.quit)

# Programming  options menu
programmingmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Programming", menu=programmingmenu)
programmingmenu.add_command(label="SoloLearn", command=soloLearnConnect)
programmingmenu.add_command(label="Slack", command=slackConnect)
programmingmenu.add_command(label="Python 3 - GUI Programming (Tkinter)", command=guiPthonkConnect)
programmingmenu.add_command(label="Download Page", command=downloadpage)
programmingmenu.add_command(label="Programming 4", command='')
programmingmenu.add_command(label="Programming 5", command='')
programmingmenu.add_separator()
programmingmenu.add_command(label="Exit", command=root.quit)

# Help options
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Search Google", command=googleConnect)
helpmenu.add_command(label="Slack", command=slackConnect)
helpmenu.add_command(label="Unofficial Win Binary package", command=unofficialWinBIN)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=on_closing)

root.config(menu=menubar)

# Socket STUFF
# Button SERVER socket
buttonServer = ttk.Button(text="SERVER multiserver socket", command=serverUI)
buttonServer.bind("<Return>", lambda event: serverUI())
buttonServer.grid(column=0, row=2)
# Button CLIENT socket
buttonClient = ttk.Button(text="CLIENT multiserver socket", command=socket_connect)
buttonClient.bind("<Return>", lambda event: socket_connect)
buttonClient.grid(column=0, row=3)

# SQL STUFF
# SQL LOCAL
# Button Sql CONNECTOR
buttonConnector = ttk.Button(text="Connect SQL Local", command=sqlConnector)
buttonConnector.bind("<Return>", lambda event: sqlConnector())
buttonConnector.grid(column=1, row=2)
# Button Sql CREATE Database
buttoncreateDatabase = ttk.Button(text="SQL Local create Database", command=createDatabase)
buttoncreateDatabase.bind("<Return>", lambda event: createDatabase())
buttoncreateDatabase.grid(column=1, row=3)
# Button Sql Use Person
buttonUsePerson = ttk.Button(text="SQL Local Use profiles", command=useProfiles)
buttonUsePerson.bind("<Return>", lambda event: useProfiles())
buttonUsePerson.grid(column=1, row=4)
# Button Sql SELECT DATABASE()
buttonSelectDatabase = ttk.Button(text="SQL LocalSelect profiles", command=selectDB)
buttonSelectDatabase.bind("<Return>", lambda event: selectDB())
buttonSelectDatabase.grid(column=1, row=5)
# Button Create Tables
buttonTables = ttk.Button(text="SQL Local create Tables", command=createTables)
buttonTables.bind("<Return>", lambda event: createTables())
buttonTables.grid(column=1, row=6)
# Button Sql INSERT query
buttonInsertQuery = ttk.Button(text="SQL Local Insert Table", command=insertQuery)
buttonInsertQuery.bind("<Return>", lambda event: insertQuery())
buttonInsertQuery.grid(column=1, row=7)
# Button See the SQL SHOW DATABASES
buttonShowDb = ttk.Button(text="SQL Local show databases", command=showDb)
buttonShowDb.bind("<Return>", lambda event: showDb())
buttonShowDb.grid(column=1, row=8)
# Button Sql drop Database
buttonDropDatabase = ttk.Button(text="Sql Local drop Database", command=dropDatabase)
buttonDropDatabase.bind("<Return>", lambda event: dropDatabase())
buttonDropDatabase.grid(column=1, row=9)
# Button Sql READ Database
buttonReadDatabase = ttk.Button(text="Sql Local READ Database", command=readFromDB)
buttonReadDatabase.bind("<Return>", lambda event: readFromDB())
buttonReadDatabase.grid(column=1, row=11)
# Button Sql DESCRIBE tables
buttonDescribeTable = ttk.Button(text="Sql Local DESCRIBE table", command=describeTable)
buttonDescribeTable.bind("<Return>", lambda event: describeTable())
buttonDescribeTable.grid(column=1, row=12)
# Button Sql DROP tables
buttonDropTable = ttk.Button(text="Sql Local DROP table", command=dropTables)
buttonDropTable.bind("<Return>", lambda event: dropTables())
buttonDropTable.grid(column=1, row=10)
# SQL hostinger.com #########################################################################
# Button Connect SQL db4free.net
buttonConnector = ttk.Button(text="Connect SQL hostinger.com", command=sqlhostingConnector)
buttonConnector.bind("<Return>", lambda event: sqlhostingConnector())
buttonConnector.grid(column=2, row=2)
# Button Sql db4free.net CREATE Database CAnt be done on db4free.net NO PRIVIGLES
buttoncreateDatabase = ttk.Button(text="SQL hostinger.com create Database", command=sqlhostingCreateDatabase)
buttoncreateDatabase.bind("<Return>", lambda event: sqlhostingCreateDatabase())
buttoncreateDatabase.grid(column=2, row=3)
# Button Sql db4free.net Use Person
buttonUsePerson = ttk.Button(text="SQL hostinger.com Use database miskdb", command=sqlhostingUsedatabase)
buttonUsePerson.bind("<Return>", lambda event: sqlhostingUsedatabase())
buttonUsePerson.grid(column=2, row=4)
# Button Sql db4free.net SELECT DATABASE()
buttonSelectDatabase = ttk.Button(text="SQL hostinger.com Select profiles", command=sqlhostingSelectDB)
buttonSelectDatabase.bind("<Return>", lambda event: sqlhostingSelectDB())
buttonSelectDatabase.grid(column=2, row=5)
# Button Create  Tables
buttonTables = ttk.Button(text="SQL hostinger.com create Tables", command=sqlhostingCreateTables)
buttonTables.bind("<Return>", lambda event: sqlhostingCreateTables())
buttonTables.grid(column=2, row=6)
# Button Sql INSERT query
buttonInsertQuery = ttk.Button(text="SQL hostinger.com Insert Table", command=sqlhostingInsertQuery)
buttonInsertQuery.bind("<Return>", lambda event: sqlhostingInsertQuery())
buttonInsertQuery.grid(column=2, row=7)
# Button See the SQL SHOW DATABASES
buttonShowDb = ttk.Button(text="SQL hostinger.com show databases", command=sqlhostingShowDb)
buttonShowDb.bind("<Return>", lambda event: sqlhostingShowDb())
buttonShowDb.grid(column=2, row=8)
# Button Sql drop Database
buttonDropDatabase = ttk.Button(text="SQL hostinger.com drop Database", command=sqlhostingDropDatabase)
buttonDropDatabase.bind("<Return>", lambda event: sqlhostingDropDatabase())
buttonDropDatabase.grid(column=2, row=9)
# Button Sql READ Database
buttonReadDatabase = ttk.Button(text="SQL hostinger.com READ Database", command=sqlhostingReadFromDB)
buttonReadDatabase.bind("<Return>", lambda event: sqlhostingReadFromDB())
buttonReadDatabase.grid(column=2, row=11)
# Button Sql DESCRIBE tables
buttonDescribeTable = ttk.Button(text="SQL hostinger.com DESCRIBE table", command=sqlhostingDescribeTable)
buttonDescribeTable.bind("<Return>", lambda event: sqlhostingDescribeTable())
buttonDescribeTable.grid(column=2, row=12)
# Button Sql DROP tables
buttonDropTable = ttk.Button(text="SQL hostinger.com DROP table", command=sqlhostingDropTables)
buttonDropTable.bind("<Return>", lambda event: sqlhostingDropTables())
buttonDropTable.grid(column=2, row=10)

#  Web  Connector STUFF   #
# Button visit Misk playgroud
buttonWebSite = ttk.Button(text="Visit My HomePage", command=homeConnect)
buttonWebSite.bind("<Return>", lambda event: homeConnect())
buttonWebSite.grid(column=3, row=2)
# Button visit michels wordpress
buttonWebSite = ttk.Button(text="Visit My Wordpress", command=wordPressConnect)
buttonWebSite.bind("<Return>", lambda event: wordPressConnect())
buttonWebSite.grid(column=3, row=3)
# Button visit DownloadPage
buttonWebSite = ttk.Button(text="Visit My DownloadPage", command=downloadpage)
buttonWebSite.bind("<Return>", lambda event: downloadpage())
buttonWebSite.grid(column=3, row=4)
# Button visit Google
buttonWebSite = ttk.Button(text="Search Google", command=googleConnect)
buttonWebSite.bind("<Return>", lambda event: googleConnect())
buttonWebSite.grid(column=3, row=5)
# Button  Slack
buttonWebSite = ttk.Button(text="Slack", command=slackConnect)
buttonWebSite.bind("<Return>", lambda event: slackConnect())
buttonWebSite.grid(column=3, row=6)
# Button GUI Programming (Tkinter
buttonWebSite = ttk.Button(text="Python 3 - GUI Programming (Tkinter)", command=guiPthonkConnect)
buttonWebSite.bind("<Return>", lambda event: guiPthonkConnect())
buttonWebSite.grid(column=3, row=7)
# Button Unofficial Windows Binaries for Python Extension Packages
buttonWebSite = ttk.Button(text="Unofficial Win Binaries for Python Extension Packages", command=unofficialWinBIN)
buttonWebSite.bind("<Return>", lambda event: unofficialWinBIN())
buttonWebSite.grid(column=3, row=8)

# Misc STUFF
# Button guess game
buttonGuessingGame = ttk.Button(text="GuessingGame", command='')
buttonGuessingGame.bind("<Return>", lambda event: '')
buttonGuessingGame.grid(column=3, row=8)
# Button See the matrix
buttonMatrix = ttk.Button(text="Enter the MATRIX", command=Matrix)
buttonMatrix.bind("<Return>", lambda event: Matrix())
buttonMatrix.grid(column=3, row=9)
# Button See the Powershell
buttonMatrix = ttk.Button(text="Powershell", command=powershell)
buttonMatrix.bind("<Return>", lambda event: powershell())
buttonMatrix.grid(column=3, row=10)
# Button FPS text textbild
buttonPrintOutGui = ttk.Button(text="FPS test video", command=fpsShow)
buttonPrintOutGui.bind("<Return>", lambda event: fpsShow())
buttonPrintOutGui.grid(column=3, row=11)
# Button FPS text textbild
buttonPrintOutGui = ttk.Button(text="Show Image", command=showimage)
buttonPrintOutGui.bind("<Return>", lambda event: showimage())
buttonPrintOutGui.grid(column=3, row=13)
# Button Print out gui
buttonPrintOutGui = ttk.Button(text="Print out gui", command=printSomething)
buttonPrintOutGui.bind("<Return>", lambda event: printSomething())
buttonPrintOutGui.grid(column=3, row=12)
# Button Goodbye exit
buttonGoodbye = ttk.Button(text="Press to exit", command=on_closing)
buttonGoodbye.bind("<Return>", lambda event: on_closing())
buttonGoodbye.grid(row=13)
# Button appgui
# buttonPrintOutGui = ttk.Button(text="app class", command=Appgui)
# buttonPrintOutGui.bind("<Return>", lambda event: Appgui())
# buttonPrintOutGui.grid(column=2, row=13)

# entry button 1
# textentry = Entry(width=20, bg="white")
# textentry.bind("<Return>", '')
# textentry.grid(row=2, column=0, sticky=W)

# root loop
# make Esc exit the program
root.bind('<Escape>', lambda e: root.destroy())
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
# root.protocol("WM_DELETE_WINDOW    ", on_closing)
