# autobot
Running the world.

# Design Docs

1) Sensor

    a) Image Capture


    b) Image Processing / computer vision
        0) image manipulation for easier process, like filtering

        a) Lane detection and highlighting for steering purposes

        b) Detecting the most important features in an image, like cars in front, stop signs, people and distances relative to car, for
            reactive behaviour
        
        c) Outputing all relavant data to decision making process

2) AI Driving

    A) Driving response to detected objects and images, based on processing all data from inputs

        1) Non ai, slope detection
        
        2) Deep learning controller based lane steering, stopping, and go-ing, based on all relevant data in image processing


3) Controls 

    a) Control Interface with computer game input

