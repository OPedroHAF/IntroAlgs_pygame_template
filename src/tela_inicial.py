import pygame
import random

def main():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("assets/sons/musica.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    tela = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("NavPy")

    frame = pygame.time.Clock()
    cor = (6, 1, 51)

    fonte_titulo = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 32)
    fonte_menu   = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 20)
    fonte_volume = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 16)

    estrelas = []
    for i in range(100):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        velocidade = random.randint(1, 5)
        estrelas.append([x, y, velocidade])

    rect_titulo = pygame.Rect(50, 20, 700, 100)
    rect_jogar  = pygame.Rect(250, 150, 300, 100)
    rect_skins  = pygame.Rect(250, 300, 300, 100)
    rect_config = pygame.Rect(250, 450, 300, 100)

    rect_vol_mais   = pygame.Rect(450, 220, 60, 60)
    rect_vol_menos  = pygame.Rect(290, 220, 60, 60)
    rect_voltar     = pygame.Rect(250, 420, 300, 80)

    volume = 0.5
    tela_atual = "menu"

    ativo = True
    acao  = None

    while ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ativo = False

            if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                pos = evento.pos

                if tela_atual == "menu":
                    if rect_jogar.collidepoint(pos):
                        acao  = "jogar"
                        ativo = False
                    elif rect_skins.collidepoint(pos):
                        acao  = "skins"
                        ativo = False
                    elif rect_config.collidepoint(pos):
                        tela_atual = "config"

                elif tela_atual == "config":
                    if rect_vol_mais.collidepoint(pos):
                        volume = min(1.0, volume + 0.1)
                        pygame.mixer.music.set_volume(volume)
                    elif rect_vol_menos.collidepoint(pos):
                        volume = max(0.0, volume - 0.1)
                        pygame.mixer.music.set_volume(volume)
                    elif rect_voltar.collidepoint(pos):
                        tela_atual = "menu"

        frame.tick(60)
        tela.fill(cor)

        for estrela in estrelas:
            estrela[1] += estrela[2]
            if estrela[1] > 600:
                estrela[1] = 0
                estrela[0] = random.randint(0, 800)
            pygame.draw.circle(tela, (255, 255, 255), (estrela[0], estrela[1]), 2)

        if tela_atual == "menu":
            texto_titulo = fonte_titulo.render("NavPy", True, (255, 255, 255))
            texto_jogar  = fonte_menu.render("Jogar", True, (255, 255, 255))
            texto_skins  = fonte_menu.render("Skins", True, (255, 255, 255))
            texto_cfg    = fonte_menu.render("Configurações", True, (255, 255, 255))

            pygame.draw.rect(tela, (0, 0, 0), rect_titulo)
            pygame.draw.rect(tela, (0, 0, 0), rect_jogar)
            pygame.draw.rect(tela, (0, 0, 0), rect_skins)
            pygame.draw.rect(tela, (0, 0, 0), rect_config)

            tela.blit(texto_titulo, texto_titulo.get_rect(center=rect_titulo.center))
            tela.blit(texto_jogar,  texto_jogar.get_rect(center=rect_jogar.center))
            tela.blit(texto_skins,  texto_skins.get_rect(center=rect_skins.center))
            tela.blit(texto_cfg,    texto_cfg.get_rect(center=rect_config.center))

        elif tela_atual == "config":
            titulo_cfg = fonte_menu.render("Configurações", True, (255, 255, 255))
            tela.blit(titulo_cfg, titulo_cfg.get_rect(center=(400, 100)))

            label_vol = fonte_volume.render("Volume", True, (255, 255, 255))
            tela.blit(label_vol, label_vol.get_rect(center=(400, 180)))

            pygame.draw.rect(tela, (40, 40, 120), rect_vol_menos)
            txt_menos = fonte_menu.render("-", True, (255, 255, 255))
            tela.blit(txt_menos, txt_menos.get_rect(center=rect_vol_menos.center))

            barra_fundo = pygame.Rect(370, 235, 60, 30)
            barra_cheia = pygame.Rect(370, 235, int(60 * volume), 30)
            pygame.draw.rect(tela, (80, 80, 80), barra_fundo)
            pygame.draw.rect(tela, (100, 200, 100), barra_cheia)

            porcentagem = fonte_volume.render(f"{int(volume * 100)}%", True, (255, 255, 255))
            tela.blit(porcentagem, porcentagem.get_rect(center=(400, 300)))

            pygame.draw.rect(tela, (40, 40, 120), rect_vol_mais)
            txt_mais = fonte_menu.render("+", True, (255, 255, 255))
            tela.blit(txt_mais, txt_mais.get_rect(center=rect_vol_mais.center))

            pygame.draw.rect(tela, (0, 0, 0), rect_voltar)
            txt_voltar = fonte_menu.render("Voltar", True, (255, 255, 255))
            tela.blit(txt_voltar, txt_voltar.get_rect(center=rect_voltar.center))

        pygame.display.update()

    return acao