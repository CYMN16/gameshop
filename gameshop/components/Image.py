import traceback
from tkinter import *

from PIL import Image, ImageTk
import requests

import os

class showImage():
    def __init__(self, win, image, padxv, padyv, sizew, sizeh):
        self.win = win
        self.padxv = padxv
        self.padyv = padyv
        self.sizew = sizew
        self.sizeh = sizeh
        try:
            path = os.curdir + "/gameshop/img/" + str(image)[-5:] + ".png"

            if not os.path.exists(path):
                img_data = requests.get(image).content
                with open(path, 'wb') as handler:
                    handler.write(img_data)

            self.photo = Image.open(path).resize((sizew, sizeh))
            self.photo2 = ImageTk.PhotoImage(self.photo)
            self.label = Label(win, image=self.photo2)
            self.label.image = self.photo2
            self.label.place(x=padxv, y=padyv)
        except Exception as e:
            print("opening image failed : ", e)
            print(traceback.format_exc())

    def changeImage(self, image):
        try:
            path = os.curdir + "/gameshop/img/" + str(image)[-5:] + ".png"

            if not os.path.exists(path):
                img_data = requests.get(image).content
                with open(path, 'wb') as handler:
                    handler.write(img_data)

            self.photo = Image.open(path).resize((self.sizew, self.sizeh))
            self.photo2 = ImageTk.PhotoImage(self.photo)
            self.label.configure(image=self.photo2)
            self.label.image = self.photo2
        except Exception as e:
            print("image change failed : ", e)
            print(traceback.format_exc())
