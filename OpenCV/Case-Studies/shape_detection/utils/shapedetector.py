import cv2

"""
- Contour approximation: reducing the number of points on a curve to a more simple approximated.
- Common values for the second parameter to 'cv2.approxPolyDP' are normally in range of 1-5% of the
    original contour perimeter
"""
class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        # initialize the shape name and approximate the contour
        shape = "unidentified"
        # compute perimeter contour
        peri = cv2.arcLength(c, True)
        # assumption that a curve can be approximated by a series of short line segments
        approx = cv2.approxPolyDP(c, 0.04 * peri, True) # list of vertices
        # 3 vertices -> triangle
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            # compute bounding box of the contour and use bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # square: aspect ratio is rounding 1, otherwise, rectangle
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"
        
        return shape

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized