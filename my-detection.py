""" import jetson.inference
import jetson.utils


net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput()

while True:
    img=camera.Capture()
    detections=net.Detect(img)
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS())) """

import jetson.inference
from jetson.inference import detectNet
import jetson.utils
from jetson.utils import videoSource, videoOutput
import time
# from playsound import playsound

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource('/dev/video0')
display = jetson.utils.videoOutput("detecttest1.mp4")
# playsound("alarm-clock-short-6402.mp3")
while True:
    img = camera.Capture()

    if img is None: 
        continue

    current_time=time.strftime("%Y-%m-%d %H:%M:%S")

    detections = net.Detect(img)

    for detection in detections:
        confidence=detection.Confidence
        class_id=detection.ClassID
        class_name=net.GetClassDesc(class_id)
        print(f"At {current_time} a {class_name} was detected with {confidence:.2f} confidence.")
    
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))