import numpy as np
from pylab import *
from PIL import Image


def multi_seg(img, n):
    new_img = np.zeros((img.shape[0], img.shape[1]))
    size_seg = 255 // n
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            new_img[i, j] = (img[i, j] // size_seg) * size_seg

    return new_img


imgNDG = Image.open('image.jpg').convert('L')
npImg = np.array(imgNDG)
result = Image.fromarray(multi_seg(npImg, 5))
result.convert('RGB').save('multi.jpg')

