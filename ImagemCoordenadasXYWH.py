import cv2

image = cv2.imread("ImagensEstacionamentosPublicos/imagem-destaque-ALTERADO-2-transformed.png")
image_copy = image.copy()

rois = []
while True:
    roi = cv2.selectROI('Selecione a região de interesse', image_copy,
                        fromCenter=False, showCrosshair=True)

    if roi == (0, 0, 0, 0):
        # Se o ROI for (0, 0, 0, 0), significa que o usuário não selecionou nada
        break
    rois.append(roi)

    image_copy = image.copy()
    for r in rois:
        x, y, w, h = r
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #cv2.imshow('Seleção de ROIs', image_copy)

cv2.destroyAllWindows()

for i, roi in enumerate(rois):
    x, y, w, h = roi
    print(f"Vaga {i+1}: x={x}, y={y}, w={w}, h={h}")

with open('Coordenadas_Vagas/Coordenadas_Vagas2.txt', 'w') as file:
    for i, roi in enumerate(rois):
        x, y, w, h = roi
        file.write(f"Vaga {i+1}: x={x}, y={y}, w={w}, h={h}\n")

