# Importa a biblioteca numpy, que é usada para trabalhar com arrays e matrizes (estruturas de dados).
import numpy as np

# Importa a biblioteca OpenCV (cv2), usada para processamento de imagens.
import cv2

# O comando a seguir carrega uma imagem para o programa. 
# 'cv2.imread' lê o arquivo de imagem no caminho fornecido (que é a localização onde está a imagem no computador).
# O 'r' antes do caminho significa que o Python trata a string como "crua", ou seja, ele ignora caracteres especiais como '\'.
obj_img = cv2.imread(r"C:\Users\milah\Documents\curso_opencv\imgs\cadeira_01.jpg")

# Aqui, a biblioteca matplotlib é importada para exibir a imagem de forma gráfica.
from matplotlib import pyplot as plt
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)

# 'plt.imshow' exibe a imagem carregada na tela.
# Essa função recebe a imagem carregada pelo OpenCV e a mostra em uma janela.
plt.imshow(obj_img)

# 'plt.show()' exibe a janela com a imagem que foi carregada e preparada para visualização.
# Após chamar essa função, a imagem será exibida na tela.
plt.show()
