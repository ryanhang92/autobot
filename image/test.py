from imageCapture import ImageCapture
import numpy as np
import cv2

def test():
    imgCapture = ImageCapture((0,0) , (700,700))
    cv2.imshow('grayscale', imgCapture.capture())
    cv2.waitKey(0)

if __name__ == '__main__':
    test()
