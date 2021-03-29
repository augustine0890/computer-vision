from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

"""
- In order to label and tag regions of an image as containing a certain color.
    We'll computing the Euclidean distance between dataset of known colors and the
    averages of particular image region.
- The known color that minimizes the Euclidean distance will be chosen as the color identification.
"""
class ColorLabeler:
    def __init__(self):
        colors = OrderedDict({
            "red": (255, 0, 0),
            "orange": (255, 140, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0)
        })

        # allocate memory for the L*a*b* image, then initialize the colore names list
        self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []
        
        for (i, (name, rgb)) in enumerate(colors.items()):
            self.lab[i] = rgb
            self.colorNames.append(name)
        
        # convert the L*a*b array from the RGB color space to L*a*b
        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)


    def label(self, image, c):
        # construct a mask for the contour, the compute the average L*a*b value for masked region
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(image, mask=mask)[:3]

        # initialize the minimum distance
        minDist = (np.inf, None)

        # loop over the known L*a*b color values
        for (i, row) in enumerate(self.lab):
            # compute the distance between the current L*a*b
            # color value and the mean of the image
            d = dist.euclidean(row[0], mean)

            # if the distance is smaller then the current distance then update the bookkeeping variable
            if d < minDist[0]:
                minDist = (d, i)

        # return the name of the color with the smallest distance
        return self.colorNames[minDist[1]]