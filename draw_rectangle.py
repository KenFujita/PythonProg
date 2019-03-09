# drawing rect angle

import cv2

ix,iy = 0,0
drawing = False

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,img,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        print("push")
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            #print("drawing")
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        else:
            pass
    elif event == cv2.EVENT_LBUTTONUP:
        print("up")
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
        print((ix,iy),(x,y))

img = cv2.imread("./me.png")

window_name = "test image"
# named~とsetMouse~はセットでないとだめ
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name,draw_rectangle)

while(1):
    cv2.imshow(window_name,img)
    k = cv2.waitKey(1)
    # 27 = esc key (case by opencv)
    if k == 27:
        break
cv2.destroyAllWindows()




