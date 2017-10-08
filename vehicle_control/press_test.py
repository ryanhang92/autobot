from vehicle_actions import Vehicle_Control

def test():
    for i in range(20):
        Vehicle_Control.forward()
        Vehicle_Control.backward()
        Vehicle_Control.left()
        Vehicle_Control.right()

test()
