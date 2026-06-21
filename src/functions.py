import pygame
import config
from src import entities
import datetime

pygame.font.init()
game_font = pygame.font.Font(None, 70)
ui_font = pygame.font.Font(None, 40)

def draw(WIN, player, time_manager, meteors_list, bullets_list, survived_time):
    WIN.fill((30, 30, 40))

    WIN.blit(player.image, (player.rect.x, player.rect.y))

    text_lives = ui_font.render(f'HP: {player.hp}', True, (255,255,255))
    text_lives_rect = text_lives.get_rect(bottomright=(config.SCREEN_WIDTH - 20, config.SCREEN_HEIGHT - 20))
    WIN.blit(text_lives, text_lives_rect)

    td = datetime.timedelta(seconds=int(survived_time))
    time_string = str(td)
    if len(time_string) == 7:
        time_string = '0' + time_string
    text_time = ui_font.render(f'{time_string}', True, (255,255,255))
    text_time_rect = text_time.get_rect(bottomleft=(20, config.SCREEN_HEIGHT - 20))
    WIN.blit(text_time, text_time_rect)

    for bullet in bullets_list:
        pygame.draw.rect(WIN, (255, 255, 0), bullet.rect)

    for meteor in meteors_list:
        active_image = config.METEOR_FRAMES[meteor.current_frame]
        WIN.blit(active_image, (meteor.rect.x, meteor.rect.y))

    if time_manager.paused:
        text_pause = game_font.render("PAUSED", True, (255, 255, 255))
        text_rect = text_pause.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        WIN.blit(text_pause, text_rect)
    pygame.display.update()

def spawn_meteor(meteor_list, wave):
    if wave >= 5:
        hp_atual = config.METEOR_HP + 2
    else:
        hp_atual = config.METEOR_HP
    new_meteor = entities.Meteor(hp_atual, config.METEOR_SPD, config.METEOR_DAMAGE)
    meteor_list.append(new_meteor)

def shoot(event, bullet_list, player, time_manager):
    if not time_manager.paused and event.type == pygame.KEYDOWN:
        if event.key == pygame.K_z:
            new_bullet = entities.Bullet(config.BULLET_SPD, player.rect.x, player.rect.y, config.BULLET_WIDTH, config.BULLET_HEIGHT)
            bullet_list.append(new_bullet)

def load_assets():
    def load_meteor_frame(path):
        raw = pygame.image.load(path).convert_alpha()
        rotated = pygame.transform.rotate(raw, 270)
        raw_w, raw_h = rotated.get_size()
        scale = config.METEOR_SCALE
        scaled_size = (max(1, int(raw_w * scale)), max(1, int(raw_h * scale)))
        return pygame.transform.smoothscale(rotated, scaled_size)

    config.METEOR_FRAMES = [
        load_meteor_frame("assets/imagens/meteor_frames/FB001.png"),
        load_meteor_frame("assets/imagens/meteor_frames/FB002.png"),
        load_meteor_frame("assets/imagens/meteor_frames/FB003.png"),
        load_meteor_frame("assets/imagens/meteor_frames/FB004.png"),
        load_meteor_frame("assets/imagens/meteor_frames/FB005.png")
    ]

    if config.METEOR_FRAMES:
        config.METEOR_WIDTH, config.METEOR_HEIGHT = config.METEOR_FRAMES[0].get_size()

    raw_player = pygame.image.load(config.PLAYER_IMAGE_PATH).convert_alpha()
    size_player = (config.PLAYER_WIDTH, config.PLAYER_HEIGHT)
    config.PLAYER_IMAGE = pygame.transform.scale(raw_player, size_player)

    

def game_over(WIN, time_manager):
    game_over_font = pygame.font.Font(None, 100)
    instructions_font = pygame.font.Font(None, 40)
    text_game_over = game_over_font.render("GAME OVER", True, (255, 50, 50))
    text_instructions = instructions_font.render("Press 'R' to Restart or 'Q' to Quit", True, (255,255,255))
    rect_game_over = text_game_over.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2 - 50))
    rect_instructions = text_instructions.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 50))

    waiting = True
    while waiting:
        time_manager.clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_r:
                    waiting = False
                    return True
        WIN.fill((30, 30, 40))
        WIN.blit(text_game_over, rect_game_over)
        WIN.blit(text_instructions, rect_instructions)
        pygame.display.update()

