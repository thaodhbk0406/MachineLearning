from PIL import Image
from resizeimage import resizeimage

fd_img = open('1816328_L.png', 'r')
img = Image.open(fd_img)
img = resizeimage.resize_crop(img, [200, 200])
img.save('test-image-crop.png', img.format)
fd_img.close()