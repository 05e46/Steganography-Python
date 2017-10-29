from PIL import Image, ImageFont, ImageDraw


#image object to work with
#image1 = Image.open('m3.jpg')
# image1.show()
#image1.save('m3.png')

"""
image = Image.open('m3.jpg')
fontType = ImageFont.truetype('arial.ttf',encoding='unic')
draw = ImageDraw.Draw(image)
draw.text(xy==(50,50),text='dont be a little bitch',fill=(255,60,0),font=fontType)
image.show()
"""
#method to write text to RGB image
def writeText(text, imgSize):

    imageText = Image.new("RGB",imgSize)
    font = ImageFont.load_default().font
    Image.Draw(imageText)

#method to encode text to image
def encode(text2Code,ImgPic):
    #split the rbg values of image
    img = Image.open('m3.jpg')
    red = img.split()[0]
    green = img.split()[1]
    blue = img.split()[2]

def text2Binary(text):
    test = 'test'
    for letter in text:
        print(ord(letter))


if __name__ == "__main__":
    text2Binary('felipe')
