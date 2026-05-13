import numpy as np
def limiarizacao(img_cinza, limiar):
    altura, largura = img_cinza.shape
    img_limiar = np.zeros((altura, largura), dtype=np.uint8)
    
    for y in range(altura):
        for x in range(largura):
            if img_cinza[y, x] >= limiar:
                img_limiar[y, x] = 255
            else:
                img_limiar[y, x] = 0
                
    return img_limiar
