from imageCapture import ImageCapture

def test():
        imgCapture = ImageCapture((200,200) , (500,500))
        imgCapture.capture(30.0, duration=70)

if __name__ == '__main__':
    test()
