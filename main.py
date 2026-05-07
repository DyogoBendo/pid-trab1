from filtros_espaciais.passa_baixa.passa_baixa_media import passa_baixa_media
from utils.arquivo import ler_imagem, salvar_imagem
from operacoes_pontuais.escala_cinza import rgb_para_cinza
from operacoes_pontuais.negativo import negativo
from segmentacao.limiarizacao_simples import threshold

if __name__ == "__main__":
    # Carrega a matriz original
    img_original = ler_imagem("images/cat.jpg")
    
    # 1. Converte para cinza
    print("Convertendo para escala de cinza...")
    img_cinza = rgb_para_cinza(img_original)
    salvar_imagem("images/01_escala_cinza.jpg", img_cinza)
    
    # 2. Aplica o Negativo
    print("Gerando negativo...")
    img_neg = negativo(img_cinza)
    salvar_imagem("images/02_negativo.jpg", img_neg)
    
    # 3. Aplica Limiarização (Binarização com limiar de 127)
    print("Aplicando limiarização...")
    img_thresh = threshold(img_cinza, limiar=127)
    salvar_imagem("images/03_limiar.jpg", img_thresh)
    
    # 4. Aplica Filtro Passa-Baixa (Suavização Média 3x3)
    print("Aplicando filtro passa-baixa (Média)...")
    img_media = passa_baixa_media(img_cinza, tamanho_mascara=3)
    salvar_imagem("images/04_passa_baixa.jpg", img_media)
    
    print("Processamento concluído!")