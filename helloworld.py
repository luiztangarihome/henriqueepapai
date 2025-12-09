import pygame
import sys

# Inicializa o pygame - marca
pygame.init()

# Tamanho da janela
LARGURA = 800
ALTURA = 600

# Cria a janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Hello Gráfico")

# Cor em RGB
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
RAIO = 100


clock = pygame.time.Clock()

#posicao que a bola esta parada
posicao = 0
direcao = 100
# Pinta o fundo de branco
tela.fill(BRANCO)
print("Iniciando o loop principal...")

while True:
    # Tratamento de eventos (fechar janela, etc.)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Desenha um círculo azul no centro
    pygame.draw.circle(tela, BRANCO, (LARGURA // 2, ALTURA - RAIO - posicao), RAIO)
    
    if (posicao > ALTURA):
        direcao = -100
    if (posicao < 0):
        direcao = 100
    posicao = posicao + direcao
    print(f"posicao " ,posicao)
    print(direcao)
    
        
    pygame.draw.circle(tela, AZUL, (LARGURA // 2, ALTURA - RAIO - posicao), RAIO)

    # Desenha uma linha vermelha
    # pygame.draw.line(tela, VERMELHO, (100, 100), (700, 500), 5)

    # Atualiza a tela
    pygame.display.flip()

    # Limita o loop a 60 FPS
    clock.tick(60)
