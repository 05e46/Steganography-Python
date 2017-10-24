from PIL import Image
from PIL import ImageFont

#image object to work with
#image1 = Image.open('m3.jpg')
#image1.show()
#image1.save('m3.png')


image = Image.open('m3.jpg')
fontType = ImageFont.truetype('arial.ttf',encoding='unic')
draw = ImageDraw.Draw(image)
draw.text(xy==(50,50),text='dont be a little bitch',fill=(255,60,0),font=fontType)
image.show()
