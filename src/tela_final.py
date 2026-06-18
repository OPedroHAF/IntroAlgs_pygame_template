import pygame
from src.config import *

def menu_game_over():
    TELA.fill(PRETO)

    titulo = FONTE.render("GAME OVER", True, (255,255,255))

    voltar = FONTE.render("1 - MENU PRINCIPAL", True, (255,255,255))

    sair = FONTE.render("2 - SAIR", True, (255,255,255))

    opcoes = FONTE.render("3 - OPCOES", True, (255,255,255))

    TELA.blit(titulo, titulo.get_rect(center=(TELA_LARGURA//2, 150)))

    TELA.blit(voltar, voltar.get_rect(center=(TELA_LARGURA//2, 300)))

    TELA.blit(sair, sair.get_rect(center=(TELA_LARGURA//2, 360)))

    TELA.blit(opcoes, opcoes.get_rect(center=(TELA_LARGURA//2, 420)))

    pygame.display.update()
