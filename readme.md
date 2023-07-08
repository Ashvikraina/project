# Detectnet

You point your camera around your room and it will detect most of what it can see and tell you what it detected and when.
Output: [Imgur](https://i.imgur.com/GUKBjRv.png)

## The Algorithm

([Imgur](https://i.imgur.com/VtioCM3.png))

import jetson.inference
from jetson.inference import detectNet
import jetson.utils
from jetson.utils import videoSource, videoOutput
import time

The code above imports everything necessary for the code to work

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource('/dev/video0')
display = jetson.utils.videoOutput("detecttest1.mp4")

Tells what camera source to use and the file name to stroe the video in. You can also try doing it with your live camera but it didn't work for me.

while True:
    img = camera.Capture()

    if img is None: 
        continue

This code captures frames of from the camera.

current_time=time.strftime("%Y-%m-%d %H:%M:%S")

This is how I added the time feature to the code.

detections = net.Detect(img)

This uses detectnet to detect the frames from the camera.

 for detection in detections:
      confidence=detection.Confidence
      class_id=detection.ClassID
      class_name=net.GetClassDesc(class_id)
      print(f"At {current_time} a {class_name} was detected with {confidence:.2f} confidence.")

This is where we define the variables to print when something is detected.

display.Render(img)
display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

This renders the detected image and sets the status of the display.

## Running this project

1. Go inside your terminal in vscode / putty.
2. SSH into your nano
3. Cd in the folder for your nano (Mine was home/nvidia), Make a directory named whatever you want. (Optional, I don't think you need to make a directory but I did) Command for making a directory: mkdir directory-name
4. Cd into that directory that you made and create a .py file. Code to cd into folder: cd foldername. Once you are in the folder, create a .py folder using the command touch filename.py.
5. Open the folder you created and copy and paste the code above. You will have to change the camera videoSource variable to whatever camera you have. You can also change the display variable depending on if you want it live or not. Since my live camera didn't work, I used a file to put the video in.
6. Make sure you are still in the folder that you created, and type in your terminal: python3 foldername.py. This will start the code running and it should work.
7. If you did the file output instead of live video, once you are done running the code press control c in your terminal to end the code.
8. Now you can open your file that has been created and see how the detectnet works!

[View a video explanation here](video link)
