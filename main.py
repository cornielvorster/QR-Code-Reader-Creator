from read import *
from create import *

if __name__ == '__main__':
    print('QR Code Creator and Reader\nChoose an option \n1- Create a QR code \n2- Read a QR \n3- Exit')
    user = input('Choose an option 1, 2 , 3')
    if user == '1':
        create.createQR()
    elif user == '2':
        read.readQR()
    elif user == '3':
        exit
    else:
        ('Invalid Input 1, 2, 3')

