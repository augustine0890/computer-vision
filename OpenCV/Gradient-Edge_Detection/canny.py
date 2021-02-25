import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0) #remove noisy edges
cv2.imshow("Blurred", image)
cv2.waitKey(0)

# Gradient values below 30 are considered non-edges whereas any values above 150 are considered edges.
canny = cv2.Canny(image, 30, 150)
# canny = cv2.Canny(image, 10, 200)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
