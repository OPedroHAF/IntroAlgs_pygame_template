import pygame
import time
import random
from src.config import(
    TELA_LARGURA,
    TELA_ALTURA,
    FPS,
    TITULO_JOGO,
    JOGADOR_ALTURA,
    JOGADOR_LARGURA ,
    JOGADOR_VEL,
    ESTRELA_ALTURA ,
    ESTRELA_LARGURA ,
    ESTRELA_VEL,
    PRETO,
    FONTE
)
from src.funcoes import (
    jogador_movimentacao
)

pygame.font.init()

#utilizando as variáveos de config
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Nave Py")

def desenhar(jogador, tempo_corrido):
    pygame.draw.rect(TELA, (255,255,255), jogador)

    tempo_string = FONTE.render(f"{round(tempo_corrido)}s", 1, "white")
    TELA.blit(tempo_string, (10, 10))

    pygame.display.update()

def main():
    pygame.init()
    run = True

    #contador de tempo de jogo
    tempo_inicio = time.time()
    tempo_corrido = 0

    clock = pygame.time.Clock()
    jogador = pygame.Rect((TELA_LARGURA - JOGADOR_LARGURA) // 2, TELA_ALTURA - JOGADOR_ALTURA * 2, JOGADOR_LARGURA, JOGADOR_ALTURA)
    while run:
        clock.tick(FPS)
        tempo_corrido = time.time() - tempo_inicio
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        teclas = pygame.key.get_pressed()
        jogador_movimentacao(teclas, jogador)

        TELA.fill(PRETO)
        desenhar(jogador, tempo_corrido)

    pygame.quit()

if __name__ == "__main__":
    # Ponto de entrada da aplicação.
    main()