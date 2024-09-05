#Iluminação Básica
import numpy as np
import matplotlib.pyplot as plt

largura,altura = 500,500
img = np.zeros((altura,largura,3),dtype=np.uint8)

intensidade = 0
img[:,:,:] = intensidade

plt.imshow(img)
plt.axis('off')
plt.title('Iluminação Básica')
plt.show()

#simulação física da luz
largura, altura = 200,200
img = np.zeros((altura,largura,3),dtype=np.uint8)

intensidade_2 = 255
for y in range(altura):
    intensidade_2 = int(255 *(y/altura))
    img[y,:,:] = [intensidade_2,intensidade_2,intensidade_2]

plt.imshow(img)
plt.axis('off')
plt.title('Iluminação Básica - Degrade')
plt.show()

#luz,sombra e fundo
largura, altura = 200,200
img = np.zeros((altura,largura,3),dtype=np.uint8)

for y in range(altura):
    vermelho = int(255 *(y/altura))
    verde = int(255 *-(altura-y)/altura)
    azul = 128
    img[y,:,:] = [vermelho,azul,azul]

plt.imshow(img)
plt.axis('off')
plt.title('Iluminação Básica - Degrade + cores')
plt.show()

#interpolação Linear
largura, altura = 200,200
img = np.zeros((altura,largura,3),dtype=np.uint8)
cor_1 = [255,0,0]
cor_2 = [100,0,255]

for x in range(largura):
    t = x/largura
    cor_interpolada = (1-t)*np.array(cor_1) + t*np.array(cor_2)
    img[:,x,:] = cor_interpolada.astype(np.uint8)

plt.imshow(img)
plt.axis('off')
plt.title('Iluminação Básica - Interpolação Linear')
plt.show()

#interpolação bILinear
largura, altura = 200,200
img = np.zeros((altura,largura,3),dtype=np.uint8)

cor_sup_esquerda = [255,0,0]
cor_sup_direita = [0,255,0]
cor_inf_esquerda = [0,0,255]
cor_inf_direita = [255,255,0]

for y in range(altura):
    for x in range(largura):
        tx = x/(largura-1)
        ty = y/(altura -1)
        
        cor_superior = (1-tx)*np.array(cor_sup_esquerda) + tx*np.array(cor_sup_direita)
        cor_inferior = (1-tx)*np.array(cor_inf_esquerda) + tx*np.array(cor_inf_direita)
        cor_interpolada = (1-ty)*np.array(cor_superior) + ty*np.array(cor_inferior)
        
        img[y,x,:] = cor_interpolada.astype(np.uint8)
    
plt.imshow(img)
plt.axis('off')
plt.title('Iluminação Básica - Interpolação BILinear')
plt.show()