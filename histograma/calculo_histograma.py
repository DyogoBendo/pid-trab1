import numpy as np

def calculo_histograma(img_cinza):
    altura, largura = img_cinza.shape
    histograma = np.zeros(256, dtype=int)
    for y in range(altura):
        for x in range(largura):            
            histograma[img_cinza[y, x]] += 1
    return histograma