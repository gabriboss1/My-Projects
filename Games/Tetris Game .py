# 1/12/2024
# Tetris is one of my favorite puzzle video games, so I wanted to recreate it. The scope for this was to make it as efficient as I could and to get better at developing games that strictly function algorithmically.
import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GAME_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GAME_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
FPS = 10 
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255), # Cyan
    (255, 165, 0), # Orange
    (0, 0, 255), # Blue
    (255, 0, 0), # Red
    (0, 255, 0), # Green
    (255, 255, 0), # Yellow
    (128, 0, 128), # Purple
]

SHAPES = [
    [[1, 1, 1, 1]], 
    [[1, 1], [1, 1]],  
    [[0, 1, 0], [1, 1, 1]], 
    [[1, 1, 0], [0, 1, 1]],  
    [[0, 1, 1], [1, 1, 0]],  
    [[1, 0, 0], [1, 1, 1]], 
    [[0, 0, 1], [1, 1, 1]], 
]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

font = pygame.font.SysFont('Arial', 24)

def create_new_piece():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return {'shape': shape, 'color': color, 'x': GAME_WIDTH // 2 - len(shape[0]) // 2, 'y': 0}

def draw_board(board):
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            if board[y][x]:
                pygame.draw.rect(screen, board[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def check_collision(board, piece):
    for y in range(len(piece['shape'])):
        for x in range(len(piece['shape'][y])):
            if piece['shape'][y][x]:
                px = piece['x'] + x
                py = piece['y'] + y
                if px < 0 or px >= GAME_WIDTH or py >= GAME_HEIGHT or (py >= 0 and board[py][px]):
                    return True
    return False

def clear_lines(board):
    full_lines = []
    for y in range(GAME_HEIGHT):
        if all(board[y]):
            full_lines.append(y)
    for y in full_lines:
        del board[y]
        board.insert(0, [None] * GAME_WIDTH)
    return len(full_lines)

def draw_text(text, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def run_game():
    board = [[None] * GAME_WIDTH for _ in range(GAME_HEIGHT)]
    current_piece = create_new_piece()
    score = 0
    best_score = 0
    fall_time = 0 

    clock = pygame.time.Clock()
    game_over = False

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if not game_over:
            if keys[pygame.K_LEFT]:
                current_piece['x'] -= 1
                if check_collision(board, current_piece):
                    current_piece['x'] += 1
            if keys[pygame.K_RIGHT]:
                current_piece['x'] += 1
                if check_collision(board, current_piece):
                    current_piece['x'] -= 1
            if keys[pygame.K_DOWN]:
                current_piece['y'] += 1
                score += 1 
                if check_collision(board, current_piece):
                    current_piece['y'] -= 1
            if keys[pygame.K_UP]:
                current_piece['shape'] = [list(row) for row in zip(*current_piece['shape'][::-1])]
                if check_collision(board, current_piece):
                    current_piece['shape'] = [list(row) for row in [zip(*current_piece['shape'])][::-1]]

            if keys[pygame.K_SPACE]:
                while not check_collision(board, current_piece):
                    current_piece['y'] += 1
                current_piece['y'] -= 1

        fall_time += 1
        if fall_time >= FPS: 
            current_piece['y'] += 1
            score += 1 
            if check_collision(board, current_piece):
                current_piece['y'] -= 1
                for y in range(len(current_piece['shape'])):
                    for x in range(len(current_piece['shape'][y])):
                        if current_piece['shape'][y][x]:
                            board[current_piece['y'] + y][current_piece['x'] + x] = current_piece['color']
                cleared_lines = clear_lines(board)
                if cleared_lines > 0:
                    score += cleared_lines * 100 
                best_score = max(best_score, score)
                current_piece = create_new_piece()
                if check_collision(board, current_piece):
                    game_over = True
                fall_time = 0

        draw_board(board)

        for y in range(len(current_piece['shape'])):
            for x in range(len(current_piece['shape'][y])):
                if current_piece['shape'][y][x]:
                    pygame.draw.rect(screen, current_piece['color'], ((current_piece['x'] + x) * BLOCK_SIZE, (current_piece['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        draw_text(f"Score: {score}", WHITE, 10, 10)
        draw_text(f"Best Score: {best_score}", WHITE, 10, 40)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    run_game()
