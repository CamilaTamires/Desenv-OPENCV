import numpy as np  # Biblioteca para manipulação de arrays e operações matemáticas
import cv2  # Biblioteca para processamento de imagens
from matplotlib import pyplot as plt  # Biblioteca para exibição de imagens e gráficos

# Caminho absoluto da imagem a ser carregada
img_path = r"C:\Users\milah\Documents\curso_opencv\imgs\sofa_01.jpg"

def showImage(img, title=""):
    # Converte a imagem de BGR (padrão OpenCV) para RGB (padrão Matplotlib)
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)  # Exibe a imagem
    plt.title(title)  # Define o título da imagem, se houver
    plt.show()  # Mostra a imagem na tela

def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    # Verifica se os valores de x e y são válidos
    if x < 1 or y < 1:
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    
    # Cria um grid de subplots com as dimensões especificadas
    fig, axes = plt.subplots(y, x, figsize=(x * 5, y * 5))
    axes = np.array(axes).reshape(y, x)  # Garante que os eixos sejam uma matriz
    
    idx = 0  # Índice para percorrer as imagens
    for i in range(y):
        for j in range(x):
            if idx < len(imgsArray):  # Se houver imagens disponíveis
                imgMPLIB = cv2.cvtColor(imgsArray[idx], cv2.COLOR_BGR2RGB)  # Converte para RGB
                axes[i, j].imshow(imgMPLIB)  # Exibe a imagem no subplot correspondente
                axes[i, j].set_title(titlesArray[idx] if titlesArray else "")  # Define o título se houver
                axes[i, j].axis('off')  # Remove os eixos da imagem
                idx += 1  # Passa para a próxima imagem
            else:
                axes[i, j].axis('off')  # Se não houver mais imagens, desativa o eixo
    
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
    plt.show()  # Exibe a grade de imagens

def plotTwoImageVertical():
    # Carrega a imagem original
    imgOriginal = cv2.imread(img_path)
    # Cria uma nova imagem com borda replicada
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 200, 100, 50, 10, cv2.BORDER_REPLICATE)
    
    # Lista com as imagens a serem exibidas
    imgsArray = [imgOriginal, imgReplicate]
    titlesArray = ["Original", "Borda Replicada"]
    # Exibe as imagens em uma grade de 1 coluna e 2 linhas
    showMultipleImageGrid(imgsArray, titlesArray, 1, 2)

def plotSixImages():
    # Carrega a imagem original
    imgOriginal = cv2.imread(img_path)
    # Cria versões da imagem com diferentes tipos de bordas
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
    imgWrap = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_WRAP)
    imgConstant = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=[255, 0, 0])
    
    # Lista com as imagens e títulos correspondentes
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101, imgConstant, imgWrap]
    titlesArray = ["Original", "Borda Replicada", "Borda de Espelho", "Borda de Espelho 2", "Moldura Azul", "Efeito Wrap"]
    # Exibe as imagens em uma grade de 3 colunas e 2 linhas
    showMultipleImageGrid(imgsArray, titlesArray, 3, 2)

def main():
    # Função principal que chama a exibição das imagens
    plotSixImages()

# Garante que o código só seja executado se o script for rodado diretamente
if __name__ == "__main__":
    main()
