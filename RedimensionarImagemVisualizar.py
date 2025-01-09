import cv2
import numpy as np
from ContadorVagasPessoal import pegar_coordenadas

vagas = pegar_coordenadas()
imagem_original = cv2.imread("C:/Users/oliveira/AreaDesenvolvimento/Estacionamento/"
                   "ImagensEstacionamentosPublicos/imagem-destaque-ALTERADO-2-transformed.png")
imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)
imagem_threshold = cv2.adaptiveThreshold(imagem_cinza, 255,
                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
imagem_blur = cv2.medianBlur(imagem_threshold,3)
kernel = np.ones((3,3),np.int8)
imagem_dilatada = cv2.dilate(imagem_blur,kernel)
largura, altura = 900, 600


imagem_dilatada_resized = cv2.resize(imagem_dilatada, (largura, altura))
quantidade_vagas_livre = 0
for x, y, w, h in vagas:
    recorte = imagem_dilatada[y:y+h,x:x+w]
    quantidade_pixel_brancos = cv2.countNonZero(recorte)
    cv2.putText(imagem_original,str(quantidade_pixel_brancos),(x+10,y+h-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2)

    if quantidade_pixel_brancos > 900:
        cv2.rectangle(imagem_original, (x, y), (x + w, y + h), (0, 0, 255), 3)
    else:
        cv2.rectangle(imagem_original, (x, y), (x + w, y + h), (0, 255, 0), 3)
        quantidade_vagas_livre+=1

cv2.rectangle(imagem_original,(90,0),(415,60),(225,0,0),-1)
cv2.putText(imagem_original,f"LIVRE: {quantidade_vagas_livre}/8",(95,45),cv2.FONT_HERSHEY_SIMPLEX,
            1.5,(255,255,255),5)
cv2.imshow("imagem_blur_resized", imagem_original)
#cv2.imshow("imagem_dilatada_resized", imagem_dilatada_resized)
print(quantidade_vagas_livre)
cv2.waitKey()
