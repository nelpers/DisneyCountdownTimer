from tkinter import Tk, Canvas, PhotoImage, Label
from PIL import ImageTk, Image

top = Tk()

img_path = "Disneypic.jpg"

C = Canvas(top, bg="blue", height=400, width=600)
img = ImageTk.PhotoImage(Image.open('C:\LinuxShare\Project\Disneypic.jpg'))

background_label = Label(top, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop()
