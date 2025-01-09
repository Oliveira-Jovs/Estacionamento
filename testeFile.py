import cv2
import numpy as np
from ContadorVagasPessoal import pegar_coordenadas

vagas = pegar_coordenadas()
imagem_original = cv2.imread(
    "C:/Users/oliveira/AreaDesenvolvimento/Estacionamento/ImagensEstacionamentosPublicos/"
    "imagem-destaque-ALTERADO-2-transformed.png")
imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

largura, altura = 900, 600
for tamanho_vizinhança in range(3, 66, 2):

    imagem_threshold = cv2.adaptiveThreshold(imagem_cinza,
                                             255,
                                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV,
                                             tamanho_vizinhança,
                                             16)
    imagem_threshold_resized = cv2.resize(imagem_threshold, (largura, altura))

    cv2.imshow(f"Imagem com vizinhança {tamanho_vizinhança}", imagem_threshold_resized)

    cv2.waitKey(1000)

cv2.destroyAllWindows()