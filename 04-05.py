import numpy as np
import cv2 as cv

# Matriz RGB -> YIQ
A = np.array( [[0.299, 0.587, 0.144], [0.5959, -0.2746, -0.3213], [0.2115, -0.5227, 0.3112]] )

def distorcao_de_cor():
    # --- boilerplate code
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()


    A = np.array( [[0.299, 0.587, 0.144], [0.5959, -0.2746, -0.3213], [0.2115, -0.5227, 0.3112]] )
    R_ = np.array( [[1,0,0], [0,1,0], [0,0,1]] )
    R = R_

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break
    # --- fim do boilerplate code

        # A variável image é um np.array com shape=(height, width, colors)
        frame = cv.resize(frame, (800,600), interpolation =cv.INTER_AREA)
        image = np.array(frame).astype(float)
        H, W, C = image.shape
        X = image.reshape(H*W, C).T
        # --- vamos trabalhar nesta parte

        X = R @ X

        X = X.astype(int)

        # --- fim da parte que vamos trabalhar
        image = X.T.reshape(H, W, C).astype(np.uint8)

    # --- mais boilerplate code
        # Agora, mostrar a imagem na tela!
        cv.imshow('Distorcao_de_cor', image)
        
        # Se aperto 'q', encerro o loop
        # # Use esse tipo de estrutura para implementar as outras interações!
        k = cv.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('b'):
            R = np.array( [[1,0,0], [0,0,0], [0,0,0]])
        elif k == ord('g'):
            R = np.array( [[0,0,0], [0,1,0], [0,0,0]])
        elif k == ord('r'):
            R = np.array( [[0,0,0], [0,0,0], [0,0,1]])
        elif k == ord('y'):
            R = np.array( [[1,0,0], [0,1,0], [0,0,0]])
        elif k == ord('w'):
            r = np.array( [[1,0,0], [0,0,0], [0,0,0]] )
            R = np.linalg.inv(A) @ r @ A
        elif k == ord('p'):
            r = np.array( [[1,0,0], [0.25,0,0.75], [0.75,0.25,0]] )
            R = np.linalg.inv(A) @ r @ A
        elif k == ord('e'):
            r = np.array( [[0.15,0,0], [0,1,0], [0,0,1]] )
            R = np.linalg.inv(A) @ r @ A
        elif k == ord('m'):
            r = np.array( [[0.25,0,0], [0,0,1], [0,1,0]] )
            R = np.linalg.inv(A) @ r @ A
        elif k == ord('a'):
            R = R_
            

    cap.release()
    cv.destroyAllWindows()
    # --- fim do boilerplate code - e da função!

distorcao_de_cor()