#   #   #   #   ######  
#   #   #   #   #
#####   #   #   #  ###
#   #   #   #   #    #
#   #   #####   ######

import numpy as np

import cv2
import time, sys
from math import *
from tkinter import *

from PIL import ImageTk, Image
import os

#maakt een input en een output als deze niet bestaan in de DIR


if os.path.exists("./input/"):
    print("input is er")
else:
    os.mkdir("./input/")
if os.path.exists("./output/"):
    print("output is er")
else:
    os.mkdir("./output/")


# neem 3 afbeeldingen
# afbeelding 1 neemt de Bigwidth en dit is de hoofd IMAGE
# afbeelding 2 en 3 nemen een secundaire rol en komer er onder te staan
filearray = []
imgaraaytk = []
def collage(image1, image2, image3):
    print(image1)
    print(image2)
    print(image3)
    im1 = cv2.imread("./input/"+image1)
    im2 = cv2.imread("./input/"+image2)
    im3 = cv2.imread("./input/"+image3)

    heightprim, widthprim, channels = im1.shape
    heightsecu2, widthsecu2, channels2 = im2.shape
    heightsecu3, widthsecu3, channels3 = im3.shape

    minheightsecu = min(heightprim, heightsecu2, heightsecu3)
    fitwidth = ceil(widthprim / 2)
    fitwidth2 = floor(widthprim / 2)
    resize2 = cv2.resize(im2, (fitwidth, minheightsecu))
    resize3 = cv2.resize(im3, (fitwidth2, minheightsecu))

    horizontalimg = np.hstack((resize2, resize3))


    vertimg = np.vstack((im1, horizontalimg))
    cv2.imwrite("./output/"+image1, vertimg)
    print(image1, image2, image3)
    del filearray[0]
    del imgaraaytk[0]
    del filearray[0]
    del imgaraaytk[0]
    del filearray[0]
    del imgaraaytk[0]
    open_img()

for geladenfile in os.listdir("./input"):
    filearray.append(geladenfile)
    imgaraaytk.append("./input/" + geladenfile)
i = True
def makeframes():
    while i:
        try:
            collage(filearray[0], filearray[1], filearray[2])
        except:
            print("error")
            break

#user frames
root=Tk()
frame = Frame(width=900, height=700, bg="snow")
def openfn():
    foto1 = imgaraaytk[0]
    foto2 = imgaraaytk[1]
    foto3 = imgaraaytk[2]
    return foto1, foto2, foto3
def open_img():
    photo1, photo2, photo3 = openfn()
    img1 = Image.open(photo1)
    img1 = img1.resize((250, 250), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    panel1 = Label(frame, image=img1)
    panel1.image = img1
    panel1.place(x=25,y=75)
    img2 = Image.open(photo2)
    img2 = img2.resize((250, 250), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    panel2 = Label(frame, image=img2)
    panel2.image = img2
    panel2.place(x=325,y=75)
    img3 = Image.open(photo3)
    img3 = img3.resize((250, 250), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    panel3 = Label(frame, image=img3)
    panel3.image = img3
    panel3.place(x=625,y=75)
    butdel1 = Button( frame, text="haal foto 1 weg", command=delete1).place(x=75, y=350)
    butdel2 = Button( frame, text="haal foto 2 weg", command=delete2).place(x=390, y=350)
    butmove2 = Button( frame, text="zet als Main", command=move2).place(x=400, y=400)
    butdel3 = Button( frame, text="haal foto 3 weg", command=delete3).place(x=690, y=350)
    butmove3 = Button( frame, text="zet als Main", command=move3).place(x=700, y=400)
    collagemaker = Button(frame, text="maak Collage", command= lambda:collage(filearray[0], filearray[1], filearray[2])). place(x=405, y= 550)
btn = Button(frame, text='open image', command=open_img).place(x=400, y=10)
def delete1():
    del imgaraaytk[0]
    del filearray[0]
    open_img()
def delete2():
    del imgaraaytk[1]
    del filearray[1]
    open_img()
def delete3():
    del imgaraaytk[2]
    del filearray[2]
    open_img()
def move2():
    filearray.insert(0, filearray.pop(1))
    imgaraaytk.insert(0, imgaraaytk.pop(1))
    open_img()
def move3():
    filearray.insert(0, filearray.pop(2))
    imgaraaytk.insert(0, imgaraaytk.pop(2))
    open_img()
reminderlabel = Label(frame,bg="snow", text="Foto 1 is de top foto \n foto 2 en 3 komen er onder te staan\nfoto 2 en 3 worden de wijdte de helft van foto 1 \n Hoogte wordt het kleinste hoogte genomen van de 3 foto's  ").place(x=50, y=610)
buttonall = Button(frame,bg="red", text="doe alles achter elkaar", command=makeframes).place(x=730, y= 655)


#<< loopt userform >>
frame.pack()
root.resizable(False, False)
root.title("Collage Maker")
root.mainloop()
