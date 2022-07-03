import qrcode
from pyqrcode import *
import png

while True:
    s = input("Enter url: ")
    n = input("Enter name: ")

    img = pyqrcode.create(s)
    img.png("{}.png".format(n),scale = 6)
    print("done")

