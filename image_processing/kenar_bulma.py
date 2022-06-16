#!/usr/bin/env python3
"""
Kenar Bulma İşlemleri
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Kamera():
    def __init__(self):
        rospy.init_node("kamera_dugumu")  #düğüm oluştur
        self.bridge = CvBridge()   #köprü kurma
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        # ("konusu",Image mesajı üzerinden işlemleri gerçekleştiren,abone olunduğunda gidilecek fonksiyon)
        rospy.spin() #sürekli yapılması için
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"mono8")  # image mesajını cv2ya çevir gri
        kenarlar = cv2.Canny(img,100,200,5)  #değerler değişebilir kenar bulma için
        cv2.imshow("Robot Kamerasi",img)
        cv2.imshow("Canny Kenarlar",kenarlar)
        cv2.waitKey(1)

Kamera()