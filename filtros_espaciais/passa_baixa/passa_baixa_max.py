import numpy as np
def passa_baixa_max(img_cinza, tamanho_mascara=3):
    altura, largura = img_cinza.shape
    img_borrada = np.zeros((altura, largura), dtype=np.uint8)
        
    offset = tamanho_mascara // 2 
        
    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):            
            maximo = 0
            for my in range(-offset, offset + 1):
                for mx in range(-offset, offset + 1):
                    maximo = max(maximo, int(img_cinza[y + my, x + mx]))                                            
            img_borrada[y, x] = maximo            
    return img_borrada
