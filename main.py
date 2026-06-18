import pygame
from src.tela_inicial import main as tela_inicial
from src.jogo import main as executar_jogo

def iniciar():
    pygame.init()

    tela = pygame.display.set_mode((800, 600))

    acao = tela_inicial()

    if acao == "jogar":
        executar_jogo()

    pygame.quit()

iniciar()
