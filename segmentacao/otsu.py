import numpy as np
from .limiarizacao import limiarizacao

def segmentacao_otsu(img_cinza):
    altura, largura = img_cinza.shape
    total_pixels = altura * largura
    
    histograma = np.zeros(256, dtype=int)
    for y in range(altura):
        for x in range(largura):
            pixel = img_cinza[y, x]
            histograma[pixel] += 1
            
    soma_total = 0.0
    for i in range(256):
        soma_total += i * histograma[i]
        
    soma_fundo = 0.0
    peso_fundo = 0
    peso_frente = 0
    
    variancia_maxima = 0.0
    limiar_ideal = 0
    
    for t in range(256):
        peso_fundo += histograma[t]
        if peso_fundo == 0:
            continue 
            
        peso_frente = total_pixels - peso_fundo
        if peso_frente == 0:
            break 
            
        soma_fundo += float(t * histograma[t])
        
        media_fundo = soma_fundo / peso_fundo
        media_frente = (soma_total - soma_fundo) / peso_frente
        
        variancia_entre_classes = float(peso_fundo) * float(peso_frente) * ((media_fundo - media_frente) ** 2)
        
        if variancia_entre_classes > variancia_maxima:
            variancia_maxima = variancia_entre_classes
            limiar_ideal = t
    
    return limiarizacao(img_cinza, limiar_ideal)
