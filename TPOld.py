import numpy as np
from PIL import Image
from pylab import *


# between class variance thresholding method that takes 2 arguments ( the total number of pixels and the histogram)
# and returns the optimal threshold value
def between_class_variance_thresholding(px, histo):

    # we need this to calculate the mean
    sum_total = 0
    for i in range(256):
        sum_total += i * histo[i]

    # initialising background class probability and  foreground class probability variables
    proba_background, proba_foreground = 0, 0
    variance_background, variance_foreground = 0, 0

    # initialising background sum , peak (max value) and the threshold value variables
    sum_background = 0
    peak = 0
    threshold = 0

    # checks if the variance is initialised
    calc_Var = False

    # looping through all possible threshold values
    for i in range(256):
        # calculating the background class probability
        proba_background += histo[i]
        if proba_background == 0:
            continue

        # calculating the foreground class probability
        proba_foreground = px - proba_background
        if proba_foreground == 0:
            break

        # we need this to calculate the means
        sum_background += i * histo[i]

        # calculating the means
        mean_background = sum_background / proba_background
        mean_foreground = (sum_total - sum_background) / proba_foreground

        # initialising the foreground variance
        if not calc_Var:
            for j in range(i, 256):
                variance_foreground += ((j - mean_foreground) ** 2) * histo[j]
        else:
            variance_foreground = variance_foreground - ((i - mean_foreground) ** 2) * histo[i]

        # calculating the background variance
        variance_background += ((i - mean_background) ** 2) * histo[i]

        # calculating the between class variance
        BCV = proba_background * proba_foreground * ((mean_background - mean_foreground) ** 2)

        # calculating the within class variance
        WCV = proba_background * (variance_background/proba_background) + proba_foreground * (variance_foreground/proba_foreground)

        # calculating the total variance
        total_variance = BCV + WCV

        # finding the max value
        if total_variance > peak:
            peak = total_variance
            threshold = i
    print(threshold)
    return threshold


# binarisation method that takes one argument (the threshold) then convert the npImg into a binary image
def binarisation(threshold):
    for i in range(npImg.shape[0]):
        for j in range(npImg.shape[1]):
            npImg[i, j] = 0 if npImg[i, j] < threshold else 255


# otsu method that takes 2 arguments (the histogram and the total number of pixels ) then applies the binarisation
# based on the returned threshold from the between class variance thresholding method
def otsu(pixel, histo):
    binarisation(between_class_variance_thresholding(pixel, histo))


'''this is the main code including loading the image (from current directory) calculating its histogram then calling 
the otsu method , result will saved at the same directory '''
# loading the image
imgNDG = Image.open('image.jpg').convert('L')

# converting image to matrix
npImg = np.array(imgNDG)

# calculating the histogram
histogram = np.zeros((256, 1))
for i in range(npImg.shape[0]):
    for j in range(npImg.shape[1]):
        histogram[npImg[i, j]] += 1

# calculating the total number of pixels
nbr_px = npImg.shape[0] * npImg.shape[1]

# calling the otsu method
otsu(nbr_px, histogram)
# saving the resulted image
Image.fromarray(npImg).save('result.jpg')














