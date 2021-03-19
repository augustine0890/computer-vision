import pickle
import cv2
from PIL import Image

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from sklearn import metrics

# load the model
faceCascade = cv2.CascadeClassifier('../model/haarcascade_frontalface_default.xml')
# load pickle file
mean = pickle.load(open('../model/mean_preprocess.pickle', 'rb'))
pca_50 = pickle.load(open('../model/pca_50.pickle', 'rb'))
model_svm = pickle.load(open('../model/model_svm.pickle', 'rb'))

font = cv2.FONT_HERSHEY_SIMPLEX
# test data
# data_path = '../data/test/female_test.png'
data_path = '../data/test/putin.png'
# step 1: read image
# img = cv2.imread(data_path)
# color = 'BGR'

def pipeline_model(img, color='BGR'):
    # step 2: convert into gray scale
    if color == 'BGR':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # step 3: crop the face (using haar cascase classifier)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=10,
        minSize=(50, 50),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) # drawing rectangle
        roi = gray[y:y+h, x:x+h] # crop image

        # step 4: normalization (0-1)
        roi = roi / 255.0
        # step 5: resize image (80,80)
        if roi.shape[1] > 80:
            roi_resize = cv2.resize(roi, (80,80), cv2.INTER_AREA)
        else:
            roi_resize = cv2.resize(roi, (80,80), cv2.INTER_CUBIC)

        # step 6: Flattening (1x6400)
        roi_reshape = roi_resize.reshape(1, 6400) # 1, -1
        # step 7: Subtract with mean
        roi_mean = roi_reshape - mean

        # step 8: Get eigen image
        eigen_image = pca_50.transform(roi_mean)
        # step 9: Predict (svm)
        results = model_svm.predict_proba(eigen_image)[0]
        # step 10:
        predict = results.argmax() # 0 or 1
        score = results[predict]
        # step 11:
        text = "%s: %0.2f" % ('male' if predict else 'female', score)
        cv2.putText(img, text, (x+5,y-8), font, 0.7, (0,255,0), 2)

    return img

test_data_path = '../data/test/female_test.png'
# test_data_path = '../data/test/putin.png'
img = cv2.imread(test_data_path)
img = pipeline_model(img)
cv2.imshow('Gender Prediction', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply to video
cap = cv2.VideoCapture('../data/face.mp4')
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    frame = pipeline_model(frame)
    cv2.imshow('Gender Detector', frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): # the 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows()
