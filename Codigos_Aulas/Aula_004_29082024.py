import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Cículo
image = np.zeros((400,400,3), dtype='uint8') #Configuração numero de linhas e colunas e tipo de imagem

#Parâmetros do objeto cículo
center = (200,200) #coordenadas do círculo
radius = 100 #raio do círculo
color = (255,0,0) #vermelho

cv2.circle(image, center, radius, color, -1)
#Exibir imagem com matplotlib
#plt.imshow(image)
#plt.axis('off')#remover eixos 'off', adicionar eixos 'on'
plt.show()

#Retângulo
image = np.full((400,400,3),(0,255,0), dtype='uint8') #Configuração numero de linhas e colunas e tipo de imagem

#Definições do objeto retângulo
top_left = (100,100)
bottom_right = (300,200)
color = (0,0,255)

cv2.rectangle(image, top_left, bottom_right, color, 1)

#plt.imshow(image)
#plt.axis('off')
#plt.show()

#Triângulo
image = np.full((400,400,3), (255,100,50), dtype='uint8') #Configuração numero de linhas e colunas e tipo de imagem

#definição do objeto triangulo
vertices = np.array([[100,300], [200,200], [300,300]], np.int32)
vertices = vertices.reshape((-1,1,2))
color = (0,0,255)

#Triângulo Normal sem preenchimento
cv2.polylines(image, [vertices], isClosed=True, color=color)

#plt.imshow(image)
#plt.axis('off')
#plt.show()

#Triângulo Preenchido
cv2.fillPoly(image, [vertices], color)

#plt.imshow(image)
#plt.axis('off')
#plt.show()

#Preenchimento de Imagem com Triângulo
caminho = 'Codigos_Aulas/Fundo_Jogo.jpg'
foto = cv2.imread(caminho)

cv2.fillPoly(foto, [vertices], color)

plt.imshow(foto)
plt.axis('off')
plt.show()
