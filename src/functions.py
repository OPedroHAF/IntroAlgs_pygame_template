import pygame
import config
from src import entities
import datetime
import os

pygame.font.init()
game_font = pygame.font.Font(config.FONT_PIXEL, 50)
ui_font = pygame.font.Font(config.FONT_PIXEL, 30)

def draw(WIN, player, time_manager, meteors_list, bullets_list, survived_time, wave, wave_transparency):
    WIN.fill((30, 30, 40))

    WIN.blit(player.image, (player.rect.x, player.rect.y))

    text_lives = ui_font.render(f'HP: {player.hp}', True, (255,255,255))
    text_lives_rect = text_lives.get_rect(bottomright=(config.SCREEN_WIDTH - 20, config.SCREEN_HEIGHT - 20))
    WIN.blit(text_lives, text_lives_rect)

    text_score = ui_font.render(f'SCORE: {config.SCORE}', True, (255,255,255))
    WIN.blit(text_score, (20, 20))
    if config.COMBO_RANK is not None:
        rank_colors = {"D": (150, 150, 150), "C": (100, 255, 100), "B": (100, 100, 255), "A": (255, 165, 0), "S": (255, 50, 50)}
        now_color = rank_colors[config.COMBO_RANK]

        text_rank = game_font.render(f'{config.COMBO_RANK}', True, now_color)
        text_rank_rect = text_rank.get_rect(topright=(config.SCREEN_WIDTH - 20, 20))
        WIN.blit(text_rank, text_rank_rect)

        width_bar = int(100 * (config.COMBO_TIMER / config.COMBO_COOLDOWN))
        bar_rect = pygame.Rect(config.SCREEN_WIDTH - 120, 75, width_bar, 8)
        pygame.draw.rect(WIN, now_color, bar_rect)

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

    if wave_transparency > 0:
        text_wave = game_font.render(f'WAVE {wave}', True, (100, 200, 255))
        wave_surface = pygame.Surface(text_wave.get_size(), pygame.SRCALPHA)
        wave_surface.blit(text_wave, (0,0))
        wave_surface.set_alpha(int(wave_transparency))
        wave_rect = wave_surface.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 150))
        WIN.blit(wave_surface, wave_rect)

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
                    config.SCORE = 0
                    config.COMBO_RANK = None
                    config.COMBO_TIMER = 0.0
                    waiting = False
                    return True
        WIN.fill((30, 30, 40))
        WIN.blit(text_game_over, rect_game_over)
        WIN.blit(text_instructions, rect_instructions)
        pygame.display.update()

def game_win(WIN, time_manager):
    win_font = pygame.font.Font(config.FONT_PIXEL, 80)
    small_font = pygame.font.Font(config.FONT_PIXEL, 35)

    ranking = load_ranking()

    text_win = win_font.render("YOU WIN!", True, (255, 255, 255))

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
                    config.SCORE = 0
                    config.COMBO_RANK = None
                    config.COMBO_TIMER = 0.0
                    return True

        WIN.fill((5, 5, 40))

        cx = config.SCREEN_WIDTH // 2

        header_rect = pygame.Rect(40, 50, config.SCREEN_WIDTH - 80, 120)
        pygame.draw.rect(WIN, (0, 0, 0), header_rect)
        pygame.draw.rect(WIN, (255, 255, 255), header_rect, 2)

        WIN.blit(text_win, text_win.get_rect(center=header_rect.center))

        score_text = small_font.render(
            f"SCORE: {config.SCORE}",
            True,
            (255, 255, 255)
        )
        WIN.blit(score_text, score_text.get_rect(center=(cx, 200)))

        rank_box = pygame.Rect(cx - 300, 260, 600, 250)
        pygame.draw.rect(WIN, (0, 0, 0), rank_box)
        pygame.draw.rect(WIN, (255, 255, 255), rank_box, 2)

        title_rank = small_font.render("TOP 3 RANKING", True, (255, 200, 0))
        WIN.blit(title_rank, title_rank.get_rect(center=(cx, 290)))

        y = 340
        for i, (name, score) in enumerate(ranking[:3]):
            color = (255, 255, 255)

            if i == 0:
                color = (255, 215, 0)

            text = small_font.render(
                f"{i+1}. {name} - {score}",
                True,
                color
            )

            WIN.blit(text, text.get_rect(center=(cx, y)))
            y += 50

        btn_rect = pygame.Rect(cx - 250, 560, 500, 80)
        pygame.draw.rect(WIN, (0, 0, 0), btn_rect)
        pygame.draw.rect(WIN, (255, 255, 255), btn_rect, 2)

        instr = small_font.render("R - Restart | Q - Quit", True, (255, 255, 255))
        WIN.blit(instr, instr.get_rect(center=btn_rect.center))

        pygame.display.update()

def save_record(now_score):
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    folder_path = os.path.join(data_folder, "recorde.txt")
    record = 0
    try:
        with open(folder_path, "r") as f:
            record = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        record = 0
    
    if now_score > record:
        with open(folder_path, "w") as f:
            f.write(str(now_score))

def save_ranking(player_name, now_score):
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    folder_path = os.path.join(data_folder, "ranking.txt")

    ranking_lines = []
    
    try:
        with open(folder_path, "r") as f:
            for l in f:
                if ":" in l:
                    name, pts = l.strip().split(":")
                    ranking_lines.append((name, int(pts)))
    except FileNotFoundError:
        pass

    ranking_lines.append((player_name, now_score))

    ranking_lines.sort(key=lambda x: x[1], reverse=True)

    ranking_lines = ranking_lines[:5]

    with open(folder_path, "w") as f:
        for name, pts in ranking_lines:
            f.write(f"{name}:{pts}\n")

def load_ranking():
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    folder_path = os.path.join(data_folder, "ranking.txt")

    ranking_lines = []

    try:
        with open(folder_path, "r") as f:
            for l in f:
                if ":" in l:
                    name, pts = l.strip().split(":")
                    ranking_lines.append((name, int(pts)))
    except FileNotFoundError:
        return []

    ranking_lines.sort(key=lambda x: x[1], reverse=True)
    return ranking_lines
