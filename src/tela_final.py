import pygame
from src.config import TELA_LARGURA, TELA_ALTURA, PRETO, FONTE

def menu_game_over(tela):
    tela.fill(PRETO)

    titulo = FONTE.render("GAME OVER", True, (255,255,255))
    voltar = FONTE.render("1 - MENU PRINCIPAL", True, (255,255,255))
    sair   = FONTE.render("2 - SAIR", True, (255,255,255))

    tela.blit(titulo, titulo.get_rect(center=(TELA_LARGURA//2, 150)))
    tela.blit(voltar, voltar.get_rect(center=(TELA_LARGURA//2, 300)))
    tela.blit(sair,   sair.get_rect(center=(TELA_LARGURA//2, 360)))

    pygame.display.update()