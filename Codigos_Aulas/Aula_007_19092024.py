import cv2 as cv
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize']

imagem = cv.imread('./img_com_ruidos.jpeg')
plt.imshow(imagem)
plt.show()

imagem_tratada = cv.medianBlur(imagem, 5)

plt.subplot(121)
plt.imshow(imagem_tratada)
plt.title('Imagem tratada')
plt.xticks([])
plt.yticks([])

plt.show()