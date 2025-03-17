import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImage(img):
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showImageGrid(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y)
        fig.suptitle(titlesArray)
        yId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId].imshow(imgMPLIB)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[xId].imshow(imgMPLIB)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId, xId].set_title(titlesArray[titleId])
            axis[yId, xId].imshow(imgMPLIB)
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1

        fig.tight_layout(pad=0.5)
    plt.show()

def resizeImage(image, scalePercent):
    width = int(image.shape[1] * scalePercent / 100)
    height = int(image.shape[0] * scalePercent / 100)
    image = cv2.resize(image, (width, height))

    return image

def addImageOverlay(background, foreground, translationForegroundW, translationForegroundH):
    backH, backW, _ = background.shape
    foreH, foreW, _ = foreground.shape

    if translationForegroundH + foreH > backH:
        print(f"Erro: sobreposição com altura maior do que a permitida.")
        print(f"Posição final que altura do objeto da frente termina: {translationForegroundH + foreH}")
        print(f"Altura do fundo: {backH}")
        return background

    if translationForegroundW + foreW > backW:
        print(f"Erro: sobreposição com largura maior do que a permitida.")
        print(f"Posição final que largura do objeto da frente termina: {translationForegroundW + foreW}")
        print(f"Largura do fundo: {backW}")
        return background

    # Parte do fundo onde a imagem será adicionada
    crop = background[translationForegroundH : foreH + translationForegroundH, translationForegroundW : foreW + translationForegroundW]

    # Transformamos o foreground em imagem com tons de cinza e criamos uma máscara binária
    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    ret, maskFore = cv2.threshold(foregroundGray, 240, 255, cv2.THRESH_BINARY)

    # Operação binária de AND para aplicar a máscara no fundo e no foreground
    backWithMask = cv2.bitwise_and(crop, crop, mask = maskFore)
    foreWithMask = cv2.bitwise_not(maskFore)
    foreWithMask = cv2.bitwise_and(foreground, foreground, mask = foreWithMask)

    # Composição entre frente e fundo
    combinedImage = cv2.add(foreWithMask, backWithMask)

    # Adiciona a imagem composta no fundo final
    copyImage = background.copy()
    copyImage[translationForegroundH:foreH + translationForegroundH, translationForegroundW:foreW + translationForegroundW] = combinedImage

    return copyImage

def addBlendingEffect(firstImage, secondImage, weight):
    firstImageGray = cv2.cvtColor(firstImage, cv2.COLOR_BGR2GRAY)
    secondImageGray = cv2.cvtColor(secondImage, cv2.COLOR_BGR2GRAY)

    mask = firstImageGray - secondImageGray
    ret, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)

    copyImg = firstImage.copy()
    altura, largura, = mask.shape
    for y in range(0, altura):
        for x in range(0, largura):
            if mask[y, x] == 255:
                blendingPixelBlue = firstImage[y, x, 0] * (1.0 - weight) + secondImage[y, x, 0] * weight
                blendingPixelGreen = firstImage[y, x, 1] * (1.0 - weight) + secondImage[y, x, 1] * weight
                blendingPixelRed = firstImage[y, x, 2] * (1.0 - weight) + secondImage[y, x, 2] * weight

                copyImg[y, x, 0] = blendingPixelBlue
                copyImg[y, x, 1] = blendingPixelGreen
                copyImg[y, x, 2] = blendingPixelRed

    return copyImg

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erro: não foi possível carregar a imagem de {image_path}")
        exit()  # Encerra o programa se a imagem não for carregada corretamente
    return image

def memeGeneratorWithBlending(fala1, imagem1, fala2, imagem2, fundo):
    # Carrega as imagens e verifica se estão corretas
    dogFeliz = load_image(imagem1)
    background = load_image(fundo)
    dogDeCp = load_image(imagem2)

    # Redimensiona as imagens para 250px de largura
    dogFeliz = resizeImage(dogFeliz, 250)
    dogDeCp = resizeImage(dogDeCp, 250)

    # Adiciona a primeira imagem no fundo
    finalImageUmDog = addImageOverlay(background, dogFeliz, 380, 465)

    # Adiciona a segunda imagem sobre a primeira
    finalImageDoisDogs = addImageOverlay(finalImageUmDog, dogDeCp, 930, 460)

    # Aplica o efeito de blending entre as duas imagens
    finalImage = addBlendingEffect(finalImageUmDog, finalImageDoisDogs, 0.4)

    # Adiciona o texto nas imagens
    finalImage = cv2.putText(finalImage, fala1, (210, 420), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 0), 5, cv2.LINE_AA)
    finalImage = cv2.putText(finalImage, fala2, (1030, 1150), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 0), 5, cv2.LINE_AA)

    # Exibe a imagem final na tela
    showImage(finalImage)

    # Salva a imagem final gerada
    cv2.imwrite("memedoguinho.png", finalImage)

# Chamada da função com as novas imagens
memeGeneratorWithBlending('Feliz!', "C:/Users/milah/Documents/curso_opencv/imgs/dog2.jpg", 'Decepcionado', "C:/Users/milah/Documents/curso_opencv/imgs/dog1.jpg", "C:/Users/milah/Documents/curso_opencv/imgs/fundo2.jpg")
