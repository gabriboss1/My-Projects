# 3/3/2024
# I am really bad at Flappy Bird, so I decided to make the game myself and code it in my favor, for example by making the falling speed slower and increasing the distance between pipes. 
# That worked pretty well, but here's how it is actually supposed to be. This has given me quite some insight on how to implement gravity in videogames, which will be useful in future projects.


import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0
bird_jump = -6.5
pipe_gap = 150
pipe_speed = 3
score = 0
high_score = 0
font = pygame.font.Font(None, 36)

bird_surface = pygame.Surface((30, 30))
bird_surface.fill(BLUE)
bird_rect = bird_surface.get_rect(center=(100, SCREEN_HEIGHT // 2))

pipe_surface = pygame.Surface((50, SCREEN_HEIGHT))
pipe_surface.fill(GREEN)

def create_pipe():
    pipe_height = random.randint(100, 400)
    bottom_pipe = pipe_surface.get_rect(midtop=(SCREEN_WIDTH + 50, pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom=(SCREEN_WIDTH + 50, pipe_height - pipe_gap))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= pipe_speed
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return False
    return True

def update_score(pipes, score):
    for pipe in pipes:
        if pipe.centerx + pipe.width // 2 == bird_rect.centerx:
            score += 1
    return score

def display_score():
    score_surface = font.render(f"Score: {int(score)}", True, BLACK)
    screen.blit(score_surface, (10, 10))
    high_score_surface = font.render(f"High Score: {int(high_score)}", True, BLACK)
    screen.blit(high_score_surface, (10, 50))

pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

running = True
game_active = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = bird_jump
            if event.key == pygame.K_SPACE and not game_active:
                bird_rect.center = (100, SCREEN_HEIGHT // 2)
                pipes.clear()
                score = 0
                bird_movement = 0
                game_active = True
        if event.type == SPAWNPIPE and game_active:
            pipes.extend(create_pipe())

    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement

        pipes = move_pipes(pipes)
        game_active = check_collision(pipes)
        score = update_score(pipes, score)

    screen.fill(WHITE)
    screen.blit(bird_surface, bird_rect)
    draw_pipes(pipes)

    if not game_active:
        high_score = max(high_score, score)
        game_over_surface = font.render("Game Over! Press SPACE to Restart", True, RED)
        high_score_surface = font.render(f"High Score: {int(high_score)}", True, BLACK)
        screen.blit(game_over_surface, (50, SCREEN_HEIGHT // 2 - 50))
        screen.blit(high_score_surface, (120, SCREEN_HEIGHT // 2))

    display_score()

    pygame.display.flip()

    clock.tick(60)
