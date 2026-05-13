import numpy as np
from utils.normalizacao import normalizar_matriz

def passa_alta_alto_reforco(img_cinza, A=1.1, tamanho_mascara=3):    
    altura, largura = img_cinza.shape
    temp = np.zeros((altura, largura), dtype=np.uint8)
    
    offset = tamanho_mascara // 2
        
    area_total = tamanho_mascara * tamanho_mascara    
    mascara = np.full((tamanho_mascara, tamanho_mascara), -1.0)    
    peso_central = (area_total * A) - 1.0
    mascara[offset, offset] = peso_central
        
    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):            
            soma_convolucao = 0.0                    
            for my in range(-offset, offset + 1):
                for mx in range(-offset, offset + 1):
                    pixel = float(img_cinza[y + my, x + mx])                                    
                    peso = mascara[my + offset, mx + offset]                    
                    soma_convolucao += pixel * peso
                                
            temp[y, x] = min(abs(soma_convolucao), 255)
            
    return temp