import numpy as np
import cv2



cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read(0)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()