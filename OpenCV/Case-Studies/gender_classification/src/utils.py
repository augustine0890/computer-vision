import pickle, os
from glob import glob
import cv2
from PIL import Image
from time import time
from pathlib import Path
import numpy as np

# load the model
faceCascade = cv2.CascadeClassifier('../model/haarcascade_frontalface_default.xml')
# load pickle file
mean = pickle.load(open('../model/mean_preprocess.pickle', 'rb'))
pca_50 = pickle.load(open('../model/pca_50.pickle', 'rb'))
model_svm = pickle.load(open('../model/model_svm.pickle', 'rb'))

font = cv2.FONT_HERSHEY_SIMPLEX

def pipeline_model(path, filename, color='BGR'):
    # step 1: read image with cv2
    img = cv2.imread(path)
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
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2) # drawing rectangle
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
        text = "%s: %0.2f" % ('Male' if predict else 'Female', score)
        cv2.putText(img, text, (x+5,y-8), font, 0.9, (0,255,0), 1)
    
    cv2.imwrite('../static/results/{}'.format(filename), img)

def cleanfile(path, filename):
    paths = glob(os.path.join(path, 'static/results/*'))
    result = [os.remove(file) for file in paths if os.stat(file).st_mtime < time() - 120] # seconds