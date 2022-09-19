from utils import *
import cv2
from time import ctime , time 
w,h = 360,240
pid = [0.4,0.4,0]
pError = 0
startCounter = 0  # for no Flight 1   - for flight 0
 
 
myDrone = initializeTello()
 
#! initilization
XMLpath = './BinaryData/haarcascade_frontalface_default.xml' 
CodeBeginTime = ctime(time()).replace(':','_').replace(' ','_')
video = cv2.VideoWriter(f'video{CodeBeginTime}.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (w, h))

while True:
    
    #! Flight
    if startCounter == 0:
        myDrone.takeoff()
        myDrone.move_up(100)
        startCounter = 1
    ## Step 1
    img = telloGetFrame(myDrone,w,h)
    ## Step 2
    img, info = findFace(img , XMLpath)
    ## Step 3
    pError = trackFace(myDrone,info,w,pid,pError)
    #print(info[0][0])
    cv2.imshow('Image',img)
    video.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        video.release()
        break
