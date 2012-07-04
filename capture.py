from SimpleCV import *
import cv2
import threading

cam1 = Camera(1)
cam2 = Camera(2)
l_cam = threading.Thread(target=cam1.live)
r_cam = threading.Thread(target=cam2.live) 
l_cam.start()
r_cam.start()
