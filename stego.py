from PIL import Image, ImageFont, ImageDraw
import sys
import os
import binascii

#image object to work with
#image1 = Image.open('m3.jpg')
# image1.show()
#image1.save('m3.png')

"""
image = Image.open('m3.jpg')
fontType = ImageFont.truetype('arial.ttf',encoding='unic')
draw = ImageDraw.Draw(image)
draw.text(xy==(50,50),text='security is dope',fill=(255,60,0),font=fontType)
image.show()
"""
#method to write text to RGB image
def writeText(text, imgSize):

    imageText = Image.new("RGB",imgSize)
    font = ImageFont.load_default().font
    drawIT = Image.Draw(imageText)

#method to convert text to binary
def txt2Bin(textMessage):
    binary = bin(int(binascii.hexlify(message),16))
    return binary[2:]

#method to convert text length to binary
def len2Bin(textMessage):
    out = (len(message))
    s1 = 'Length of string is: '
    print(s1 + str(out))
    print('')
    s2 = 'Binary text length is: '
    print(s2 + bin(out))

#method to encode text to image
def encode(text2Code,ImgPic):
    #check image compatibiilty
    if ImgPic.mode!='RGB':
        print('Image not compatible, choose another')
        return false

    #split the rbg values
    img = Image.open('testImage.png')
    red = img.split()[0]
    green = img.split()[1]
    blue = img.split()[2]

    xCoord = img.size[0]
    yCoord = img.size[1]

    imageTEXT = writeText(text2Code,img.size)
    #convert to binary
    back = text2Binary(text2Code)

    #encode the text to the image
    enc_image = Image.new("RBG",(xCoord,yCoord))
    pixels = enc_image.load()
    #filling in the pixels
    for i in range(xCoord):
        for j in range(yCoord):
            r = bin(red.getpixel((i,j)))
            b = bin(blue.getpixel((i,j)))
            g = bin(green.getpixel((i,j)))

            result = bin(enc_image.getpixel((i,j)))

            if result[-1] == '1':
                r = red[:-1] + '1'
            else:
                r = red[:-1] + '0'
            pixels[i,j] =

#method to extract message from image
def decode(picture_location):
    #pull up image from directory
    secret = Image.open(testImage.png)
    #rotate the image from bottom right to top left format
    secret2 = secret.rotate(180)

    #get the rgb values
    rojo = secret.split()[0]
    azul = secret.split()[1]
    verde = secret.split()[2]

    #length and width of image
    xAxis = secret.size[0]
    yAxis = secret.size[1]
    #test to print out size
    print(secret.size)

    secret = Image.new("RGB",secret.size)
    pixels = secret.load()

    for i in range(xAxis):
        for j in range(yAxis):

            return message

"""
def text2Binary(text):
    test = 'test'
    for letter in text:
        print(ord(letter))
"""

if __name__ == "__main__":
    #sample string testing
    #text2Binary('felipe')

    #option to encode the text to image
    #what text to encode, what image to use, and where to save it
    if sys.argv[1] == '-e':
        message = sys.argv[2]
        picture = Image.open(sys.argv[3])
        encode(message,picture)
        pic.save(sys.argv[4])
    #option to decode text from image
    elif sys.arg[1] == '-d':
        pic = Image.open(sys.argv[2])
        message = decode(picture)
        print message

    #call method to print text to binary
    txt2Bin(sys.argv[2])

    #call method to print text length to binary
    len2Bin(sys.argv[2])
