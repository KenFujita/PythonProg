import cv2
#import numpy as np
import matplotlib.pyplot as plt

cascade_path = "./haarcascade_frontalcatface.xml"

img = cv2.imread('./gorillaface/gorillaface3.jpg')
#cv2.imshow("test",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier(cascade_path)

facerect = cascade.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=1,minSize=(1,1))
print("rect angle")
print(facerect)

if len(facerect) > 0:
    for rect in facerect:
        cv2.rectangle(img,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),(255,255,255),thickness=2)
    #cv2.imshow("result",img)
#img[img < 100]=1
#img[img >= 130]=0
    plt.imshow(img)
    plt.colorbar()
    plt.show()

