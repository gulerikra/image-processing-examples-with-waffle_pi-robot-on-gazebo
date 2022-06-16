#!/usr/bin/env python3

"""
Geometrik Dönüşümler: Afin,Perspektif
Perspektif dönüşüm yaparak zemine daha yukarıdan bakmış oluruz
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
        rospy.spin() #işelemin sürekli yapılması için
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8") # image mesajını cv2ya çevirir
        # k1 = np.float32([[30,500],[200,500],[30,600]]) #rastgele noktalar aldık
        # k2 = np.float32([[15,500],[100,500],[15,600]]) #k1'in ilk değerlerinin yarıya inmiş hali
        # M = cv2.getAffineTransform(k1,k2)  #ki ve k2 arasında dönüşüm matrisi bul
        # afin = cv2.warpAffine(img,M,(640,480)) #img üzerinde  dönüşüm matrisini kullanarak 64a 480 boyutunda
        cv2.imshow("Robot Camera",img) #imgi göster
        # cv2.imshow("Afin Dönüşüm",afin) 
        k1 = np.float32([[5,250],[605,250],[5,400],[605,400]]) #kabaca 4 nokta aldık
        k2 = np.float32([[0,0],[640,0],[0,480],[640,480]])
        M = cv2.getPerspectiveTransform(k1,k2)  #M matrisi: ki ve k2 arasinda perspektif dönüşüm uygula
        perspektif = cv2.warpPerspective(img,M,(640,480)) #img üzerine,Mmatrisini uygula 640a 480 boyutu
        kenarlar = cv2.Canny(perspektif,100,200,5) #oerspektif+ kenar bulma
        cv2.imshow("Perspective",kenarlar)
        cv2.waitKey(1)
        
Kamera()
