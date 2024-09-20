import cv2
import matplotlib.pyplot as plt

# Carrega a imagem original
imagem = cv2.imread("C:/Users/Raphael/Downloads/img_001.jpeg")

# Aplica o filtro de média
imagem_tratada = cv2.medianBlur(imagem, 5)

# Cria um novo array para a imagem combinada
imagem_combinada = cv2.hconcat([imagem, imagem_tratada])

# Exibe a imagem combinada
plt.imshow(cv2.cvtColor(imagem_combinada, cv2.COLOR_BGR2RGB))
plt.title('Imagem original e tratada')
plt.xticks([])
plt.yticks([])
plt.show()

# Carrega a imagem original
imagem = cv2.imread("C:/Users/Raphael/Downloads/img_002.jpeg")

# Aplica o filtro de média
imagem_tratada = cv2.medianBlur(imagem, 5)

# Cria um novo array para a imagem combinada
imagem_combinada = cv2.hconcat([imagem, imagem_tratada])

# Exibe a imagem combinada
plt.imshow(cv2.cvtColor(imagem_combinada, cv2.COLOR_BGR2RGB))
plt.title('Imagem original e tratada')
plt.xticks([])
plt.yticks([])
plt.show()

# Carrega a imagem original
imagem = cv2.imread("C:/Users/Raphael/Downloads/img_003.jpeg")

# Aplica o filtro de média
imagem_tratada = cv2.medianBlur(imagem, 5)

# Cria um novo array para a imagem combinada
imagem_combinada = cv2.hconcat([imagem, imagem_tratada])

# Exibe a imagem combinada
plt.imshow(cv2.cvtColor(imagem_combinada, cv2.COLOR_BGR2RGB))
plt.title('Imagem original e tratada')
plt.xticks([])
plt.yticks([])
plt.show()