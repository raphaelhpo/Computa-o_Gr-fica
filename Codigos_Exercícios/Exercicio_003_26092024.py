import cv2
#import dlib
import matplotlib.pyplot as plt
import pylab as pl
pl.rcParams['figure.figsize'] = (10.0, 8.0)
import seaborn as sns
import numpy as np

imagem = cv2.imread("./Images/Imagem_Pessoas.jpg")
familia = cv2.cvtColor(imagem, cv2.IMREAD_COLOR)
#plt.imshow(familia)
#plt.show()

rosto_mulher = familia[40:148, 170:230]
#plt.imshow(rosto_mulher)
#plt.show()

classificar = cv2.CascadeClassifier('./Classificador/haarcascade_frontalface_default.xml')

familia_pb = cv2.cvtColor(familia, cv2.COLOR_RGB2GRAY)
#plt.imshow(familia_pb)
#plt.show()

faces = classificar.detectMultiScale(familia_pb, scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

#print(len(faces))

for(x,y,l,a) in faces:
    cv2.rectangle(familia,(x,y),(x+l,y+a),(0,255,0),2)

plt.imshow(familia)
plt.show()


imagem = cv2.imread("./Images/Imagem_Pessoas_02.png")
mendigos_pb = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
faces = classificar.detectMultiScale(mendigos_pb, scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for(x,y,l,a) in faces:
    cv2.rectangle(familia,(x,y),(x+l,y+a),(0,255,0),2)

plt.imshow(mendigos_pb)
plt.show()

