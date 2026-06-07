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
    JOGADOR_VIDAS,
    METEORO_ALTURA ,
    METEORO_LARGURA ,
    METEORO_VEL,
    PRETO,
    FONTE,
    JOGADOR_NAVE_IMAGEM
)
from src.funcoes import (
    jogador_movimentacao,
    gerar_meteoro,
    game_over,
    atirar,
    tiros_movimentacao
)

pygame.init()
pygame.font.init()
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption(TITULO_JOGO)
JOGADOR_NAVE = pygame.transform.scale(JOGADOR_NAVE_IMAGEM, (JOGADOR_LARGURA,JOGADOR_ALTURA))

#Variaveis para a animação do meteoro---------------------------------------
METEORO_FRAMES =[
    pygame.transform.rotate(pygame.image.load("assets/imagens/FB001.png").convert_alpha(), 270),
    pygame.transform.rotate(pygame.image.load("assets/imagens/FB002.png").convert_alpha(), 270),
    pygame.transform.rotate(pygame.image.load("assets/imagens/FB003.png").convert_alpha(), 270),
    pygame.transform.rotate(pygame.image.load("assets/imagens/FB004.png").convert_alpha(), 270),
    pygame.transform.rotate(pygame.image.load("assets/imagens/FB005.png").convert_alpha(), 270),
]
animacao_vel = 0.2
frame_atual = 0
#----------------------------------------------------------------------------

#Desenhando os elementos na tela---------------------------------------------
def desenhar(jogador, tempo_corrido, vidas, meteoros, tiros):
    global frame_atual
    TELA.fill(PRETO)
    TELA.blit(JOGADOR_NAVE, (jogador.x, jogador.y))

    tempo_string = FONTE.render(f"{round(tempo_corrido)}s", 1, "white")
    TELA.blit(tempo_string, (tempo_string.get_width(), TELA_ALTURA - tempo_string.get_height() - 10))

    vidas_string = FONTE.render(f"{vidas} HP", 1, "white")
    TELA.blit(vidas_string, (TELA_LARGURA - vidas_string.get_width() - 10, TELA_ALTURA - vidas_string.get_height() - 10))

    for tiro in tiros:
        pygame.draw.rect(TELA, "white", tiro)

    for meteoro in meteoros:
        frame_atual += animacao_vel
        if frame_atual >= len(METEORO_FRAMES):
            frame_atual = 0
        frame_ativo = METEORO_FRAMES[int(frame_atual)]
        TELA.blit(frame_ativo,(meteoro.x, meteoro.y))

    pygame.display.update()
#--------------------------------------------------------------------------
def main():
    run = True

    tempo_inicio = time.time()
    tempo_corrido = 0

    clock = pygame.time.Clock()

    jogador = pygame.Rect((TELA_LARGURA - JOGADOR_LARGURA) // 2, TELA_ALTURA - JOGADOR_ALTURA * 2, JOGADOR_LARGURA, JOGADOR_ALTURA)
    vidas = JOGADOR_VIDAS
    
    meteoro_add = 2000
    meteoro_contador = 0
    meteoros = []

    tiros = []
    while run:
        clock_delta = clock.tick(FPS)
        
        tempo_corrido = time.time() - tempo_inicio
        #contador recebe o tempo em milisegundos para cada tick
        meteoro_contador += clock_delta
        hit = False

        if meteoro_contador > meteoro_add:            
            meteoro = gerar_meteoro(meteoros)
            meteoros.append(meteoro)
            meteoro_add = max(200, meteoro_add - 200)
            meteoro_contador = 0

#AREA DOS EVENTO---------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    atirar(jogador, tiros)
#------------------------------------------------------------------------------

#MOVIMENTAÇÃO DO JOGADOR-------------------------------------------------------
        teclas = pygame.key.get_pressed()
        jogador_movimentacao(teclas, jogador)

        for meteoro in meteoros[:]:
            meteoro.y += METEORO_VEL
            if meteoro.y > TELA_ALTURA:
                meteoros.remove(meteoro)
            elif meteoro.colliderect(jogador):
                meteoros.remove(meteoro)
                hit = True
                break
#------------------------------------------------------------------------------
        tiros_movimentacao(tiros, meteoros)

        if hit:
            vidas -= 1
            if vidas <= 0:
                desenhar(jogador, tempo_corrido, vidas, meteoros, tiros)
                game_over()
                run = False
            
        if run:
            desenhar(jogador, tempo_corrido, vidas, meteoros, tiros)
            
    pygame.quit()

if __name__ == "__main__":
    # Ponto de entrada da aplicação.
    main()