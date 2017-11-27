import numpy as np
import cv2
from matplotlib import pyplot as plt

# https://github.com/naokishibuya/car-finding-lane-lines

class Image_Processor(object):
    def __init__(self):

    '''
    Processes an Image (Takes a color Image)
    1) Feature Detection, Line Detection Steering
    2) Queue Detection, Line

    1) Steering Features
    2) Acceleration / Speed Features
    '''
    @staticmethod
    def process_image(image):
        return True


    @staticmethod
    def return_roi_image(image):
        r = cv2.selectROI(image)
        image_cropped = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        return image_cropped


    # Experiment with different edge detectors
    def return_edge_images(image):
        edges = cv2.Canny(image, 10, 20, 3)
        '''
        plt.subplot(121), plt.imshow(image, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(image, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()
        '''
        return edges


    # http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    @staticmethod
    def return_line_images(edge_images):
        return True


    @staticmethod
    def process_image_for_steering(image):
        return True


    @staticmethod
    def process_image_for_acceleration(image):
        return True

