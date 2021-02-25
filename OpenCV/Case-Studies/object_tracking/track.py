# US
import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
# path to video file on disk
ap.add_argument("-v", "--video",
    help="Path to the (optional) video file")
args = vars(ap.parse_args())

# track shades of blue
# blueLower = np.array([100, 67, 0], dtype="uint8")
# blueUpper = np.array([255, 128, 50], dtype="uint8")

greenLower = np.array([0, 100, 51], dtype="uint8")
greenUpper = np.array([102, 255, 178], dtype="uint8")

# load the video
camera = cv2.VideoCapture(args["video"])

"""
--grabbed: boolean, whether or not the frame was successfully read from video file.
--frame: frame
"""
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    # thresholded image, with pixels falling within the upper and lower range
    # blue = cv2.inRange(frame, blueLower, blueUpper)
    green = cv2.inRange(frame, greenLower, greenUpper)
    green = cv2.GaussianBlur(green, (3, 3), 0)

    (cnts, _) = cv2.findContours(green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        # largest contour
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0] # cv2.contourArea: compute the area of the contour

        # cv2.minAreaRect: compute the minimum bounding box around the contour
        # cv2.boxPoints: re-shapes the bounding box to be a list of points
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 0, 255), 2)
    
    cv2.imshow("Tracking", frame) # frame with the detected object
    cv2.imshow("Binary", green) # thresholded image is displayed

    time.sleep(0.025)

    if cv2.waitKey(1) & 0xFF == ord("q"): # the 'q' key is pressed
        break

camera.release()
cv2.destroyAllWindows()