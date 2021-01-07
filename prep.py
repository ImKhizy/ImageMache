import cv2.cv2 as cv2 #for resizing image
import glob
import numpy as np
import os
import time

prev =[]


for imagefile in glob.glob("/home/khizarsays/Downloads/Dataset/gallery_images/train_images/*.jpg"):
    img = cv2.imread(imagefile,cv2.IMREAD_UNCHANGED)

    data = np.reshape(img, (-1,3))
    # print(data.shape)
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness,labels,centers = cv2.kmeans(data,1,None,criteria,10,flags)

    tempVar = (centers[0].astype(np.int32))
    roundedcol= (np.around(tempVar/5, decimals= -0)*5)
    # print("first ", int(roundedcol[0]))
    blue = "{:03d}".format(int(roundedcol[0]))
    green = "{:03d}".format(int(roundedcol[1]))
    red= "{:03d}".format(int(roundedcol[2]))
    roundedcol = "["+blue+" "+green+" "+ red+"]"
    # roundedcol= str(roundedcol)
    # roundedcol = roundedcol.replace(".", "")
    # roundedcol = ' '.join(roundedcol.split())
    # if str(roundedcol)[1] == " ":
    #     roundedcol = roundedcol[1].replace(" ", "")
    if (roundedcol) not in prev:
        colorval = ("/home/khizarsays/Desktop/GitProjects/ImageMache/V2Images/" + roundedcol + ".jpeg")
        os.rename(imagefile, colorval)
        prev.append(roundedcol)
        print("final:" + roundedcol)

print("Part 1 Complete")
time.sleep(2)

for imagefile in glob.glob("/home/khizarsays/Downloads/Dataset/gallery_images/fruits-360/Training/**/*.jpg"):
    img = cv2.imread(imagefile,cv2.IMREAD_UNCHANGED)

    data = np.reshape(img, (-1,3))
    # print(data.shape)
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness,labels,centers = cv2.kmeans(data,1,None,criteria,10,flags)

    tempVar = (centers[0].astype(np.int32))
    roundedcol= (np.around(tempVar/5, decimals= -0)*5)
    # print("first ", int(roundedcol[0]))
    blue = "{:03d}".format(int(roundedcol[0]))
    green = "{:03d}".format(int(roundedcol[1]))
    red= "{:03d}".format(int(roundedcol[2]))
    roundedcol = "["+blue+" "+green+" "+ red+"]"
    # roundedcol= str(roundedcol)
    # roundedcol = roundedcol.replace(".", "")
    # roundedcol = ' '.join(roundedcol.split())
    # if str(roundedcol)[1] == " ":
    #     roundedcol = roundedcol[1].replace(" ", "")
    if (roundedcol) not in prev:
        colorval = ("/home/khizarsays/Desktop/GitProjects/ImageMache/V2Images/" + roundedcol + ".jpeg")
        os.rename(imagefile, colorval)
        prev.append(roundedcol)
        print("final:" + roundedcol)
print("Part 2 Complete")