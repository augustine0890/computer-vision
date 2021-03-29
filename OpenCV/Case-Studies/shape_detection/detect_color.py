from utils.shapedetector import ShapeDetector
from utils.colorlabeler import ColorLabeler
from utils.shapedetector import *

import argparse
import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that the shapes can be approximated better
image = cv2.imread(args["image"])

resized = resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# blur the resized image slightly, then convert it to both
# grayscale and the L*a*b* color spaces
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# initialize the shape detector and color labeler
sd = ShapeDetector()
cl = ColorLabeler()

for c in cnts:
    # chareacterize the shape of an object: area, centroid, orientation etc.,
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
    else:
        cX, cY = 0, 0

    shape = sd.detect(c)
    color = cl.label(lab, c)
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # draw the contour and show name of shape

    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    text = "{} {}".format(color, shape)
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, text, (cX, cY),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # show the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
