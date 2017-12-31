import time  # for real time and date
import os
from tkinter import *  # for the display
from datetime import datetime, time
# from Pillow import Image #to import jpeg


# countdown time for Disney
tk = Tk()
canvas = Canvas(tk, width=500, height=500)

def datediffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds

def timedef(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    months, days = divmod(days, 30)
    return months, days, hours, minutes, seconds


while True:
    now = datetime.now()

canvas.pack()

#im = Image.open('Disneypic.jpg')
#Backgroud_image = Image.open(file= 'C:\LinuxShare\Project\Disneypic.jpg')
# img.show()
