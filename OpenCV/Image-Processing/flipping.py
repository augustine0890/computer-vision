import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

flipped = cv2.flip(image, 1) #flip around y-axis
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, 0) #flip around x-axis
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1) #flip around both axes
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
