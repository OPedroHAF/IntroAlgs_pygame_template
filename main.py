import pygame
import config
from src import entities
from src import functions
from src.time_manager import TimeManager
from src.menu import GetName, Menu, SettingsMenu
import os

pygame.init()
WIN = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("NavePy")

# Carregando sprites
functions.load_assets()

def main():
    # Definindo o o tickrate do jogo
    time_manager = TimeManager(config.FPS)
    font_menu = pygame.font.Font(config.FONT_PIXEL, 60)

    state = "MENU"
    main_menu = Menu()
    settings_menu = SettingsMenu()
    screen_name = GetName()

    while state != "GAMEPLAY":
        if state == "MENU":
            escolha = main_menu.run_loop(WIN, time_manager, font_menu)
            if escolha == "play":
                state = "GET_NAME"
            elif escolha == "settings":
                state = "SETTINGS"
            else:
                pygame.quit()
                exit()

        elif state == "SETTINGS":
            retorno = settings_menu.run_loop(WIN, time_manager, font_menu)
            if retorno == "menu":
                state = "MENU"

        elif state == "GET_NAME":
            if screen_name.run_loop(WIN, time_manager, font_menu):
                state = "GAMEPLAY"
            else:
                state = "MENU" 

    main_loop = True
    while main_loop:
        # Criando o objeto para player
        player = entities.Player(config.PLAYER_HP, config.PLAYER_SPD, config.PLAYER_STARTING_X, config.PLAYER_STARTING_Y, config.PLAYER_WIDTH, config.PLAYER_HEIGHT)

        # Inicializando os meteoros
        meteors = []
        bullets = []

        game_time = 0.0

        wave = 1
        wave_timer = 0.0
        wave_transparency = 0.0
        fade_state = "fade_in"
        fade_speed = 250.0
        display_timer = 0.0
        display_duration = 2.0

        meteor_timer = 0.0
        meteor_cooldown = 1.2
        
        second_loop = True
        while second_loop:
            # Calculando o espaço de tempo entre um frame e outro / 1000
            dt = time_manager.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    second_loop = False
                    main_loop = False
                    break
                functions.shoot(event, bullets, player, time_manager)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        time_manager.toggle_pause()

            game_time += dt
            wave_timer += dt
            
            if config.COMBO_RANK is not None and not time_manager.paused:
                config.COMBO_TIMER -= dt
                if config.COMBO_TIMER <= 0:
                    config.COMBO_RANK = None

            if wave_timer >= 25.0:
                wave += 1
                wave_timer = 0.0
                wave_transparency = 0.0
                fade_state = "fade_in"
                display_timer = 0.0

                if wave == 2:
                    meteor_cooldown = 0.9
                if wave == 3:
                    meteor_cooldown = 0.6
                if wave == 4:
                    meteor_cooldown = 0.3
                if wave == 5:
                    meteor_cooldown = 1.5
            
            if not time_manager.paused:
                if fade_state == "fade_in":
                    wave_transparency += fade_speed * dt
                    if wave_transparency >= 255.0:
                        wave_transparency = 255.0
                        fade_state = "display"
                elif fade_state == "display":
                    display_timer += dt
                    if display_timer >= display_duration:
                        fade_state = "fade_out"
                elif fade_state == "fade_out":
                    wave_transparency -= fade_speed * dt
                    if wave_transparency <= 0.0:
                        fade_state = "done"

            meteor_timer += dt
            if meteor_timer >= meteor_cooldown:
                functions.spawn_meteor(meteors, wave)
                meteor_timer = 0.0

            for meteor in meteors:
                meteor.move(dt)

            for bullet in bullets[:]:
                bullet.move(dt)
                if bullet.rect.y < -config.BULLET_HEIGHT:
                    bullets.remove(bullet)

            for bullet in bullets[:]:
                for meteor in meteors[:]:
                    if bullet.rect.colliderect(meteor.rect):
                        if bullet in bullets:
                            bullets.remove(bullet)
                        meteor.take_damage(1)
                        if meteor.hp <= 0:
                            if meteor in meteors:
                                meteors.remove(meteor)
                            
                            pts_values = {None: 5, 
                                          "D": 10, 
                                          "C": 20, 
                                          "B": 40, 
                                          "A": 80, 
                                          "S": 160}
                            config.SCORE += pts_values[config.COMBO_RANK]
                            proximo_rank ={
                                None: "D",
                                "D": "C",
                                "C": "B",
                                "B": "A",
                                "A": "S",
                                "S": "S"
                            }
                            config.COMBO_RANK = proximo_rank[config.COMBO_RANK]
                            config.COMBO_TIMER = config.COMBO_COOLDOWN
                        break

            for meteor in meteors[:]:
                if player.rect.colliderect(meteor.rect):
                    player.take_damage(meteor.damage)
                    meteors.remove(meteor)
                    if player.hp <= 0:
                        functions.save_record(config.SCORE)
                        functions.save_ranking(config.PLAYER_NAME, config.SCORE)
                        reset = functions.game_over(WIN, time_manager)
                        if reset:
                            second_loop = False
                        
            keys = pygame.key.get_pressed()
            player.move(keys, dt)
            functions.draw(WIN, player, time_manager, meteors, bullets, game_time, wave, wave_transparency)

    pygame.quit()

if __name__ == "__main__":
    main()