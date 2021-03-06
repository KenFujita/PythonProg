# draw rect angle by matplotlib
import numpy as np
import matplotlib.pyplot as plt

class DrawRectangle:

    def __init__(self,np_img):
        # 初期値
        self.x1  = 0
        self.y1  = 0
        self.x2  = 0
        self.y2  = 0

        # フラグ類
        self.DragFlag = False
        self.PlotFlag = False
        self.StopFlag = False

        # ソート
        self.ix1, self.ix2 = sorted([self.x1,self.x2])
        self.iy1, self.iy2 = sorted([self.y1,self.y2])

        # plot
        plt.close('all')
        self.np_img = np_img
        self.fig = None
        self.ax2 = None

        self.lns = []
        self.rect_list = []

    # 押した時
    def Press(self,event):
        # 丸める
        cx = int(round(event.xdata))
        cy = int(round(event.ydata))

        self.x1 = cx
        self.y1 = cy

        # フラグをたてる
        self.DragFlag = True
        self.PlotFlag = False

    # ドラッグした時
    def Drag(self,event):
        # ドラッグしていなければ終了
        if self.DragFlag == False:
            return
        # 丸める
        cx = int(round(event.xdata))
        cy = int(round(event.ydata))
        self.x2 = cx
        self.y2 = cy
        # ソート
        self.ix1, self.ix2 = sorted([self.x1,self.x2])
        self.iy1, self.iy2 = sorted([self.y1,self.y2])
        # 四角形を更新
        self.DrawRect(self.x1,self.x2,self.y1,self.y2)
        # 描画
        plt.draw()

    # 離した時
    def Release(self,event):
        # フラグをたおす
        self.DragFlag = False
        self.PlotFlag = True
        self.rect_list.append([self.x1,self.y1,self.x2-self.x1,self.y2-self.y1])
        print(self.rect_list)
        #for l in rect_list:
        self.DrawRect(self.x1,self.x2,self.y1,self.y2)
        plt.draw()

    # キーボードのキーが押された時
    def onKey(self,event):
        # キーボードの'a'が押されたとき
        if event.key == 'a':
            print("a is press!!")
            self.rect_list.clear()
            print(self.rect_list)
            self.fig.delaxes(self.ax2)
            self.lns.clear()
            self.conf_plt(0,0,0,0)
            plt.draw()
        # キーボードの'n'が押されたとき
        if event.key == 'n':
            print("let's go next image!!")
            plt.close('all')
        if event.key == 'm':
            print("finish detect rectangle")
            self.StopFlag = True
            plt.close('all')

    # 四角形を描く関数
    def DrawRect(self,x1,x2,y1,y2):
        # 四角形の座標を指定
        Rect = [ [ [x1,x2], [y1,y1] ],
                 [ [x2,x2], [y1,y2] ],
                 [ [x1,x2], [y2,y2] ],
                 [ [x1,x1], [y1,y2] ] ]
        for i, rect in enumerate(Rect):
            if self.PlotFlag:
                self.ax2.plot(rect[0],rect[1],color='r',lw=1)
            else:
                self.lns[i].set_data(rect[0],rect[1])
                #print([x1,x2,y1,y2])

    # pltの初期化
    def conf_plt(self,x1,x2,y1,y2):

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.DragFlag = False
        # plot
        plt.close('all')
        self.fig = plt.figure(figsize=(8,4))

        # subplot 1
        #ax1 = fig.add_subplot(1,1,1)
        self.ax2 = self.fig.add_subplot(1,1,1)

        # 画像を描画
        #im1 = ax1.imshow(img)

        # 四角形を描画
        Rect = [ [ [self.x1,self.x2], [self.y1,self.y1] ],
                 [ [self.x2,self.x2], [self.y1,self.y2] ],
                 [ [self.x1,self.x2], [self.y2,self.y2] ],
                 [ [self.x1,self.x1], [self.y1,self.y2] ] ]

        for rect in Rect:
            ln, = self.ax2.plot(rect[0],rect[1],color='r',lw=1)
            self.lns.append(ln)
            #print(lns)

        # カラーマップの範囲を合わせる
        #ax1.set_clim(im1.get_clim())

        # 軸を消す
        plt.axis('off')

        # 背景画像を表示
        plt.imshow(self.np_img)

        # イベント
        plt.connect('button_press_event', self.Press)
        plt.connect('motion_notify_event', self.Drag)
        plt.connect('button_release_event', self.Release)
        plt.connect('key_press_event', self.onKey)

        plt.show()

        return self.StopFlag,self.rect_list


from PIL import Image
import csv
import glob
import sys
import os

img_fol = sys.argv[1] + '*'
file_l = [ fn for fn in glob.glob(img_fol) ]
print("sum of file: {}".format(str(len(file_l))))
index = 0

# 途中から始められるよう前回終了時の次の画像のindexを読み込む
if os.path.exists('/path/to/tmp_index'):
    with open('/path/to/tmp_index') as f:
        index = int(f.read())+1

for i,fnm in enumerate(file_l):
    print("now list of {}".format(str(i)))
    if i < index:
        continue
    posi_img = []
    posi_img.append(fnm)

    # 画像を開く
    img = Image.open(fnm)
    # numpy.ndarrayに
    img = np.asarray(img)

    dr_rect = DrawRectangle(img)
    stop_f,img_points = dr_rect.conf_plt(0,0,0,0)

    print("done")
    sum_rect = len(img_points)
    posi_img.append(sum_rect)
    for n in range(sum_rect):
        x,y,w,h = img_points[n]
        if x==0 and y==0 and w==0 and h==0:
            break
        posi_img.append(x)
        posi_img.append(y)
        posi_img.append(w)
        posi_img.append(h)
    print(posi_img)

    if len(posi_img) == 2:
        # ネガ画像ファイルを登録するcsvを開く
        with open('/path/to/negacsv','a') as f:
            writer = csv.writer(f,delimiter=' ')
            # 単一行の場合はwriterow()を使う。複数行の場合はwriterows()
            nega_fullpath = os.path.abspath(posi_img[0])
            writer.writerow(nega_fullpath)
        img = None
        dr_rect = None
        if stop_f:
            # 最終の画像ファイルのindexを保存する
            with open('/path/to/tmp_index','w') as f:
                f.write(str(i))
                print("write tmp index")
            break
        continue

    # ポジ画像ファイルを登録するcsvを開く
    with open('/path/to/posicsv','a') as f:
        writer = csv.writer(f,delimiter=' ')
        # 単一行の場合はwriterow()を使う。複数行の場合はwriterows()
        writer.writerow(posi_img)
    img = None
    dr_rect = None
    if stop_f:              # ストップフラグが立ったら
        with open('/path/to/tmp_index','w') as f:
            f.write(str(i))
            print("write tmp index")
        break

with open('/path/to/posicsv') as f:
    posi_list = f.readlines()
    print("sum of posi: {}".format(str(len(posi_list))))
with open('/path/to/negacsv') as f:
    nega_list = f.readlines()
    print("sum of nega: {}".format(str(len(nega_list))))
