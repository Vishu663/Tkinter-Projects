from tkinter import *
from PIL import Image, ImageTk

mainwin = Tk()
mainwin.title("Welcome to my coding page")

my_img1 = ImageTk.PhotoImage(Image.open("Images//im1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images//im3.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images//im4.jpg"))

image_list = [my_img1, my_img2, my_img3]


status = Label(mainwin, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(mainwin, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(mainwin, text="<<", command=lambda: back(image_number - 1))

    if image_number == 2:
        button_forward = Button(mainwin, text=">>", command=DISABLED)

    status = Label(mainwin, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=3)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    global status
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(mainwin, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(mainwin, text="<<", command=lambda: back(image_number - 1))

    if image_number == 0:
        button_back = Button(mainwin, text="<<", command=DISABLED)

    status = Label(mainwin, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=3)


button_back = Button(mainwin, text="<<", command=lambda: back(0))
button_forward = Button(mainwin, text=">>", command=lambda: forward(0))
button_quit = Button(mainwin, text="Exit Program", command=mainwin.quit)
button_quit.grid(row=1, column=2)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=3)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
mainwin.mainloop()
