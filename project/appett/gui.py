from tkinter import *
from tkinter import ttk
from vecka42.appett.sqlLocal import sqlConnector, createDatabase, dropDatabase, insertQuery, showDb, createTables, \
    usePerson, readFromDB
from vecka42.appett.socketScrips import socket_connect, server
from vecka42.appett.webconnect import homeConnect, googleConnect, slackConnect, guiPthonkConnect, soloLearnConnect
from vecka42.appett.ImportSubProcessFiles import Matrix, powershell
from vecka42.appett.guiapp import Appgui

#   TKINTER SETTING  ###########################


root = Tk()
root.configure(background="black")
root.iconbitmap(default="Untitled.ico")
root.title("Michel´s Playground Title")
root.geometry("565x307")
guiframe = Frame(root)
guiframe.grid(row=0, column=3, columnspan=7, rowspan=7)

# guiframe2 = LabelFrame(root)
# guiframe2.grid(row=0, column=0, )

#  MY Canvas
# myBackgroundCanvas = Canvas(root, bg="black")
# myBackgroundCanvas.grid(row=0,column=0,columnspan=6)
# photobackground = PhotoImage(file="./Untitled.gif")
# myBackgroundCanvas.create_image(0, 100, image=photobackground)

# MIN LABEL
labelett = ttk.Label(text="Michel's Playground")
labelett.grid(row=0, column=1, padx=10, pady=10)
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
sqlmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Sql Options", menu=sqlmenu)
sqlmenu.add_command(label="Connect Sql ", command=sqlConnector)
sqlmenu.add_command(label="Create database sql", command=createDatabase)
sqlmenu.add_command(label="Drop database sql", command=dropDatabase)
sqlmenu.add_command(label="Insert table sql", command=insertQuery)
sqlmenu.add_command(label="Show database sql", command=showDb)
sqlmenu.add_separator()
sqlmenu.add_command(label="Exit", command=root.quit)

# HomePage options menu
homePage = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Homepages", menu=homePage)
homePage.add_command(label="Search Google ", command=googleConnect)
homePage.add_command(label="Visit My HomePage", command=homeConnect)
homePage.add_command(label="Slack", command=slackConnect)
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
programmingmenu.add_command(label="Programming 3", command='')
programmingmenu.add_command(label="Programming 4", command='')
programmingmenu.add_command(label="Programming 5", command='')
programmingmenu.add_separator()
programmingmenu.add_command(label="Exit", command=root.quit)

# Help options
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Search Google", command=googleConnect)
helpmenu.add_command(label="Slack", command=slackConnect)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=root.quit)

root.config(menu=menubar)

# Socket STUFF
# Button SERVER socket
buttonServer = ttk.Button(text="SERVER socket", command=server)
buttonServer.bind("<Return>", lambda event: server())
buttonServer.grid(column=0, row=2)
# Button CLIENT socket
buttonClient = ttk.Button(text="CLIENT socket", command=socket_connect)
buttonClient.bind("<Return>", lambda event: socket_connect())
buttonClient.grid(column=0, row=3)

# SQL STUFF
# Button Sql connector
buttonConnector = ttk.Button(text="Connect SQL", command=sqlConnector)
buttonConnector.bind("<Return>", lambda event: sqlConnector())
buttonConnector.grid(column=1, row=2)
# Button Sql create Database
buttoncreateDatabase = ttk.Button(text="Sql create Database", command=createDatabase)
buttoncreateDatabase.bind("<Return>", lambda event: createDatabase())
buttoncreateDatabase.grid(column=1, row=3)
# Button Sql Use Person
buttonUsePerson = ttk.Button(text="Sql Use Person", command=usePerson)
buttonUsePerson.bind("<Return>", lambda event: usePerson())
buttonUsePerson.grid(column=1, row=4)
# Button Create Tables
buttonTables = ttk.Button(text="Sql create Tables", command=createTables)
buttonTables.bind("<Return>", lambda event: createTables())
buttonTables.grid(column=1, row=5)
# Button Sql insert query
buttonInsertQuery = ttk.Button(text="Insert SQL Table", command=insertQuery)
buttonInsertQuery.bind("<Return>", lambda event: insertQuery())
buttonInsertQuery.grid(column=1, row=6)
# Button See the SQL show databases
buttonShowDb = ttk.Button(text="SQL show databases", command=showDb)
buttonShowDb.bind("<Return>", lambda event: showDb())
buttonShowDb.grid(column=1, row=7)
# Button Sql drop Database
buttonDropDatabase = ttk.Button(text="Sql drop Database", command=dropDatabase)
buttonDropDatabase.bind("<Return>", lambda event: dropDatabase())
buttonDropDatabase.grid(column=1, row=9)
# Button Sql READ Database
buttonReadDatabase = ttk.Button(text="Sql READ Database", command=readFromDB)
buttonReadDatabase.bind("<Return>", lambda event: readFromDB())
buttonReadDatabase.grid(column=1, row=8)

#  Web  Connector STUFF
# Button visit Misk playgroud
buttonWebSite = ttk.Button(text="Visit My HomePage", command=homeConnect)
buttonWebSite.bind("<Return>", lambda event: homeConnect())
buttonWebSite.grid(column=2, row=2)
# Button visit Google
buttonWebSite = ttk.Button(text="Search Google", command=googleConnect)
buttonWebSite.bind("<Return>", lambda event: googleConnect())
buttonWebSite.grid(column=2, row=3)
# Button  Slack
buttonWebSite = ttk.Button(text="Slack", command=slackConnect)
buttonWebSite.bind("<Return>", lambda event: slackConnect())
buttonWebSite.grid(column=2, row=4)
# Button GUI Programming (Tkinter
buttonWebSite = ttk.Button(text="Python 3 - GUI Programming (Tkinter)", command=guiPthonkConnect)
buttonWebSite.bind("<Return>", lambda event: guiPthonkConnect())
buttonWebSite.grid(column=2, row=5)

# Misc STUFF
# Button guess game
buttonGuessingGame = ttk.Button(text="GuessingGame", command='')
buttonGuessingGame.bind("<Return>", lambda event: '')
buttonGuessingGame.grid(column=2, row=8)
# Button See the matrix
buttonMatrix = ttk.Button(text="Enter the MATRIX", command=Matrix)
buttonMatrix.bind("<Return>", lambda event: Matrix())
buttonMatrix.grid(column=2, row=9)
# Button See the Powershell
buttonMatrix = ttk.Button(text="Powershell", command=powershell)
buttonMatrix.bind("<Return>", lambda event: powershell())
buttonMatrix.grid(column=2, row=10)
# Button Goodbye exit
buttonGoodbye = ttk.Button(text="Press to exit", command=exit)
buttonGoodbye.bind("<Return>", lambda: exit())
buttonGoodbye.grid(row=11)
# entry button 1
# textentry = Entry(width=20, bg="white")
# textentry.bind("<Return>", '')
# textentry.grid(row=2, column=0, sticky=W)

# root loop
root.mainloop()
