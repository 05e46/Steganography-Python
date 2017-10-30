import random
import sys
import os
import binascii
#from PIL import Image


"""img = Image.open('m3.jpg')
img.show()
"""

message = 'hello'
binary = bin(int(binascii.hexlify(message),16))
print (binary)
