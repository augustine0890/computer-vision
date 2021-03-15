from glob import glob
import numpy as np
import cv2

female_path = glob('./data/female/*.png')
male_path = glob('./data/male/*.png')
# print(len(female_path))
# print(len(male_path))

path = male_path[7]
img = cv2.imread(path)
# cv2.imshow("Face", img)
# cv2.waitKey(0)

# convert image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
# cv2.imshow("Face-Gray", gray)
# cv2.waitKey(0)

# Load haar cascade classifier
faceCascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
# draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
# crop the image
crop_img = img[y:y+h, x:x+h]
# cv2.imshow("Crop-Image", crop_img)
# cv2.waitKey(0)

def extract_image(path, gender, index):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        roi = img[y:y+h, x:x+h]
        if gender == 'female':
            cv2.imwrite('./data/faces/female/{}.png'.format(index), roi)
        else:
            cv2.imwrite('./data/faces/male/{}.png'.format(index), roi)

for i, path in enumerate(female_path):
    extract_image(path, 'female', i)
    
for i, path in enumerate(male_path):
    extract_image(path, 'male', i)


