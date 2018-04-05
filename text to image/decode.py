import binascii
from options import *
from PIL import Image

def decodeIm():  
    img = Image.open(ob)#inputs the image to be changed
    rgb = img.convert('RGB')
    #setting up pre-vars
    width, height = img.size

    y = 0
    x = 0
    binary = []

    #main pixel change loop
    for y in range(0, height): #Y axis for loop
        x = 0
        for x in range(0, width): #X axis for loop
            if rgb.getpixel((x, y)) == (0,0,0):
                binary.append(1)
            else:
                binary.append(0)
            x += 1
        y += 1

    joined = "".join(str(x) for x in binary)

    debug(joined);

    while ((str(joined)[-1]) == "0"):
        joined = joined[:-1]

    while ((len(str(joined)) % 8) != 0):
        joined = joined + "0"

    binaryArray = int(joined, 2)

    decoded = binascii.unhexlify('%x' % binaryArray)

    decoded = decoded.decode("utf-8")

    if oe == True:
        f = open(of,'w')
        f.write(str(decoded))
        f.close()
    else:
        print("Decoded string:\n"+decoded)
    img.close
