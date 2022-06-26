from dataclasses import dataclass
import uuid
from xmlrpc.client import DateTime
import cv2
from datetime import datetime
# import breeze_resources
# import uuid
import os

now = datetime.now()
time = now.strftime("%d-%m-%Y %H:%M:%S")
# print("date and time =", time)	
# a = str(uuid.uuid4())
path='/home/ronit/newfol/'
new = os.mkdir(f'{path}'+str(time))
count =0 

cap = cv2.VideoCapture('/home/ronit/Downloads/SampleVideo_1280x720_5mb.mp4')
while True:
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    cv2.imwrite(str(path)+str(time)+'/'+'Frame_'+str(count)+".jpg",frame)
    count = count+1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
    
    
    



    