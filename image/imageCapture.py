import pyscreenshot as screen
import numpy as np
import cv2

class ImageCapture(object):
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def capture(self):
        img = screen.grab(bbox=(self.topLeft[0], self.topLeft[1], self.bottomRight[0], self.bottomRight[1]))
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
