import numpy as np
from PIL import Image
import cv2
import os, time, sys, math

# neem 3 afbeeldingen
# afbeelding 1 neemt de Bigwidth en dit is de hoofd IMAGE
# afbeelding 2 en 3 nemen een secundaire rol en komer er onder te staan
filearray = []


def collage(image1, image2, image3):
    im1 = cv2.imread("./input/"+image1)
    im2 = cv2.imread("./input/"+image2)
    im3 = cv2.imread("./input/"+image3)

    heightprim, widthprim, channels = im1.shape
    heightsecu2, widthsecu2, channels2 = im2.shape
    heightsecu3, widthsecu3, channels3 = im3.shape

    minheightsecu = min(heightprim, heightsecu2, heightsecu3)
    fitwidth = math.ceil(widthprim / 2)
    fitwidth2 = math.floor(widthprim / 2)
    resize2 = cv2.resize(im2, (fitwidth, minheightsecu))
    resize3 = cv2.resize(im3, (fitwidth2, minheightsecu))

    horizontalimg = np.hstack((resize2, resize3))


    vertimg = np.vstack((im1, horizontalimg))
    cv2.imwrite("./output/"+image1, vertimg)
    print(image1, image2, image3)
    del filearray[0]
    del filearray[0]
    del filearray[0]

for geladenfile in os.listdir("./input"):
    filearray.append(geladenfile)
filearray.sort()
i = True
while i:
    try:
        collage(filearray[0], filearray[1], filearray[2])
    except:
        print("error")
        break


