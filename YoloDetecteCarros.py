from ultralytics import YOLO
import cv2

modelo = YOLO('yolo11n.pt')

resultados = modelo("ImagensEstacionamentosPublicos/imagem-destaque-ALTERADO-2-transformed.png")

detections = resultados[0].boxes

img = cv2.imread("ImagensEstacionamentosPublicos/imagem-destaque-ALTERADO-2-transformed.png")

for i, (xyxy, conf, cls) in enumerate(zip(detections.xyxy, detections.conf, detections.cls)):
    print(f"Detecção {i}: Classe={cls}, Confiança={conf:.2f}, Coordenadas={xyxy}")  # Depuração

    if cls == 67 and conf > 0.10:  # Classe 2 corresponde a "carro" no modelo COCO e confiança superior a 40%
        x1, y1, x2, y2 = xyxy  # Coordenadas da caixa delimitadora

        print(f"Desenhando caixa para carro com confiança {conf:.2f}")  # Depuração
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  # Verde

        label = f"Carro: {conf:.2f}"  # Exibir a confiança
        cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow('Detecção de Carros', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

