#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uygulama 5: Kameradan Gelen Veriyi Görüntüye Çevirme
"""

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class RobotKamera():
    def __init__(self):
        rospy.init_node("kamera")
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        self.bridge = CvBridge()
        rospy.spin()
    
    def kameraCallback(self,mesaj):
        self.foto = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        cv2.imshow("Robot Kamerasi",self.foto)
        cv2.waitKey(1)

nesne = RobotKamera()