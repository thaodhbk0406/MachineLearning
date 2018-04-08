import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

def rgp2gray(rgb):
	return np.dot(rgb[... , :3], [0.299, 0.587, 0.114])

img=mpimg.imread("1816328_L.png")
gray=rgp2gray(img)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()