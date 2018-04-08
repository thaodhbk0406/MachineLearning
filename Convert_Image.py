from PIL import Image
import numpy as np
from resizeimage import resizeimage
#Function to convert image to array or list
def loadImage (inFileName, outType ) :
    img = Image.open( inFileName )
    img.load()
    data = np.asarray( img, dtype="int32" )
    if outType == "anArray":
        return data
    if outType == "aList":
        return list(data)


#Load image to array
myArray1 = loadImage("1816328_L.png", "anArray")
print(myArray1)

im = Image.open('1816328_L.png')
width, height = im.size
print(width, height)



# #Load image to a list
# myList1 = loadImage("1816328_L.png", "aList")
# print(myList1)