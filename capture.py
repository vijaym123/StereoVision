from SimpleCV import *
import cv2
import threading
import logging

def live(index1,index2):
    """
    **SUMMARY**
    This functions gives a live view of the two camera's.
    
    **PARAMETERS**
    * *index1* - The index of the camera 1.
    * *index2* - The index of the camera 2.
    
    **RETURNS**
    True : If the cameras are up and are working properly.
    False : If the they are not working.
    
    **EXAMPLE**
    >>> import capture
    >>> capture.live(0,1)
    """
    try :
        cam1 = Camera(1)
        cam2 = Camera(2)
        l_cam = threading.Thread(target=cam1.live)
        r_cam = threading.Thread(target=cam2.live) 
        l_cam.start()
        r_cam.start()
        return True
    except :
        logging.warning("Cannot initialise two camera's !")
        return False
