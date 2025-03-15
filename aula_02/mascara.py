import cv2  # Importa a biblioteca OpenCV para manipulação de imagens
import numpy as np  # Importa a biblioteca NumPy para operações com arrays

# Cria uma matriz de zeros (imagem preta) com dimensões 200x200 pixels
# dtype="uint8" indica que os valores vão de 0 a 255 (escala de cinza)
mascara = np.zeros((200, 200), dtype="uint8")

# Desenha um retângulo branco na imagem
# Parâmetros:
# - imagem onde será desenhado (mascara)
# - coordenadas do canto superior esquerdo (50,50)
# - coordenadas do canto inferior direito (150,150)
# - cor branca (255,255,255) -> como a imagem é em escala de cinza, apenas o primeiro valor (255) é usado
# - espessura -1 indica que o retângulo será preenchido
cv2.rectangle(mascara, (50, 50), (150, 150), (255, 255, 255), -1)

# Salva a imagem resultante como "mascara-rectangle.png"
cv2.imwrite("mascara-rectangle.png", mascara)
