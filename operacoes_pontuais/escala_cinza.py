import numpy as np

def rgb_para_cinza(img_colorida):
    """
    Converte imagem colorida para tons de cinza. 
    Se já for uma imagem em cinza, irá retornar a imagem original
    """
    
    if len(img_colorida.shape) == 2:
        return img_colorida
    
    altura, largura, _ = img_colorida.shape
        
    img_cinza = np.zeros((altura, largura), dtype=np.uint8)
    
    for y in range(altura):
        for x in range(largura):            
            b, g, r = img_colorida[y, x]                        
            cinza = int((r * 0.299) + (g * 0.587) + (b * 0.114))
            img_cinza[y, x] = cinza
            
    return img_cinza