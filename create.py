import qrcode
from PIL import Image

class create():

    def __init__(self):
        pass

    def createQR():
        data = input("Enter a link or data for the QR code: ")

        qr = qrcode.QRCode(version=1, box_size=10, border=5)

        qr.add_data(data)


        qr.make(fit=True)


        img = qr.make_image(fill_color="black", back_color="white")


        qrcodeName = (input('Enter a name for the QR Code: ') + ".png")

        img.save(qrcodeName )

