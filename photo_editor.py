from PIL import Image, ImageEnhance, ImageFilter
import requests
from io import BytesIO

def baixar_imagem(url):
    """Baixa uma imagem a partir de uma URL."""
    response = requests.get(url)
    response.raise_for_status()  # Levanta um erro se o download falhar
    return Image.open(BytesIO(response.content))

def salvar_imagem(imagem, caminho):
    """Salva a imagem no caminho especificado."""
    imagem.save(caminho)

def ajustar_brilho(imagem, fator):
    """Ajusta o brilho da imagem."""
    enhancer = ImageEnhance.Brightness(imagem)
    return enhancer.enhance(fator)

def ajustar_contraste(imagem, fator):
    """Ajusta o contraste da imagem."""
    enhancer = ImageEnhance.Contrast(imagem)
    return enhancer.enhance(fator)

def redimensionar_imagem(imagem, largura, altura):
    """Redimensiona a imagem para a largura e altura especificadas."""
    return imagem.resize((largura, altura))

def aplicar_filtro(imagem, filtro):
    """Aplica um filtro na imagem."""
    return imagem.filter(filtro)

def main():
    url_imagem = input("Digite a URL da imagem que você deseja editar: ")
    
    try:
        imagem = baixar_imagem(url_imagem)
    except Exception as e:
        print(f"Erro ao baixar a imagem: {e}")
        return
    
    # Exemplo de manipulação
    imagem_brilho = ajustar_brilho(imagem, 1.5)  # Aumentar brilho
    imagem_contraste = ajustar_contraste(imagem, 1.5)  # Aumentar contraste
    imagem_redimensionada = redimensionar_imagem(imagem, 800, 600)  # Redimensionar
    imagem_filtro = aplicar_filtro(imagem, ImageFilter.BLUR)  # Aplicar filtro de desfoque

    # Salvar as imagens manipuladas
    salvar_imagem(imagem_brilho, 'imagem_brilho.jpg')
    salvar_imagem(imagem_contraste, 'imagem_contraste.jpg')
    salvar_imagem(imagem_redimensionada, 'imagem_redimensionada.jpg')
    salvar_imagem(imagem_filtro, 'imagem_filtro.jpg')

    print("Imagens manipuladas salvas com sucesso!")

if __name__ == "__main__":
    main()