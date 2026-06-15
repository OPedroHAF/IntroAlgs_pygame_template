import pygame
import random

def main():
    pygame.init()

    tela = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Iniciando jogo")

    frame = pygame.time.Clock()

    cor = (6, 1, 51)

    fonte_titulo = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 32)
    fonte_menu = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 20)

    texto_titulo = fonte_titulo.render("NavPy", True, (255, 255, 255))
    texto_jogar = fonte_menu.render("Jogar", True, (255, 255, 255))
    texto_skins = fonte_menu.render("Skins", True, (255, 255, 255))
    texto_config = fonte_menu.render("Configurações", True, (255, 255, 255))

    estrelas = []

    for i in range(100):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        velocidade = random.randint(1, 5)

        estrelas.append([x, y, velocidade])

    rect_titulo = pygame.Rect(50, 20, 700, 100)
    rect_jogar = pygame.Rect(250, 150, 300, 100)
    rect_skins = pygame.Rect(250, 300, 300, 100)
    rect_config = pygame.Rect(250, 450, 300, 100)

    titulo_rect = texto_titulo.get_rect(center=rect_titulo.center)
    jogar_rect = texto_jogar.get_rect(center=rect_jogar.center)
    skins_rect = texto_skins.get_rect(center=rect_skins.center)
    config_rect = texto_config.get_rect(center=rect_config.center)

    ativo = True

    while ativo:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ativo = False

        frame.tick(60)

        tela.fill(cor)

        for estrela in estrelas:

            estrela[1] += estrela[2]

            if estrela[1] > 600:
                estrela[1] = 0
                estrela[0] = random.randint(0, 800)

            pygame.draw.circle(
                tela,
                (255, 255, 255),
                (estrela[0], estrela[1]),
                2
            )

        pygame.draw.rect(tela, (0, 0, 0), rect_titulo)
        pygame.draw.rect(tela, (0, 0, 0), rect_jogar)
        pygame.draw.rect(tela, (0, 0, 0), rect_skins)
        pygame.draw.rect(tela, (0, 0, 0), rect_config)

        tela.blit(texto_titulo, titulo_rect)
        tela.blit(texto_jogar, jogar_rect)
        tela.blit(texto_skins, skins_rect)
        tela.blit(texto_config, config_rect)

        pygame.display.update()

    pygame.quit()

main()