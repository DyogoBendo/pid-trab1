import numpy as np
from .calculo_histograma import calculo_histograma

def equalizacao_histograma(img_cinza):
    altura, largura = img_cinza.shape
    total_pixels = altura * largura    
    histograma = calculo_histograma(img_cinza)
                
    mapa_cores = np.zeros(256, dtype=np.uint8)
    probabilidade_acumulada = 0.0
    
    for i in range(256):        
        probabilidade_atual = histograma[i] / total_pixels                
        probabilidade_acumulada += probabilidade_atual                
        nova_cor = int(np.round(probabilidade_acumulada * 255))                
        mapa_cores[i] = nova_cor
                
    img_resultado = np.zeros((altura, largura), dtype=np.uint8)
    
    for y in range(altura):
        for x in range(largura):                        
            img_resultado[y, x] = mapa_cores[img_cinza[y, x]]
            
    return img_resultado