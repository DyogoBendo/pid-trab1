import numpy as np
def passa_baixa_min(img_cinza, tamanho_mascara=3):
    altura, largura = img_cinza.shape
    img_borrada = np.zeros((altura, largura), dtype=np.uint8)
        
    offset = tamanho_mascara // 2 
        
    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):            
            minimo = 255
            for my in range(-offset, offset + 1):
                for mx in range(-offset, offset + 1):
                    minimo = min(minimo, int(img_cinza[y + my, x + mx]))                                            
            img_borrada[y, x] = minimo            
    return img_borrada
