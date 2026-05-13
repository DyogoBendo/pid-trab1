import numpy as np
import math

def passa_alta_roberts(img_cinza):
    altura, largura = img_cinza.shape
    img_resultado = np.zeros((altura, largura), dtype=np.uint8)
        
    mascara_x = [
        [ 1,  0],
        [ 0, -1]
    ]
        
    mascara_y = [
        [ 0,  1],
        [-1,  0]
    ]
        
    for y in range(0, altura - 1):
        for x in range(0, largura - 1):
            
            soma_x = 0.0
            soma_y = 0.0
                        
            for my in range(2):
                for mx in range(2):
                    pixel = float(img_cinza[y + my, x + mx])
                    
                    peso_x = mascara_x[my][mx]
                    peso_y = mascara_y[my][mx]
                    
                    soma_x += pixel * peso_x
                    soma_y += pixel * peso_y
                                            
            img_resultado[y, x] = min(int(math.sqrt((soma_x ** 2) + (soma_y ** 2))), 255)
            
    return img_resultado