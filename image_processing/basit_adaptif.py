#!/usr/bin/env python3

"""
Basit ve Adaptif Eşikleme Yöntemleri
Basit eşikleme şekli dirk siyaha boyarken asaptif şekli daha ayrıntılı görmemizi sağlar sanki beyaz kağıda siyah kalemle şekli çizmiş gibi
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import matplotlib.pylab as plt

class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")  #düğüm oluştur
        self.bridge = CvBridge()   #köprü kurma
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        # ("konusu",Image mesajı üzerinden işlemleri gerçekleştiren,abone olunduğunda gidilecek fonksiyon)
        rospy.spin() #sürekli yapılması için
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8") # image mesajını cv2ya çevir "bgr8"(renkli), "mono8"(gri)
        ret, esiklenmis = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # imge 127 eşik, eşiği aşanlara255
        a_esiklenmis = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY,11,2) #eşiği aşanlar 255,blok büyüklüğü 11, sabit2
        cv2.imshow("Robot Kamerasi",img) #imgi göster
        cv2.imshow("Basit Esikleme",esiklenmis)
        cv2.imshow("Adaptif Esikleme",a_esiklenmis)
        cv2.waitKey(1)

Kamera()