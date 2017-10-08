import pyscreenshot as screen
import threading
import time

class ImageCapture(object):
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def imgCapture(self):
        img = screen.grab(bbox=(self.topLeft[0], self.topLeft[1], self.bottomRight[0], self.bottomRight[1]))
        img.show()

    def capture(self, frequency, duration=0):
        imgThread = threading.Timer(frequency, self.imgCapture)
        imgThread.start()

        if duration != 0:
            time.sleep(duration)
            imgThread.canel()
