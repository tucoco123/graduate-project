#encoding:utf-8
import os
from PIL import Image
import face_recognition

files = [f for f in os.listdir('.') if os.path.isfile(f)]
num = 0
name = []

#抓資料夾圖片的檔名
for f in files:
    if f.find("jpg")>0 and f.find("aftercut")<0:
        name.append(f[0:-4])
        num+=1

for i in name:
    #打開的圖片檔檔名
    ImageName= i
    filetype='.jpg'

    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(ImageName+filetype)

    #使用默認的基於HOG的模型查找圖像中的所有面部。
    #這種方法相當準確，但不如CNN模型準確，也沒有GPU加速。
    #另請參閱：find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    print("圖片裡找到 {} 個face".format(len(face_locations)))

    for face_location in face_locations:
        
        # Print此圖像中每張臉的位置
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        #計算放大20%的座標
        img=Image.open(ImageName+filetype)
        rl=(right-left)*0.2
        bt=(bottom-top)*0.2
        left=left-rl
        right=right+rl
        top=top-bt
        bottom=bottom+bt
        #若超過圖片邊界取至邊界值
        if left<0:
            left=0
        if top<0:
            top=0
        #img.size[0]=寬，img.size[1]=高
        if right>img.size[0]:
            right=img.size[0]
        if bottom>img.size[1]:
            bottom=img.size[1]
        #裁切圖片(左,上,右,下)
        new_img=img.crop((left,top,right,bottom))
#        new_img.show()
        #存檔
        new_img.save(ImageName+'_aftercut'+filetype)


