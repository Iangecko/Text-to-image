from PIL import Image
from options import *

img = Image.open(oa)#inputs the image to be changed

def encodeTxt():
    if oc == True:  
        f = open(od,"r")
        text = f.read()
        f.close
    else:
        text = input("convert text to image\n")

    binary = ''.join('{0:08b}'.format(ord(x), 'b') for x in text)

    #setting up pre-vars
    width, height = img.size
    y = 0
    x = 0
    item = 0
    debug(binary)

    #main pixel change loop
    for y in range(0, height): #Y axis for loop
        x = 0
        for x in range(0, width): #X axis for loop
            if item < len(str(binary)):
                if binary[item] == "1":
                    img.putpixel((x, y), (0, 0, 0)) #place a black pixel
                else:
                    img.putpixel((x, y), (255, 255, 255)) #place a white pixel (not necessary but good if the image isnt totally white)
            else:
                img.putpixel((x, y), (255, 255, 255))
            x += 1
            item += 1
        y += 1

    img.save(oa) #write out to the output image
    img.close
