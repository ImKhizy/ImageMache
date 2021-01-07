import cv2.cv2 as cv2
import glob
import numpy as np
import os
import time
import sys

curdir = str(os.getcwd())
print(curdir)
names =[]
outcount = 0
divisor = 8
hvals= []
vvals= []
def dimcorrect(height, width):
    if height > 1999 or width > 1999:
        height = height/1.2
        width = width/1.2
        hvals.append(height)
        vvals.append(width)
        print(height, " ", width)
        dimcorrect(height, width)

def closest(colors,color):
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return smallest_distance 


for imgs in sorted(glob.glob(curdir +"/V2Images/*.jpeg")):
    name = (imgs[-17:-6])
    name = name.replace(" ", "")  
    bgr = [int(name[0:3]),int(name[3:6]),int(name[6:9])]
    names.append(bgr)

print("Index Complete")
time.sleep(2)

def mainproc(resized, height, width, curdir, outcount):
    
    column=[]
    for countery in range(0, width):
        row = []
        for counterx in range(0, height):
            pixel = (resized[counterx, countery])
            pixel = (np.around(pixel/5, decimals= 0)*5)
            bluepx = "{:03d}".format(int(pixel[0]))
            greenpx = "{:03d}".format(int(pixel[1]))
            redpx= "{:03d}".format(int(pixel[2]))
            pixel = [int(bluepx), int(greenpx), int(redpx)]
            closest_color = closest(names,pixel)
            validmatch = closest_color
            validmatch = validmatch[0]
            bluevm = "{:03d}".format((validmatch[0]))
            greenvm = "{:03d}".format((validmatch[1]))
            redvm= "{:03d}".format((validmatch[2]))
            validmatch = "["+bluevm+" "+greenvm+" "+redvm+"]"      
            matchpath = (curdir + "/V2Images/" + str(validmatch) + ".jpeg")        
            matchimg = cv2.imread(matchpath)
            matchimg = cv2.resize(matchimg, (int(np.sqrt(height*width)/4), int(np.sqrt(height*width)/4)), interpolation = cv2.INTER_AREA)
            row.append(matchimg)
            # print("Row Complete")
        final_row =np.hstack(row)
        column.append(final_row)
        print("Column complete")    
    final_column = np.vstack(column)
    print("Image complete")
    imagef = cv2.rotate(final_column, cv2.ROTATE_90_CLOCKWISE)
    imagef = cv2.flip(imagef, 1)
    os.chdir(curdir+"/Output") 
    cv2.imwrite(str(outcount)+".jpeg", imagef)
    cv2.waitKey(0)    
    print("ImageMache complete")
    os.chdir(curdir)


for inputfile in glob.glob(curdir+ "/Input/*"):
    img = cv2.imread(inputfile, cv2.IMREAD_UNCHANGED)
    height = img.shape[0]
#    print(height)
    width = img.shape[1]
    dimcorrect(height, width)
#    height = hvals[-1]
#    width= vvals[-1]
    print("height: ", height, "width: ", width)
    height = int(int(height)/divisor)
    width = int(int(width)/divisor)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    mainproc(resized, height, width, curdir, outcount)
    outcount += 1
