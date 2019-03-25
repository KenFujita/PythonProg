# draw rect angle by matplotlib
import numpy as np
import matplotlib.pyplot as plt

rect_list = []

# 押した時
def Press(event):
    global x1,y1,DragFlag,PlotFlag

    # 丸める
    cx = int(round(event.xdata))
    cy = int(round(event.ydata))

    x1 = cx
    y1 = cy

    # フラグをたてる
    DragFlag = True
    PlotFlag = False

# ドラッグした時
def Drag(event):
    global x1,y1,x2,y2,DragFlag

    # ドラッグしていなければ終了
    if DragFlag == False:
        return

    # 丸める
    cx = int(round(event.xdata))
    cy = int(round(event.ydata))

    x2 = cx
    y2 = cy

    # ソート
    ix1, ix2 = sorted([x1,x2])
    iy1, iy2 = sorted([y1,y2])

    # 四角形を更新
    DrawRect(x1,x2,y1,y2)

    # 描画
    plt.draw()

# 離した時
def Release(event):
    global x1,y1,x2,y2,DragFlag,PlotFlag
    # フラグをたおす
    DragFlag = False
    PlotFlag = True
    rect_list.append([x1,y1,x2-x1,y2-y1])
    print(rect_list)
    #for l in rect_list:
    DrawRect(x1,x2,y1,y2)
    plt.draw()

# キーボードのキーが押された時
def onKey(event):
    if event.key == 'a':
        print("q is press!!")
        DrawRect(0,0,0,0)
        rect_list.clear()
        print(rect_list)
        plt.draw()

# 四角形を描く関数
def DrawRect(x1,x2,y1,y2):
    global PlotFlag
    Rect = [ [ [x1,x2], [y1,y1] ],
             [ [x2,x2], [y1,y2] ],
             [ [x1,x2], [y2,y2] ],
             [ [x1,x1], [y1,y2] ] ]

    for i, rect in enumerate(Rect):
        if PlotFlag:
            plt.plot(rect[0],rect[1],color='r',lw=2)
        else:
            lns[i].set_data(rect[0],rect[1])
    #print([x1,x2,y1,y2])

# 画像を開く    
from PIL import Image
fnm = './gorillaface/gorillaface2.jpg'
img = Image.open(fnm)

# numpy.ndarrayに
img = np.asarray(img)

# 初期値
x1  = 0 
y1  = 0
x2  = 0
y2  = 0

# ドラッグしているかのフラグ
DragFlag = False

# ソート
ix1, ix2 = sorted([x1,x2])
iy1, iy2 = sorted([y1,y2])

# plot
plt.close('all')
plt.figure(figsize=(8,4))

# subplot 1
plt.subplot(1,1,1)

# 画像を描画
im1 = plt.imshow(img, cmap='gray')

# 四角形を描画
Rect = [ [ [x1,x2], [y1,y1] ],
         [ [x2,x2], [y1,y2] ],
         [ [x1,x2], [y2,y2] ],
         [ [x1,x1], [y1,y2] ] ]

lns = []
for rect in Rect:
    ln, = plt.plot(rect[0],rect[1],color='r',lw=2)
    lns.append(ln)
#print(lns)

# カラーマップの範囲を合わせる 
plt.clim(im1.get_clim())

# 軸を消す
plt.axis('off')

# イベント
plt.connect('button_press_event', Press)
plt.connect('motion_notify_event', Drag)
plt.connect('button_release_event', Release)
plt.connect('key_press_event', onKey)

plt.show()
