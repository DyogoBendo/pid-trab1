import numpy as np
import math
from utils.normalizacao import normalizar_matriz

def transformacao_logaritmica(img_cinza):
    altura, largura = img_cinza.shape
        
    temp = np.zeros((altura, largura), dtype=np.float32)
    
    for y in range(altura):
        for x in range(largura):                        
            r = float(img_cinza[y, x])                    
            temp[y, x] = math.log(1 + r)
                
    return normalizar_matriz(temp)