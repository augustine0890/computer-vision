# OpenCV and Case Studies

**Required Packages**
- Create virtual environment
    - `python3 -m venv .env`
    - `source .env/bin/activate`
- Install OpenCV
    - `pip install opencv-python`
    - __DO NOT__ install both `opencv-python` and `opencv-contrib-python`. Pick __ONE__ of them.
    - [Reference](https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/)
- Install SciPy
    - `pip install scipy`
- Install Matplotlib
    - `pip install matplotlib`
- Install Mahotas
    - `pip install mahotas`
    - Fast computer vision algorithms (all implemented in C++ for speed) operating over numpy arrays.
- Install Scikit-learn for machine learning
    - `pip install scikit-learn`
- Install Scikit-image
    - `pip install -U scikit-image`
    - Collection of algorithms for image processing

## Loading, Displaying, and Saving
- Basic information on the image: width, height, and 3 channels(RGB components of the image).
- The Numpy array: (228, 350, 3). 228 pixels (number of rows) and 350 pixels (number of columns)
- Every image consists of a set of pixels. Pixels are the raw building blocks of an image.
- Most pixels are represented in two ways: grayscale and color.
    - Grayscale: each pixel has a value between 0 and 255 (black: zero, white: 255)
- Color pixels are represented in the RGB color space (Red-Green-Blue)
    - Each of the three colors is represented by an integerin the range 0 to 255, which indicates how much of the color there is.
    - Use an 8-bit unsigned integer to represent each color intensity.
    - Combine these values into an RGB tuple in the form `(red, green, blue)` --> represents color.
    - White color: (255, 255, 255), black color: (0, 0, 0)
- The point (0, 0) corresponds to the upper left corner of the image.
- Even though we specify pixels in terms of (x, y)-coordinates, when it comes to writing code, we access the individual pixel values as `image[y, x]`
- OpenCV stores RGB channels in _reverse order_ (Blue, Green, Red).

## Drawing
- Drawing operations allow us to draw Regions of Interest (ROIs) surrounding objects in an image.

## Image Processing
- While RGB is easy to understand, it's unintuitive when defining exact shades of a color if you need to define a particular range of colors.
- The `HSV` color space tends to be more intuitive terms of actually defining a particular color.
- `L*a*b*` color space tries to mimic the methodology in which humans see and interpret color. This implies that the Euclidean distance between two arbitrary colors in the `L*a*b*` color space have actual perceptual meaning.
- `HSV` to extract color histograms to quantify the contects of an image and even build an image search engine.

## Histograms
- A histogram represents the distribution of pixel intensities in an images.
- The color histogram is arguably the simplest way to quantify the contents of an image

## Smoothing and Blurring
- Apply blurring to reduce the details in the image, thereby allowing you to focus on the actual structual objects in the image.
- An image as a big matrix and a kernel as tiny matrix.
- At each `(x, y)`-coordinate of the original image, we stop and examine the neighborhood of pixels located at the __center__ of the image kernel. We then take this neighborhood of pixels, convolve them with the kernel, and obtain a single output value. This output value is then stored in the output image at the same `(x, y)`-coordinates as the center of the kernel.
- As the size of the blur kernel increases the image will appear to be more blurred.
- A Gaussian blur is a weighted average of the local pixels and the average blur is not.

## Thresholing
- We use thresholding to focus on objects or areas of particular interest in an image.
- Segmenting the foreground from the background of the image.
- `cv2.threshold` function: a threshold value T must be manually supplied, making simple thresholding challenging in varying lighting conditions.
- `Otsu`'s method assumes there are two peaks in the grayscale histogram of the image. One for the background, another for the foreground.
- Adaptive thresholding allows us to handle cases where there may be dramatic ranges of pixel intensities and the optimal value of T may change for different parts of the image.