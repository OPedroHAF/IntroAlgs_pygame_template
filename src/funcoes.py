import pygame
import random
import time
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
    TELA,
    FONTE,
    TIRO_ALTURA,
    TIRO_LARGURA,
    TIRO_VEL
)

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
    if teclas[pygame.K_d] and jogador.x + JOGADOR_VEL <= TELA_LARGURA - JOGADOR_LARGURA:
        jogador.x += JOGADOR_VEL
    if teclas[pygame.K_a] and jogador.x - JOGADOR_VEL >= 0:
        jogador.x -= JOGADOR_VEL

def tiros_movimentacao(tiros, meteoros):
    for tiro in tiros[:]:
        tiro.y -= TIRO_VEL

        if tiro.y < 0:
            tiros.remove(tiro)
            continue
        
        for meteoro in meteoros:
            if tiro.colliderect(meteoro):
                meteoros.remove(meteoro)
                if tiro in tiros:
                    tiros.remove(tiro)
                break


def atirar(jogador, tiros):
    tiro_x = jogador.x + (JOGADOR_LARGURA // 2) - (TIRO_LARGURA // 2)
    tiro_y = jogador.y
    novo_tiro = pygame.Rect(tiro_x, tiro_y, TIRO_LARGURA, TIRO_ALTURA)
    tiros.append(novo_tiro)

def game_over():
    TELA.fill(PRETO)

    gameover_string = FONTE.render("GAME OVER", True, (255, 255, 255))

    gameover_rect = gameover_string.get_rect(
        center=(TELA_LARGURA // 2, TELA_ALTURA // 2)
    )

    TELA.blit(gameover_string, gameover_rect)
    pygame.display.update()
    
def calcular_pontos(pontos_atuais, pontos_ganhos):
    return pontos_atuais + pontos_ganhos

def jogador_perdeu(vidas):
    return vidas <= 0

def limitar_valor(valor, minimo, maximo):
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor

    