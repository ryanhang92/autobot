import pyscreenshot as screen
import numpy as np
import cv2

class Image_Capture(object):
    def __init__(self):

    @staticmethod
    def capture(self, top_left_coordinate, bottom_right_coordinate):
        img = screen.grab(bbox=(self.topLeft[0], self.topLeft[1], self.bottomRight[0], self.bottomRight[1]))
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

