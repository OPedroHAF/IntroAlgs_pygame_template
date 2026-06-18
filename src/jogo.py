import pygame
import time
import random
from src.tela_final import menu_game_over
from src.tela_inicial import main as tela_inicial
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
def desenhar(jogador, tempo_corrido, vidas, meteoros, tiros, onda_idx, onda_elapsed):
    global frame_atual
    TELA.fill(PRETO)
    TELA.blit(JOGADOR_NAVE, (jogador.x, jogador.y))

    tempo_string = FONTE.render(f"{round(tempo_corrido)}s", 1, "white")
    TELA.blit(tempo_string, (10, TELA_ALTURA - tempo_string.get_height() - 10))

    vidas_string = FONTE.render(f"Vidas: {vidas}", 1, "white")
    TELA.blit(vidas_string, (10, 10))
    
    if onda_elapsed <= 3.0:
        progresso = min(onda_elapsed, 3.0) / 3.0
        opacidade = int(255 * (1.0 - progresso))
        onda_string = FONTE.render(f"HORDA {onda_idx + 1}", True, (255, 255, 255))

        onda_rect = onda_string.get_rect(center=(TELA_LARGURA // 2, 40))

        TELA.blit(onda_string, onda_rect)

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
def executar_jogo():
    run = True
    estado = "jogo"
    game_over_inicio = 0
    tempo_inicio = time.time()
    tempo_corrido = 0
    clock = pygame.time.Clock()
    jogador = pygame.Rect((TELA_LARGURA - JOGADOR_LARGURA) // 2, TELA_ALTURA - JOGADOR_ALTURA * 2, JOGADOR_LARGURA, JOGADOR_ALTURA)
    vidas = JOGADOR_VIDAS

    ondas = [2000, 1600, 1200, 800, 400]
    onda_idx = 0
    onda_duracao = 25

    meteoro_add = ondas[onda_idx]
    meteoro_contador = 0
    meteoros = []
    onda_inicio = time.time()
    onda_elapsed = 0
    tiros = []

    while run:
        clock_delta = clock.tick(FPS)

        tempo_corrido = time.time() - tempo_inicio
        meteoro_contador += clock_delta
        hit = False

        # Atualiza quanto tempo passou desde o início da onda atual
        onda_elapsed = time.time() - onda_inicio

        if meteoro_contador > meteoro_add:
            meteoro = gerar_meteoro(meteoros)
            meteoros.append(meteoro)
            meteoro_contador = 0

        if tempo_corrido >= (onda_idx + 1) * onda_duracao and onda_idx < len(ondas) - 1:
            onda_idx += 1
            meteoro_add = ondas[onda_idx]
            onda_inicio = time.time()

        # ÁREA DE EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if estado == "jogo":
                    if event.key == pygame.K_z:
                        atirar(jogador, tiros)

                elif estado == "menu_game_over":
                    if event.key == pygame.K_1:
                        tela_inicial()
                    elif event.key == pygame.K_2:
                        run = False

        # MOVIMENTAÇÃO
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

        tiros_movimentacao(tiros, meteoros)

        if hit:
            vidas -= 1
            if vidas <= 0 and estado == "jogo":
                estado = "game_over"
                game_over_inicio = pygame.time.get_ticks()

        # RENDERIZAÇÃO (fora do for event, executada uma vez por tick)
        if estado == "jogo":
            desenhar(jogador, tempo_corrido, vidas, meteoros, tiros, onda_idx, onda_elapsed)

        elif estado == "game_over":
            game_over()
            tempo_passado = pygame.time.get_ticks() - game_over_inicio
            if tempo_passado > 3000:
                estado = "menu_game_over"

        elif estado == "menu_game_over":
           menu_game_over(TELA)

    pygame.quit()
if __name__ == "__main__":
# Ponto de entrada da aplicação.
  executar_jogo()