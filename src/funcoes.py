import pygame
from src.config import(
    TELA_LARGURA,
    TELA_ALTURA,
    FPS,
    TITULO_JOGO,
    JOGADOR_ALTURA,
    JOGADOR_LARGURA ,
    JOGADOR_VEL,
    METEORO_ALTURA ,
    METEORO_LARGURA ,
    METEORO_VEL,
    PRETO
)

def jogador_movimentacao(teclas, jogador):
    if teclas[pygame.K_UP] and jogador.y - JOGADOR_VEL >= 0:
        jogador.y -= JOGADOR_VEL
    if teclas[pygame.K_DOWN] and jogador.y + JOGADOR_VEL <= TELA_ALTURA - JOGADOR_ALTURA:
        jogador.y += JOGADOR_VEL
    if teclas[pygame.K_RIGHT] and jogador.x + JOGADOR_VEL <= TELA_LARGURA - JOGADOR_LARGURA:
        jogador.x += JOGADOR_VEL
    if teclas[pygame.K_LEFT] and jogador.x - JOGADOR_VEL >= 0:
        jogador.x -= JOGADOR_VEL
    if teclas[pygame.K_w] and jogador.y - JOGADOR_VEL >= 0:
        jogador.y -= JOGADOR_VEL
    if teclas[pygame.K_s] and jogador.y + JOGADOR_VEL <= TELA_ALTURA - JOGADOR_ALTURA:
        jogador.y += JOGADOR_VEL
    if teclas[pygame.K_d] and jogador.x + JOGADOR_VEL < TELA_LARGURA - JOGADOR_LARGURA:
        jogador.x += JOGADOR_VEL
    if teclas[pygame.K_a] and jogador.x - JOGADOR_VEL > 0:
        jogador.x -= JOGADOR_VEL