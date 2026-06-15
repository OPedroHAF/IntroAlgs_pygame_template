import pygame
from src.tela_inicial import main as tela_inicial
from src.jogo import executar_jogo

def iniciar():
    pygame.init()

    acao = tela_inicial()

    if acao == "jogar":
        executar_jogo()

    pygame.quit()

iniciar()
