#!/usr/bin/env python3

"""
Çizim Fonksiyonlari
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
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8") # image mesajını cv2ya çevir renkli
        cv2.line(img,(0,0),(250,250),(255,0,0),5)   
        #imgin üzerine,0,0dan başlayan 250ye250de biten,mavi renkli, 5 kalınlıklı çizgi
        cv2.rectangle(img,(250,175),(500,125),(123,23,200),3)
        #imgin üzerine,sol üst,sağ alt köşe,renk,kalınlık dikdörtgen
        cv2.circle(img,(100,100),10,(0,0,255),-1) #-1 içini doldurur
        #imgin üzerine merkez noktası,yarıçapı,renk,kalınlık çizen çember
        cv2.putText(img,"ROS",(0,250),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)
        # imgin üzerine, yazı,başlangıç,font,yazı boyutu, renk, kalınlık
        cv2.imshow("Robot Kamerasi",img) #imgi göster
        cv2.waitKey(1)
        
Kamera()