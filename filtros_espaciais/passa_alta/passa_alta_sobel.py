import numpy as np
import math

def passa_alta_sobel(img_cinza):
    altura, largura = img_cinza.shape
    img_resultado = np.zeros((altura, largura), dtype=np.uint8)
        
    mascara_x = [
        [-1,  0,  1],
        [-2,  0,  2],
        [-1,  0,  1]
    ]
        
    mascara_y = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]
    
    offset = 1 
        
    for y in range(offset, altura - offset):
        for x in range(offset, largura - offset):
            
            soma_x = 0.0
            soma_y = 0.0
                        
            for my in range(-1, 2):
                for mx in range(-1, 2):
                    pixel = float(img_cinza[y + my, x + mx])
                    
                    peso_x = mascara_x[my + 1][mx + 1]
                    peso_y = mascara_y[my + 1][mx + 1]
                    
                    soma_x += pixel * peso_x
                    soma_y += pixel * peso_y
                                    
            img_resultado[y, x] = min(int(math.sqrt((soma_x ** 2) + (soma_y ** 2))), 255)
            
    return img_resultado