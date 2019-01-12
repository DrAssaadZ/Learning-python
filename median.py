import numpy as np
from PIL import Image
from pylab import *


def filtre(img, ftr):
    new_img = np.zeros((img.shape[0], img.shape[1]))
    halfFTR = ftr.shape[0] // 2

    for i in range(halfFTR, img.shape[0] - halfFTR):
        for j in range(halfFTR, img.shape[1] - halfFTR):
            some = 0
            for u in range(ftr.shape[0]):
                for l in range(ftr.shape[1]):
                    some += img[i - halfFTR + u, j - halfFTR + l] * ftr[u, l]
            new_img[i, j] = some
    return new_img


imgNDG = Image.open('download.jpg').convert('L')
imshow(imgNDG)
show()
npImg = np.array(imgNDG)
fil = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                [0.04, 0.04, 0.04, 0.04, 0.04],
                [0.04, 0.04, 0.04, 0.04, 0.04],
                [0.04, 0.04, 0.04, 0.04, 0.04],
                [0.04, 0.04, 0.04, 0.04, 0.04]])
print(fil)
res = filtre(npImg, fil)

x = Image.fromarray(res)

imshow(x)
show()

x.convert('RGB').save('hello.jpg')