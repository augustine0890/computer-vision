import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

rotated = imutils.rotate(image, angle=45, center=center, scale=1.0)
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, angle=180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, angle=-90)
cv2.imshow("Rotated by -90 Degress", rotated)
cv2.waitKey(0)