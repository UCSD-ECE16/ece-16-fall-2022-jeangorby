import numpy as np
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
size = (int(cap.get(3)), int(cap.get(4)))
result = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(*'MJPG'), 60, size, 0)

# result = cv2.VideoWriter(outfilename, fourcc, fps, (width, height), 0)
 
while(True):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        canny = cv2.Canny(gray, 100, 200)
        result.write(canny)
        cv2.imshow('frame',canny)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
result.release()
cv2.destroyAllWindows()