from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import sys

del_flag = False

def onKey(event):
    global del_flag         # globalで宣言しないと関数外の変数の中身を変更できない！！
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
'''
with open(csv_file) as f:
    reader = csv.reader(f)
    for row in reader:
        imgname = row[0]
        print(imgname)
        show_image(imgname)
'''
pd.set_option("display.max_colwidth", 120)  #pandasのカラム内の最大表示文字数
image_paths = pd.read_csv(csv_file,header=None,encoding="shift-jis",names=('img',),nrows=20)
for i,row in enumerate(image_paths['img']):
    #print('{}: {}'.format(str(i),row))
    show_image(row)
    print("finish show image")
    if del_flag:
        print("delete the image")
        image_paths.drop(i,inplace=True)    # 元のDataFrame(この場合はimage_paths)の値は変更されない
        del_flag = False
print(image_paths)
image_paths.to_csv(csv_file,header=False,index=False,columns=['img'])
print("rewrited image name to csv")
