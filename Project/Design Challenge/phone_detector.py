from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from utils.plots import plot_results
import cv2
import torch
import time
import urllib.request
from urllib.error import HTTPError
import numpy as np
import http.client
import socket

# socket.setdefaulttimeout(10.0)  # or whatever

<<<<<<< Updated upstream
phone_cascade = cv2.CascadeClassifier("Phone_Cascade.xml")
# url = 'http://192.168.0.24/800x600.jpg' #HC IP
url = 'http://192.168.1.214/800x600.jpg'  #JG IP

# phone_view = CircularList([], 5)
# comms = Communication("COM11", 115200)  #HC Comms
comms = Communication("COM7", 115200)     #JG Comms
=======
# phone_cascade = cv2.CascadeClassifier("Phone_Cascade.xml")
model = torch.hub.load('ultralytics/yolov5', 'yolov5x6')              # importing yolo v5 model

url = 'http://192.168.0.24/640x480.jpg'
# url = 'http://192.168.4.1/1280x720.jpg'

# phone_view = CircularList([], 3)

comms = Communication("COM7", 115200)
>>>>>>> Stashed changes
comms.clear()

current_time = 0
pre_time = 0

try:
    pre_time = time.time_ns()
    pre_time = pre_time / 1000
    while True:
<<<<<<< Updated upstream
        current_time = time.time()
        current_time = current_time 

        if(current_time - pre_time >= 0.2):
            
            imgRespond = urllib.request.urlopen(url)
            print(imgRespond.status)
            response_size = imgRespond.headers.get("content-length")
            print("Response Size: ", response_size)
            
            try:
                # the program gets stuck on the read() function
                imgnp = np.array(bytearray(imgRespond.read(int(response_size))), dtype=np.uint8)

                print("Image Size: ", imgnp.shape)
                img = cv2.imdecode(imgnp, -1) 

                pre_time = current_time
                print(imgRespond)
            # except (http.client.IncompleteRead) as e:
            #     page = e.partial
            #     print(e)
            # except Exception as e:
            #     print(e.__class__, " occured")
            except HTTPError as e:
                print(e)
                continue

        else:
            continue
=======
        current_time = time.time_ns()
        current_time = current_time / 1000


        imgRespond = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(imgRespond.read()), dtype=np.uint8)
        img = cv2.imdecode(imgnp, -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # phones = phone_cascade.detectMultiScale(gray, 3, 9)
>>>>>>> Stashed changes

        # for (x, y, w, h) in phones:
        #     cv2.rectangle(img, (x,y), ((x+w),(y+h)), (0, 255, 0), 3)
        #
        # phones_len = len(phones)
        # phone_view.add(phones_len)

        result = model(img)
        result.show()
        result.print()

<<<<<<< Updated upstream
        phones_len = len(phones)
        # phone_view.add(phones_len)

        if(phones_len > 0):
            print("Phone detected")
            comms.send_message("detected")
        else:
            comms.send_message("undetected")
=======
        # Streaming result

        if(current_time - pre_time >= 1500):
            pre_time = current_time

            # if all(item > 0 for item in phone_view):
            #     comms.send_message("detected")
            #     print("detected")
            # else:
            #     comms.send_message("undetected")
            #     print("undetected")
>>>>>>> Stashed changes

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break


except(Exception, KeyboardInterrupt) as e:
    print(e)
finally:
    print("Closing Connection.")
    comms.close()
    cv2.destroyAllWindows()
