import os
from tkinter import *
from subprocess import Popen


def Matrix():
    root = Tk()
    p = Popen("Matrix.bat", cwd=r"C:\Users\miche\PycharmProjects\DevOps-Programmering av Python\vecka42\appett")

    root.mainloop()
    stdout, stderr = p.communicate()


def powershell():
    p = Popen("powershell.exe",
              cwd=r"C:\Users\miche\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell")
    win = Tk()
    win.mainloop()
    stdout, stderr = p.communicate()
