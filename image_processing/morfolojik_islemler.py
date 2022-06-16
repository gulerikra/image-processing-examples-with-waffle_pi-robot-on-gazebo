#!/usr/bin/env python3

"""
Morfolojik işlemler
"""

import rospy
import cv2 
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np

class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")  #düğüm oluştur
        self.bridge = CvBridge()   #köprü kurma
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        # ("konusu",Image mesajı üzerinden işlemleri gerçekleştiren,abone olunduğunda gidilecek fonksiyon)
        rospy.spin() #sürekli yapılması için
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8") # image mesajını cv2ya çevir gri
        ret,esiklenmis = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
        kernel = np.ones((11,11),np.uint8) #11e 11 boyutunda 1lerden oluşan uint8 formatında bir kernel
        e_img = cv2.erode(esiklenmis,kernel)  #görüntüdeki gürültüleri kaldırdı
        d_img = cv2.dilate(esiklenmis,kernel) #görüntüdeki kopuklukları(gürültüyü birleştirdi gibi) tamamladı 
        f_img = d_img - e_img  #şeklin şeklini (dışını) çizdi gibi
        o_img = cv2.morphologyEx(esiklenmis,cv2.MORPH_OPEN,kernel)  #şeklin dışındaki gürültüleri kaldırır
        c_img = cv2.morphologyEx(esiklenmis,cv2.MORPH_CLOSE,kernel) #şeklin içindeki gürültüleri kaldırır
        cv2.imshow("Robot Kamerasi",img)
        cv2.imshow("Esiklenmis",esiklenmis)
        cv2.imshow("Erosion",e_img)
        cv2.imshow("Dilation",d_img)
        cv2.imshow("Morfolojik Gradyan",f_img)
        cv2.imshow("Opening",o_img)
        cv2.imshow("Closing",c_img)
        cv2.waitKey(1)
        
Kamera()
