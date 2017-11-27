import time
from sensor.image_capture import Image_Capture
from sensor_processing.image_processor import Image_Processor

image_capture = Image_Capture()
image_processor = Image_Processor()

SCREEN_TOP_LEFT = (0, 0)
SCREEN_BOTTOM_RIGHT = (700, 700)

# Takes an image and the outputs a command
def driving():
    image_sensor_state = image_capture.capture(SCREEN_TOP_LEFT, SCREEN_BOTTOM_RIGHT)





# Starts drive polling process
def start_driving():
    while True:
        time.sleep(1)
        driving()



