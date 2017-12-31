import time  # for real time and date
import os
from tkinter import TK, Canvas, PhotoImage, Label #to import jpeg
from PIL import ImageTK, Image
from datetime import datetime






#im = Image.open('Disneypic.jpg')
#Backgroud_image = Image.open(file= 'C:\LinuxShare\Project\Disneypic.jpg')
#img.show()


d1 = datetime.now()
d1 = d1.strftime("%m/%d/%Y %H:%M:%S")
d2 = "05/03/2018 08:30:00"

date_format = '%m/%d/%Y %H:%M:%S'
hours_format = '%m/%d/%Y %H:%M:%S'
minutes_format = '%m/%d/%Y %H:%M:%S'
seconds_format = '%m/%d/%Y %H:%M:%S'
time_days = datetime.strptime(d1, date_format) - datetime.strptime(d2, date_format)

print(abs(time_days))

top = Tk()

img_name = "Disneypic.jpg"

c = Canvas(top, bg = "blue", height = 500, width = 500)
img = ImageTK.PhotoImage(Image.open('c:\LinuxShare\Project\Disneypic.jpg'))

background_label = Label(top, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

print(abs(time_days))

c.pack()
top.mainloop()

# countdown time for Disney
# tk = Tk()
# tk.title("Disney Countdown!")
# tk.resizable(0,0)
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# tk.update()
# canvas_heght = 500
# canvas_width = 500
# background_image = PhotoImage(file = 'C:\LinuxShare\Project\Disneypic.jpg')
# background_label = tk.label(parent, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# #canvas.create_image(0, 0, anchor = NW, image = Backgrounnd_image)
