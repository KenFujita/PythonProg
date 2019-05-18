from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

del_flag = False

def onKey(event):
    if event.key == 'd':
        print("this image delete csv!")
        del_flag = True
        plt.close('all')
    if event.key == 'n':
        print("go to next image")
        plt.close('all')

def show_image(imgpath):
    img = Image.open(imgpath)
    img_li = np.asarray(img)
    plt.imshow(img_li)
    plt.connect('key_press_event',onKey)
    plt.show()

csv_file = sys.argv[1]  # input the file name which record the image name

with open(csv_file) as f:
    reader = csv.reader(f)
    for row in reader:
        imgname = row[0]
        print(imgname)
        show_image(imgname)
