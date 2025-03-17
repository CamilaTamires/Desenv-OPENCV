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



def main():
    """
    Esta função carrega, processa e exibe uma imagem.
    """

    # Carrega a imagem do caminho especificado no computador
    obj_img = cv2.imread(r"C:\Users\milah\Documents\curso_opencv\imgs\cachorro_02.jpg")

    # Obtém as dimensões da imagem: altura, largura e número de canais de cor (RGB)
    altura, largura, canais_cor = obj_img.shape

    # Exibe as informações da imagem no terminal
    print("Dimensões da Imagem: " + str(largura) + "x" + str(altura))
    print("Canais de Cor: ", canais_cor)

    # Percorre todos os pixels da imagem para modificar a cor
    for y in range(0, altura):  # Percorre a imagem de cima para baixo (altura)
        for x in range(0, largura):  # Percorre a imagem da esquerda para a direita (largura)
            azul = obj_img.item(y, x, 0)      # Obtém o valor do canal Azul
            verde = obj_img.item(y, x, 1)     # Obtém o valor do canal Verde
            vermelho = obj_img.item(y, x, 2)  # Obtém o valor do canal Vermelho

            # Remove os tons de verde e vermelho, deixando apenas o azul
            obj_img[y, x, 1] = 0  # Define o canal Verde como 0 (remove o verde)
            obj_img[y, x, 2] = 0  # Define o canal Vermelho como 0 (remove o vermelho)


    cv2.imwrite("cachorro_02_modificado.png", obj_img )
    # Exibe a imagem alterada
    ShowImage(obj_img)

# Chama a função principal para executar o código
main() 
