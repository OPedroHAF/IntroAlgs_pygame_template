# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
import pygame
import os
pygame.font.init()

TELA_LARGURA = 1280
TELA_ALTURA = 720
FPS = 60

TITULO_JOGO = "Projeto Final - Pygame"

JOGADOR_ALTURA = 100
JOGADOR_LARGURA = 100
JOGADOR_VEL = 6
JOGADOR_VIDAS = 3
JOGADOR_NAVE_IMAGEM = pygame.image.load("assets\imagens\jogador_nave.png")

METEORO_ALTURA = 50
METEORO_LARGURA = 50
METEORO_VEL = 3

PRETO = (0, 0, 0)

FONTE = pygame.font.SysFont("Times New Roman", 22)


