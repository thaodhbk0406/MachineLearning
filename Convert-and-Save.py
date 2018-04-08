from PIL import Image
img=Image.open('1816328_L.png').convert('LA')
img.save("grayimg.png")