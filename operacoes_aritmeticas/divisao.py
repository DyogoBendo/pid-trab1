import numpy as np
from utils.normalizacao import normalizar_matriz

def divisao(img1, img2):
    altura, largura = img1.shape
    temp = np.zeros((altura, largura), dtype=np.float32)
    
    for y in range(altura):
        for x in range(largura):            
            temp[y, x] = float(img1[y, x]) / max(img2[y, x], 1.0)
            
    return normalizar_matriz(temp)