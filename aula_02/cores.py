import cv2
import numpy as np

#criando ndarrays
branco =np.ones(shape = ((500,500,1)))
cinza = 0.3 * branco
preto = np.zeros(shape=(branco.shape))

cv2.imshow("Branco" , branco)
cv2.imshow("Cinza",cinza)
cv2.imshow("Preto",preto)
cv2.waitKey(0)