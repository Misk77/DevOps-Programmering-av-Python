import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib import font_manager

LARGE_FONTS = ("Helvetica", 12)


class Appgui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="Untitled.ico")
        tk.Tk.title(self, "Michel´s Playground")
        container = tk.Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=TRUE)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf():
    print("Page 1")


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Michel´s Playground StartPage", font=LARGE_FONTS)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page one", font=LARGE_FONTS)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Michel´s Playground StartPage",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page two", font=LARGE_FONTS)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Michel´s Playground StartPage",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = Appgui()

app.mainloop()
