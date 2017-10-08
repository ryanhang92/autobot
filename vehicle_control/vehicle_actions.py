import time
from windows_actions import Windows_Actions

W_KEY = 0x11
A_KEY = 0x1E
S_KEY = 0x1F
D_KEY = 0x20

SLEEP_INTERVAL = 0.5

class Vehicle_Control(object):

    @staticmethod
    def forward():
        Windows_Actions.PressKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)
        Windows_Actions.ReleaseKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)

    @staticmethod
    def backward():
        Windows_Actions.PressKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)
        Windows_Actions.ReleaseKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)

    @staticmethod
    def left():
        Windows_Actions.PressKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)
        Windows_Actions.ReleaseKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)

    @staticmethod
    def right():
        Windows_Actions.PressKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)
        Windows_Actions.ReleaseKey(W_KEY)
        time.sleep(SLEEP_INTERVAL)


