# 11/29/2023
# I made this snake game because I had some free time (it took me around 8 hours) and I wanted to get better at making dynamic games. I improved my movement, collision, and spawning mechanics skills as well as my UI skills. 
# I think that I now have the skillset required to code minesweeper. 

import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

BLOCK_SIZE = 20
SPEED = 15

BORDER_WIDTH = int(WIDTH * 0.7)
BORDER_HEIGHT = int(HEIGHT * 0.7)
BORDER_X = (WIDTH - BORDER_WIDTH) // 2
BORDER_Y = (HEIGHT - BORDER_HEIGHT) // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 33)

top_score = 0

def your_score(score):
    global top_score
    top_score = max(top_score, score)
    score_text = score_font.render(f"Score: {score}", True, CYAN)
    top_score_text = score_font.render(f"Top Score: {top_score}", True, CYAN)
    screen.blit(score_text, [10, 10])
    screen.blit(top_score_text, [10, 50])

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])
        pygame.draw.rect(screen, DARK_GRAY, [x[0] + 4, x[1] + 4, block_size - 8, block_size - 8])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def draw_border():
    pygame.draw.rect(screen, DARK_GRAY, [BORDER_X - 2, BORDER_Y - 2, BORDER_WIDTH + 4, BORDER_HEIGHT + 4], 4)
    pygame.draw.rect(screen, CYAN, [BORDER_X, BORDER_Y, BORDER_WIDTH, BORDER_HEIGHT], 2)

def gameLoop():
    global top_score
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    direction = "STOP"

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(BORDER_X, BORDER_X + BORDER_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(BORDER_Y, BORDER_Y + BORDER_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    y1_change = BLOCK_SIZE
                    x1_change = 0
                    direction = "DOWN"

        if x1 >= BORDER_X + BORDER_WIDTH or x1 < BORDER_X or y1 >= BORDER_Y + BORDER_HEIGHT or y1 < BORDER_Y:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        draw_border()
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(BORDER_X, BORDER_X + BORDER_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(BORDER_Y, BORDER_Y + BORDER_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

gameLoop()
