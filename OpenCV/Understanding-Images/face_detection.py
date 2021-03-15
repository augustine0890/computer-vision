import numpy as np
import cv2


harr = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_dectect(img):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = harr.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)
    
    return img

cap = cv2.VideoCapture('../images/face.mp4')
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    frame = face_dectect(frame)
    cv2.imshow('face_dectect', frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): # the 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows()