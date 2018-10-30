from time import time
from numpy import uint8
from numpy.random import rand
import tkinter as tk
import cv2
from tkinter import *
from PIL import Image, ImageTk


# !/usr/bin/env python
def fpsShow():
    xy = (512, 512)
    Nf = 500

    def fpsopencv(dat):
        tic = time()
        for i in dat:
            cv2.imshow('Fps test', i)
            cv2.waitKey(1)  # integer milliseconds, 0 makes wait forever
        cv2.destroyAllWindows()
        return Nf / (time() - tic)

    imgs = (rand(Nf, xy[0], xy[1]) * 255).astype(uint8)
    fps = fpsopencv(imgs)
    print(fps, 'fps')
    # label = Label(fps, 'fps')
    # label = Label(root, fps, text='fps')
    # label.pack()


# Not complete, not showing with pack, my app are in grid
def showimage():
    import tkinter as tk
    from PIL import Image, ImageTk

    root = tk.Tk()
    root.title("display image")
    im = Image.open(
        "C:/Users/miche/Desktop/trex.png")  # This is the correct location and spelling for my image location
    photo = ImageTk.PhotoImage(im)
    cv = tk.Canvas()
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(10, 10, image=photo, anchor='nw')
    root.mainloop()


# https://www.geeksforgeeks.org/working-images-python/
"""
#img  = Image.open(path)      
# On successful execution of this statement, 
# an object of Image type is returned and stored in img variable) 
   
try:  
    img  = Image.open(path)  
except IOError: 
    pass
# Use the above statement within try block, as it can  
# raise an IOError if file cannot be found,  
# or image cannot be opened.


img = cv2.imread('trex.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""
