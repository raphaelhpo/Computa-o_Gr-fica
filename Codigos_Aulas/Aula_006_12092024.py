import numpy as np
import matplotlib.pyplot as plt

#ALGORITMO DE BRESENHAM - Decorar esse conceito para prova
# O algoritmo de Bresenham é uma tecnica amplamente utilizada na computação gráfica ´para desenhar linhas retas em uma grade raterizada
# de píxels. Ele permite traçar linha com precisão, minimizando a necessidade de cálcula e opeções matemáticas complexas.

#Configuraçãos iniciais
largura,altura = 500,500
img = np.zeros((altura,largura,3), dtype=np.uint8)

#ponto inicial e final da linha
x1, y1 = 100,400
x2, y2 = 400,100
#Para prova, saber como definir os pontos.

#Rasterização da linha usando o algoritmo de Bresenham
dx = abs(x2 - x1)
dy = abs(y2 - y1)
sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1
erro = dx - dy

while (x1 != x2 or y1 != y2):
    img[y1,x1,:] = [255,255,255] #define o píxel branco
    #Na prova será necessário saber Aonde mudar a cor e qual será a cor que sairá
    erro2 = 2*erro
    if erro2 > -dy:
        erro2 -= dy
        x1 += sx
    if erro2 < dx:
        erro2 += dx
        y1 += sy
        
# plt.imshow(img)
# plt.show()
    
#Curva de bézier Quadrática
#Configuraçãos iniciais
largura,altura = 500,500
img = np.zeros((altura,largura,3), dtype=np.uint8)

#Pontos de controle
p0 = np.array([100,400])
p1 = np.array([100,100])
p2 = np.array([400,100])
#Na prova será perguntado sobre os pontos e como definir e desenhar

#parâmetro da curva
#Faz 100 pontos diferentes entre 0 e 1
t = np.linspace(0,1,500)

#Função da curva
def curva_bezier_curva_quadratica(p0,p1,p2,t):
    return np.outer((1-t)**2,p0) + np.outer(2*(1-t)*t,p1) + np.outer((t**2),p2)

#pontos da curva
pontos_curva = curva_bezier_curva_quadratica(p0,p1,p2,t)
pontos_curva = pontos_curva.astype(int)

#looping de desenho da curva
for ponto_curva in pontos_curva :
    x,y = ponto_curva
    if 0<= x < largura and 0<= y < altura:
        img[y,x,:] = [255,255,255]

plt.imshow(img)
plt.show()



