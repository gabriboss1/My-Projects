# 5/1/2024
# This is a game for those who don't have friends to play with. I developed an artificial intelligence system against which players can play. I still haven't been able to win against it.
# I'm very proud of this implementation of AI, and I am sure that it will be used and ameliorated in my future projects.


import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

BALL_SIZE = 15

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

left_paddle_y = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2)
right_paddle_y = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2)

paddle_speed = 7

ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 4 
ball_dy = 4  

speed_multiplier = 1.0
speed_increment = 0.01 

left_score = 0
right_score = 0

font = pygame.font.Font(None, 74)

ai_speed = 7
reaction_buffer = 15

def draw_paddles_and_ball():
    pygame.draw.rect(screen, WHITE, (10, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 20, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

def draw_scores():
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 10))
    screen.blit(right_text, (SCREEN_WIDTH * 3 // 4, 10))

def ai_move():
    global right_paddle_y
    if ball_dx > 0:
        if ball_y > right_paddle_y + PADDLE_HEIGHT // 2 + reaction_buffer and right_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            right_paddle_y += ai_speed
        elif ball_y < right_paddle_y + PADDLE_HEIGHT // 2 - reaction_buffer and right_paddle_y > 0:
            right_paddle_y -= ai_speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and left_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += paddle_speed

    ai_move()

    ball_x += ball_dx * speed_multiplier
    ball_y += ball_dy * speed_multiplier

    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_dy = -ball_dy

    if (ball_x <= 20 and left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT) or \
       (ball_x >= SCREEN_WIDTH - 20 - BALL_SIZE and right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT):
        ball_dx = -ball_dx
        speed_multiplier += speed_increment

    if ball_x <= 0:
        right_score += 1
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_dx = 4
        ball_dy = 4
        speed_multiplier = 1.0

    if ball_x >= SCREEN_WIDTH - BALL_SIZE:
        left_score += 1
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_dx = -4
        ball_dy = 4
        speed_multiplier = 1.0

    screen.fill(BLACK)

    draw_paddles_and_ball()
    draw_scores()

    pygame.display.flip()

    clock.tick(60)
