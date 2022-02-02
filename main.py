from deepface import DeepFace
from tkinter import *
import imutils
import numpy as np
import cv2
from PIL import ImageTk,Image
from tkinter import filedialog
import gc
import winsound
from tqdm import tqdm
import os

def verf():
    global path

    img_path = filedialog.askopenfilename()
    path = img_path
    img = Image.open(img_path)
    img = img.resize((512, 512), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(80, 30, anchor=NW, image=img)

    img2 = cv2.imread(path, cv2.IMREAD_COLOR)

    ######verify######
    dataset='db'

    for img in tqdm(os.listdir(dataset)):

        path = os.path.join(dataset, img)
        img1 = cv2.imread(path, cv2.IMREAD_COLOR)

        result = DeepFace.verify(img1, img2)
        res = result["verified"]
        print(res)

        if res:
            winsound.PlaySound('mostafa.wav', winsound.SND_FILENAME)
            header = Label(text="His name is mostafa , he is your nephew and he is 24 years old")
            header.place(x=700, y=50)
            break


    ################################
    form.mainloop()


def main():

    ###########GUI#############

    Upload_butt = Button(text="   Upload   ", command=verf)
    Upload_butt.place(x=550, y=600)

    form.mainloop()
    ###########################

if __name__ == '__main__':
    form = Tk()
    canvas = Canvas(form, width=1200, height=650)
    canvas.pack()
    main()






