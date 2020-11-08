import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('Desktop/Velen.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imwrite('res.png',res)
