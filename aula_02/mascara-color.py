import cv2
import numpy as np

# Criar uma máscara em escala de cinza
mascara = np.zeros((200, 200), dtype="uint8")

# Criar uma imagem colorida a partir da máscara
mascara_colorida = cv2.merge([mascara, mascara, mascara])

# Desenhar um círculo vermelho (BGR: (0, 0, 255))
cv2.circle(mascara_colorida, (100, 100), 50, (0, 0, 255), -1)

# Salvar a imagem
cv2.imwrite("mascara-circle.png", mascara_colorida)