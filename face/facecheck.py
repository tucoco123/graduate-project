#encoding:utf-8
import cv2
import dlib
import csv
from skimage import io

#設定檔名
ImageName='민새롬 Saerom Min-15'
imgstatus='_aftercut'
filetype='.jpg'

#open csv 寫入檔
csvname=ImageName+'_record.csv'
csvfile = open(csvname, 'w',newline='')
#設定字典
dic = ['index','coordinate_x','coordinate_y']
writer = csv.DictWriter(csvfile, fieldnames=dic)
writer.writeheader()


# 使用特徵提取器get_frontal_face_detector
detector = dlib.get_frontal_face_detector()
# dlib的68點模型，使用作者訓練好的特徵預測器
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# 圖片所在路徑
img = io.imread(ImageName+imgstatus+filetype)
# 生成dlib的圖像窗口
win = dlib.image_window()#能夠在螢幕上顯示圖像的GUI窗口
win.clear_overlay()#從image_window中刪除所有疊加層
win.set_image(img)#重載功能

# 特徵提取器的實例化
dets = detector(img, 1)
print("人臉數：", len(dets))

for k, d in enumerate(dets):
    print("第", k+1, "個人臉d的座標：",
          "left:", d.left(),
          "right:", d.right(),
          "top:", d.top(),
          "bottom:", d.bottom())
        
    width = d.right() - d.left()
    heigth = d.bottom() - d.top()
          
    print('人臉面積為：',(width*heigth))
    # 利用預測器預測
    shape = predictor(img, d)
    # 標出68個點的位置
    for i in range(68):
        #繪製圓圈cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度)
        cv2.circle(img, (shape.part(i).x, shape.part(i).y), 4, (0, 255, 0), -1, 8)
        #在圖片上加上文字cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
        cv2.putText(img, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        #印出68個點座標
        xy='x:'+str(shape.part(i).x)+',y:'+str(shape.part(i).y)
        print('第'+str(i)+'個點：'+xy)
        writer.writerow({'index' : i ,'coordinate_x': str(shape.part(i).x),'coordinate_y' : str(shape.part(i).y)})
    csvfile.close()
    # 顯示一下處理的圖片，然後銷燬窗口
    cv2.imshow('face', img)
    cv2.waitKey(0)

#{
#IdxRange jaw;       // [0 , 16]
#IdxRange rightBrow; // [17, 21]
#IdxRange leftBrow;  // [22, 26]
#IdxRange nose;      // [27, 35]
#IdxRange rightEye;  // [36, 41]
#IdxRange leftEye;   // [42, 47]
#IdxRange mouth;     // [48, 59]
#IdxRange mouth2;    // [60, 67]
#}


