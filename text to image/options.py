#ouput image file name
oa = "image.png"

#input image file name

ob = "image.png"

#use input file for text to image
oc = False

#input file name (not needed if oc is set to false)
od = "input"

#output text from decoded image to file
oe = False

#out file name (not needed if oe is set to false)
of = "output"

#debug mode
og = False


#Debug mode output certain parts of the decoding/encoding proccess to help with solving problems
def debug(out):
    if og == True:
        print(out)
