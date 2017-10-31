
---------------------
Felipe Perez
http://github.com/05e46/Steganography-Python
Due Date: 10/31/2017

Purpose: Hide a text inside an image and conform to the listed requirements

Requirements
--------------
-text embedded inside images
-converts text to binary
-converts text length to binary
-use the bottom right 11 pixels to hide the text length
-use the remaining pixels to hide the text
-replace the least significant bit of the RGB values (leftmost bit)
-consumes jpeg image
-exports png image
-extract text length from image
-extract text from image

Program Architecture
---------------------
Running in Linux OS: Ubuntu 17.10
           Python: 2.7
           Pip: 9.0.1

Run Program
-------------
1.Open terminal
2.run python "filename.py" with parameters (i.e: python stego.py -e 'hello' 'imagelocation' 'output to save to'
3.run python "filename.py" with the methods called in main

Miscellaneous
---------------
Please ignore test.py file. Created to test single methods and learn python
at the same time
