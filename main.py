import pygame
import config
from src import entities
from src import functions
from src.time_manager import TimeManager

pygame.init()
WIN = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("NavePy")

#Carregando sprites
functions.load_assets()


def main():
    #Definindo o o tickrate do jogo
    time_manager = TimeManager(config.FPS)
    main_loop = True
    while main_loop:
        #Criando o objeto para player
        player = entities.Player(config.PLAYER_HP, config.PLAYER_SPD, config.PLAYER_STARTING_X, config.PLAYER_STARTING_Y, config.
        PLAYER_WIDTH, config.PLAYER_HEIGHT)

        #Inicializando os meteoros
        meteors = []
        bullets = []

        game_time = 0.0

        meteor_timer = 0.0
        meteor_cooldown = 1.0
        
        second_loop = True
        while second_loop:
            #Calculando o espaço de tempo entre um frame e outro / 1000
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

            meteor_timer += dt
            if meteor_timer >= meteor_cooldown:
                functions.spawn_meteor(meteors)
                meteor_timer = 0.0

            for meteor in meteors:
                meteor.move(dt)

            for bullet in bullets[:]:
                bullet.move(dt)
                if bullet.rect.y < -config.BULLET_HEIGHT:
                    bullets.remove(bullet)

            for meteor in meteors[:]:
                if player.rect.colliderect(meteor.rect):
                    player.take_damage(meteor.damage)
                    meteors.remove(meteor)
                    if player.hp <= 0:
                        reset = functions.game_over(WIN, time_manager)
                        if reset:
                            second_loop = False
                        
            keys = pygame.key.get_pressed()
            player.move(keys, dt)
            functions.draw(WIN, player, time_manager, meteors, bullets, game_time)

    pygame.quit()

if __name__ == "__main__":
    main()