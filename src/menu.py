import pygame
import config

class Button():
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def clicked(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)

class GetName():
    def __init__(self):
        cx = config.SCREEN_WIDTH // 2
        self.btn_confirm = Button(cx - 150, 580, 300, 80, "Confirm")
        self.input_rect = pygame.Rect(cx - 200, 420, 400, 60)
        self.name_input = ""

    def run_loop(self, WIN, time_manager, font_menu):
        run = True
        while run:
            time_manager.update()
            pos_mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.btn_confirm.clicked(pos_mouse) and self.name_input.strip() != "":
                        config.PLAYER_NAME = self.name_input.strip()
                        return True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.name_input = self.name_input[:-1]
                    elif event.key == pygame.K_RETURN and self.name_input.strip() != "":
                        config.PLAYER_NAME = self.name_input.strip()
                        return True
                    else:
                        if len(self.name_input) < 12 and (event.unicode.isalnum() or event.unicode == " "):
                            self.name_input += event.unicode
            
            WIN.fill((5, 5, 40))
            cx = config.SCREEN_WIDTH // 2
            
            txt_pergunta = font_menu.render("QUEM VAI JOGAR?", True, (255, 255, 255))
            WIN.blit(txt_pergunta, txt_pergunta.get_rect(center=(cx, 260)))
            
            pygame.draw.rect(WIN, (20, 20, 20), self.input_rect)
            pygame.draw.rect(WIN, (255, 255, 255), self.input_rect, 2)

            txt_digitado = font_menu.render(self.name_input, True, (255, 255, 255))
            WIN.blit(txt_digitado, (self.input_rect.x + 15, self.input_rect.y + 10))

            pygame.draw.rect(WIN, (0, 150, 75), self.btn_confirm.rect)
            pygame.draw.rect(WIN, (255, 255, 255), self.btn_confirm.rect, 2)
            txt_confirm = font_menu.render(self.btn_confirm.text, True, (255, 255, 255))
            WIN.blit(txt_confirm, txt_confirm.get_rect(center=self.btn_confirm.rect.center))
            
            pygame.display.update()
            
        return False

class Menu():
    def __init__(self):
        cx = config.SCREEN_WIDTH // 2
        self.btn_play = Button(cx - 300, 290, 600, 140, "Play")
        self.btn_skins = Button(cx - 300, 530, 600, 140, "Skins")
        self.btn_config = Button(cx - 300, 770, 600, 140, "Settings")
        self.btn_list = [self.btn_play, self.btn_skins, self.btn_config]

    def run_loop(self, WIN, time_manager, font_menu):
        # Fonte ajustada para tamanho 45 para caber perfeitamente nos botões de 600px
        font_btns = pygame.font.Font(config.FONT_PIXEL, 45)
        run = True
        while run:
            time_manager.update()
            pos_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.btn_play.clicked(pos_mouse):
                        return "play"
                    elif self.btn_config.clicked(pos_mouse):
                        return "settings"
                    elif self.btn_skins.clicked(pos_mouse):
                        return "skins"

            WIN.fill((5, 5, 40))
            
            header_rect = pygame.Rect(40, 75, config.SCREEN_WIDTH - 80, 150)
            pygame.draw.rect(WIN, (0, 0, 0), header_rect)
            pygame.draw.rect(WIN, (255, 255, 255), header_rect, 2)
            txt_titulo = font_menu.render("NavPy", True, (255, 255, 255))
            WIN.blit(txt_titulo, txt_titulo.get_rect(center=header_rect.center))
            
            for b in self.btn_list:
                pygame.draw.rect(WIN, (0, 0, 0), b.rect)
                pygame.draw.rect(WIN, (255, 255, 255), b.rect, 2)
                txt_btn = font_btns.render(b.text, True, (255, 255, 255))
                WIN.blit(txt_btn, txt_btn.get_rect(center=b.rect.center))
                
            pygame.display.update()
        return False

class SettingsMenu():
    def __init__(self):
        cx = config.SCREEN_WIDTH // 2
        self.btn_back = Button(cx - 200, 700, 400, 100, "Back")

    def run_loop(self, WIN, time_manager, font_menu):
        font_btns = pygame.font.Font(config.FONT_PIXEL, 45)
        run = True
        while run:
            time_manager.update()
            pos_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.btn_back.clicked(pos_mouse):
                        return "menu"

            WIN.fill((5, 5, 40))
            
            # Título das Configurações
            txt_settings = font_menu.render("SETTINGS", True, (255, 255, 255))
            WIN.blit(txt_settings, txt_settings.get_rect(center=(config.SCREEN_WIDTH // 2, 150)))
            
            # Texto indicando o Volume Atual
            txt_vol = font_btns.render(f"Master Volume: {int(config.MASTER_SOUND * 100)}%", True, (200, 200, 200))
            WIN.blit(txt_vol, txt_vol.get_rect(center=(config.SCREEN_WIDTH // 2, 400)))

            # Botão Voltar
            pygame.draw.rect(WIN, (150, 0, 0), self.btn_back.rect)
            pygame.draw.rect(WIN, (255, 255, 255), self.btn_back.rect, 2)
            txt_back = font_btns.render(self.btn_back.text, True, (255, 255, 255))
            WIN.blit(txt_back, txt_back.get_rect(center=self.btn_back.rect.center))

            pygame.display.update()
        return False