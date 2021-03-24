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
class ColorLabler:
    def __init__(self):
        colors = OrderedDict({
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255)
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