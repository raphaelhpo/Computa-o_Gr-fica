#opencv
import cv2 as cv
import numpy as np
#%matplotlib inline
from matplotlib import pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

image = cv.imread('Codigos_Aulas/Fundo_Jogo.jpg')

print(image.size)
print(image.shape)
print(image.dtype)

#plt.imshow(image)
cv.imshow('image', image)
cv.waitKey(0)

b, g, r = cv.split(image)
#plt.imshow(g)
cv.imshow('image', g)
cv.waitKey(0)

image_rgb = cv.merge([r,g,b])
#plt.imshow(image_rgb)
cv.imshow('image', image_rgb)
cv.waitKey(0)

uni = image_rgb[150:260,0:220] #altura x largura
#plt.imshow(olho)
cv.imshow('image', uni)
cv.waitKey(0)

image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
univ_hsv = image_hsv[0:120, 0:170,1]
#plt.imshow(olho, cmap="gray")
cv.imshow('image', univ_hsv)
cv.waitKey(0)