# Importa a biblioteca NumPy, que é usada para manipular arrays (estruturas de dados organizadas em tabelas)
import numpy as np

# Importa a biblioteca OpenCV (cv2), usada para processar imagens e vídeos
import cv2

def ShowImage(img):
    """
    Esta função exibe a imagem usando a biblioteca Matplotlib.
    """
    from matplotlib import pyplot as plt  # Importa a Matplotlib para exibir a imagem

    # Converte a imagem do formato BGR (usado pelo OpenCV) para RGB (usado pelo Matplotlib)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Exibe a imagem na tela
    plt.imshow(img) 
    plt.show()

def getColor(img,x,y):
    """
    Esta função retorna os valores de cor (azul, verde e vermelho) de um pixel na posição (x, y).
    """
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)  # Obtém os valores dos três canais de cor

def setColor(img,x,y, b , g , r):
    """
    Esta função define novos valores de cor para um pixel na posição (x, y).
    """
    img[y, x, 0] = b  # Define o canal Azul como o valor fornecido
    img[y, x, 1] = g  # Define o canal Verde como o valor fornecido
    img[y, x, 2] = r  # Define o canal Vermelho como o valor fornecido

    return img  # Retorna a imagem modificada

def main():
    """
    Esta função carrega uma imagem, modifica os pixels e exibe o resultado.
    """

    # Carrega a imagem do caminho especificado
    obj_img = cv2.imread(r"C:\Users\milah\Documents\curso_opencv\imgs\cachorro_02.jpg")

    # Obtém as dimensões da imagem: altura, largura e número de canais de cor
    altura, largura, canais_cor = obj_img.shape

    # Exibe as informações da imagem no terminal
    print("Dimensões da Imagem: " + str(largura) + "x" + str(altura))
    print("Canais de Cor: ", canais_cor)

    # Percorre todos os pixels da imagem para modificar as cores
    for y in range(0, altura):  # Percorre cada linha da imagem (altura)
        for x in range(0, largura):  # Percorre cada coluna da imagem (largura)
            azul, verde, vermelho = getColor(obj_img, x, y)  # Obtém os valores originais do pixel
            obj_img = setColor(obj_img, x, y, 0, 0, vermelho)  # Remove os canais azul e verde, mantendo o vermelho

    # Recorta uma região da imagem correspondente à coleira do cachorro
    # O corte é feito a partir da posição (312, 342) com uma largura e altura de 80 pixels
    corte_img = obj_img[312: 312 + 80, 342: 342 + 80]

    # Exibe a região recortada da imagem
    ShowImage(corte_img)

    # Cola a região recortada em uma nova posição dentro da imagem original
    # A nova posição é (397, 521), garantindo que o recorte não ultrapasse os limites da imagem
    obj_img[397: 397 + corte_img.shape[0], 521: 521 + corte_img.shape[1]] = corte_img

    # Exibe a imagem final com a região copiada e colada
    ShowImage(obj_img)

# Chama a função principal para executar o código
main()
