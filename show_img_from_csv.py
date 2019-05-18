from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

def show_image(imgpath):
    img = Image.open(imgpath)
    img_li = np.asarray(img)
    plt.imshow(img_li)
    plt.show()

csv_file = sys.argv[1]  # input the file name which record the image name

with open(csv_file) as f:
    reader = csv.reader(f)
    for row in reader:
        imgname = row[0].replace(' ','')
        show_image(imgname)
