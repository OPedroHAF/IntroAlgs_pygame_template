# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
import pygame
pygame.init()
pygame.font.init()

TELA_LARGURA = 800
TELA_ALTURA = 600
FPS = 60

TITULO_JOGO = "Projeto Final - Pygame"

JOGADOR_ALTURA = 100
JOGADOR_LARGURA = 100
JOGADOR_VEL = 6
JOGADOR_VIDAS = 3
JOGADOR_NAVE_IMAGEM = pygame.image.load("assets/imagens/jogador_nave.png")

METEORO_ALTURA = 50
METEORO_LARGURA = 50
METEORO_VEL = 3

TIRO_VEL = 7
TIRO_LARGURA = 5
TIRO_ALTURA = 15

PRETO = (0, 0, 0)

FONTE = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 14)
FONTE_GRANDE = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 22)


