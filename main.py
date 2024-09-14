import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from colorthief import ColorThief
import os

root = Tk()
root.title("Color picker from image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False,False)

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), #filedialog.askopenfilename: This opens a file dialog box that allows the user to browse and select an image file. # initialdir=os.getcwd(): Sets the initial directory to the current working directory
                                          title= 'Select Image File', filetypes=(('PNG file', '*.png'),
                                                                                 ('JPG file','*.jpg'),
                                                                                 ('ALL file', '*.txt'))) #Specifies which file types the user can select from (e.g., .png, .jpg, .txt files).
    img=Image.open(filename) #Opens the image: This uses the PIL.Image.open() function to load the selected image from the filename path.
    img=ImageTk.PhotoImage(img) #converts the PIL image (img) into a format that can be displayed in a Tkinter label or widget. 
    lbl.configure(image=img, width=310, height=270)
    lbl.image=img

def findColor():
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    # Lists for hex labels and canvas items for both colors and colors2 canvases
    color_labels = [hex1, hex2, hex3, hex4, hex5, hex6, hex7, hex8, hex9, hex10]
    color_ids = [id1, id2, id3, id4, id5, id6, id7, id8, id9, id10]
    canvases = [colors, colors, colors, colors, colors, colors2, colors2, colors2, colors2, colors2]

    # Loop over the palette and update labels and canvas items
    for i, rgb in enumerate(palette[:10]):
        color_hex = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"  # Convert RGB to hex
        canvases[i].itemconfig(color_ids[i], fill=color_hex)  # Update the correct canvas color
        color_labels[i].config(text=color_hex)  # Update the hex label text


#icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

Label(root, width=120, height=10, bg="#A452A4").pack()

#frame
frame = Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)

logo = PhotoImage(file="logo.png")
Label(frame, image=logo, bg="#fff").place(x=10, y=10)

Label(frame, text="Color Finder", font="arial 25 bold", bg="white").place(x=100, y=20)

#color1
colors = Canvas(frame, bg="#fff", width=150, height=265,bd=0) #Canvas is a widget in Tkinter used to draw shapes, lines, images, text, and more. It's often used to create custom graphics or interactive elements in the user interface.
colors.place(x=20, y=90)

id1 = colors.create_rectangle((10,10,50,50), fill="#fff")
id2 = colors.create_rectangle((10,50,50,100), fill="#fff")
id3 = colors.create_rectangle((10,100,50,150), fill="#fff")
id4 = colors.create_rectangle((10,150,50,200), fill="#fff")
id5 = colors.create_rectangle((10,200,50,250), fill="#fff")

hex1 = Label(colors, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex1.place(x=60, y=15)

hex2 = Label(colors, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex2.place(x=60, y=65)

hex3 = Label(colors, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex3.place(x=60, y=115)

hex4 = Label(colors, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex4.place(x=60, y=165)

hex5 = Label(colors, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex5.place(x=60, y=215)

#color2
colors2 = Canvas(frame, bg="#fff", width=150, height=265,bd=0) #Canvas is a widget in Tkinter used to draw shapes, lines, images, text, and more. It's often used to create custom graphics or interactive elements in the user interface.
colors2.place(x=180, y=90)

id6 = colors2.create_rectangle((10,10,50,50), fill="#fff")
id7 = colors2.create_rectangle((10,50,50,100), fill="#fff")
id8 = colors2.create_rectangle((10,100,50,150), fill="#fff")
id9 = colors2.create_rectangle((10,150,50,200), fill="#fff")
id10 = colors2.create_rectangle((10,200,50,250), fill="#fff")

hex6 = Label(colors2, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex6.place(x=60, y=15)

hex7 = Label(colors2, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex7.place(x=60, y=65)

hex8 = Label(colors2, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex8.place(x=60, y=115)

hex9 = Label(colors2, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex9.place(x=60, y=165)

hex10 = Label(colors2, text="#fff", fg="#000", font="arial 12 bold", bg="white")
hex10.place(x=60, y=215)

#select image
selectimage = Frame(frame, width = 340, height=350, bg="#d6dee5")
selectimage.place(x=350, y=10)

f= Frame(selectimage, bd=3, bg="black", width=320, height=280, relief=GROOVE)
f.place(x=10, y=10)

lbl=Label(f, bg="black")
lbl.place(x=0, y=0)

Button( selectimage, text="Select Image", width=12, height=1, font="arial 14 bold", command = showimage).place(x=10, y=300)
Button( selectimage, text="Find Colors", width=12, height=1, font="arial 14 bold", command= findColor).place(x=176, y=300)
root.mainloop()
