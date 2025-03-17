# Importa a biblioteca NumPy, que é usada para manipular arrays (estruturas de dados organizadas em tabelas)
import numpy as np

# Importa a biblioteca OpenCV (cv2), usada para processar imagens e vídeos
import cv2

from matplotlib import pyplot as plt

def showMultipleImageGrid(imgsArray,titlesArray,x ,y):
    if ( x < 1 or y < 1):
        print("Erro: X OU Y não poder ser igual ou menor zero")
        return 
    elif(x == 1 and y == 1):
        showImageGrid(imgsArray, titlesArray)
    elif(x == 1):  # Se x for 1, cria uma coluna de imagens
        fig, axis = plt.subplots(y)
        fig.suptitle(titlesArray)
        axisId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[axisId].imshow(imgMPLIB)
            axisId += 1
    elif(y == 1):  # Se y for 1, cria uma linha de imagens
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[xId].imshow(imgMPLIB)
            xId += 1
    else:  # Para uma grid de imagens com x e y especificados
        fig, axis = plt.subplots(y, x)
        xId, vId = 0, 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[vId, xId].imshow(imgMPLIB)
            axis[vId, xId].set_title(titlesArray)
            xId += 1
            if xId == x:  # Move para a próxima linha
                xId = 0
                vId += 1
    plt.show()  # Mostra a grid final com as imagens

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotTwoImageHorizontal(img, title):
    # Carrega a imagem original
    img_original = cv2.imread(r"C:\Users\milah\Documents\curso_opencv\imgs\sofa_01.jpg")
    # Cria uma borda replicada na imagem
    img_Replicate = cv2.copyMakeBorder(img_original, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

    # Criando um grid com as duas imagens
    imgsArray = [img_original, img_Replicate]
    title = "Imagem original e imagem com borda replicada"
    showMultipleImageGrid(imgsArray, title, 2, 1)

def main():
    plotTwoImageHorizontal(None, "")  # Chama a função para exibir as imagens

if __name__ == "__main__":
    main()
