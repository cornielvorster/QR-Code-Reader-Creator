import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser



class read():

    def __init__(self):
        pass
# load the QR code image file
    def readQR():
        userIn = (input("Enter a image name: ") + ".png" )
        img = cv2.imread(userIn)

        # convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detect QR codes in the image
        decoded = pyzbar.decode(gray)

        # loop over the detected QR codes
        for obj in decoded:
            # print the QR code data
            qrLink = obj.data.decode("utf-8")
        # specify the link you want to open

        webbrowser.open(qrLink, new=1)

