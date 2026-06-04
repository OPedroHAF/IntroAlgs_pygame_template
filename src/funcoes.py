import pygame
import random
from src.config import(
    TELA_LARGURA,
    TELA_ALTURA,
    FPS,
    TITULO_JOGO,
    JOGADOR_ALTURA,
    JOGADOR_LARGURA ,
    JOGADOR_VEL,
    JOGADOR_VIDAS,
    METEORO_ALTURA ,
    METEORO_LARGURA ,
    METEORO_VEL,
    PRETO,
    FONTE
)

TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Nave Py")


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

def gerar_meteoro(meteoros):
    while True:
        meteoro_x = random.randint(0, TELA_LARGURA - METEORO_LARGURA)
        meteoro_y = random.randint(-600, -METEORO_ALTURA)
        novo = pygame.Rect(meteoro_x, meteoro_y, METEORO_LARGURA, METEORO_ALTURA)
        colisao = False

        for m in meteoros:
            if novo.colliderect(m):
                colisao = True
                break
        
        if not colisao:
            return novo