// 12/20/2024
// I wanted to put my C programming skills into practice by implementing game mechanics like collision detection, physics, and dynamic difficulty adjustment. Therefore, I made this 2D platform game with enemies that the player has to avoid the enemies.
// This game helped me better understand how to manage game states and apply mathematical concepts to create an interactive game environment.

#include <SDL2/SDL.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600
#define PLAYER_WIDTH 50
#define PLAYER_HEIGHT 50
#define PLATFORM_WIDTH 100
#define PLATFORM_HEIGHT 20
#define ENEMY_WIDTH 40
#define ENEMY_HEIGHT 40
#define GRAVITY 500.0f
#define JUMP_SPEED -350.0f
#define PLAYER_SPEED 200.0f
#define ENEMY_SPEED 100.0f

typedef struct {
    SDL_Rect rect;
    float velX, velY;
    bool onGround;
} Player;

typedef struct {
    SDL_Rect rect;
} Platform;

typedef struct {
    SDL_Rect rect;
    float velX;
} Enemy;

bool checkCollision(SDL_Rect a, SDL_Rect b);

int main() {
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("2D Platformer with Enemies", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, 0);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    if (!window || !renderer) {
        SDL_Log("Failed to create window or renderer: %s", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    Player player = {{WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2, WINDOW_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT}, 0, 0, false};

    Platform platforms[3] = {
        {{200, 500, PLATFORM_WIDTH, PLATFORM_HEIGHT}},
        {{400, 400, PLATFORM_WIDTH, PLATFORM_HEIGHT}},
        {{600, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT}}
    };

    Enemy enemies[2] = {
        {{220, 470, ENEMY_WIDTH, ENEMY_HEIGHT}, ENEMY_SPEED},
        {{420, 370, ENEMY_WIDTH, ENEMY_HEIGHT}, -ENEMY_SPEED}
    };

    int score = 0;
    Uint32 startTime = SDL_GetTicks();

    bool running = true;
    SDL_Event event;
    Uint32 lastTime = SDL_GetTicks();
    float deltaTime;

    while (running) {
        Uint32 currentTime = SDL_GetTicks();
        deltaTime = (currentTime - lastTime) / 1000.0f;
        lastTime = currentTime;

        int elapsedTime = (currentTime - startTime) / 1000; // Time in seconds
        float difficultyMultiplier = 1.0f + floor(elapsedTime / 10) * 0.2f; // Increase speed by 20% every 10 seconds

        for (int i = 0; i < 2; ++i) {
            enemies[i].rect.x += (int)(enemies[i].velX * difficultyMultiplier * deltaTime);

            if (enemies[i].rect.x <= platforms[i].rect.x || enemies[i].rect.x + enemies[i].rect.w >= platforms[i].rect.x + platforms[i].rect.w) {
                enemies[i].velX = -enemies[i].velX;
            }
        }

        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            } else if (event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_SPACE && player.onGround) {
                player.velY = JUMP_SPEED;
                player.onGround = false;
            }
        }

        const Uint8* keystate = SDL_GetKeyboardState(NULL);
        player.velX = 0;
        if (keystate[SDL_SCANCODE_LEFT]) {
            player.velX = -PLAYER_SPEED;
        }
        if (keystate[SDL_SCANCODE_RIGHT]) {
            player.velX = PLAYER_SPEED;
        }

        player.velY += GRAVITY * deltaTime;

        player.rect.x += (int)(player.velX * deltaTime);
        player.rect.y += (int)(player.velY * deltaTime);

        if (player.rect.x < 0) player.rect.x = 0;
        if (player.rect.x + player.rect.w > WINDOW_WIDTH) player.rect.x = WINDOW_WIDTH - player.rect.w;
        if (player.rect.y + player.rect.h > WINDOW_HEIGHT) {
            player.rect.y = WINDOW_HEIGHT - player.rect.h;
            player.onGround = true;
            player.velY = 0;
        }

        player.onGround = false;
        for (int i = 0; i < 3; ++i) {
            if (checkCollision(player.rect, platforms[i].rect) && player.velY > 0) {
                player.rect.y = platforms[i].rect.y - player.rect.h;
                player.onGround = true;
                player.velY = 0;
            }
        }

        for (int i = 0; i < 2; ++i) {
            enemies[i].rect.x += (int)(enemies[i].velX * deltaTime);

            if (enemies[i].rect.x <= platforms[i].rect.x || enemies[i].rect.x + enemies[i].rect.w >= platforms[i].rect.x + platforms[i].rect.w) {
                enemies[i].velX = -enemies[i].velX;
            }
        }

        for (int i = 0; i < 2; ++i) {
            if (checkCollision(player.rect, enemies[i].rect)) {
                running = false; 
                printf("Game Over! Final Score: %d\n", score);
            }
        }

        score = (SDL_GetTicks() - startTime) / 1000;

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255); 
        SDL_RenderFillRect(renderer, &player.rect);

        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        for (int i = 0; i < 3; ++i) {
            SDL_RenderFillRect(renderer, &platforms[i].rect);
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255); 
        for (int i = 0; i < 2; ++i) {
            SDL_RenderFillRect(renderer, &enemies[i].rect);
        }

        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255); 
        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

bool checkCollision(SDL_Rect a, SDL_Rect b) {
    return a.x + a.w > b.x && a.x < b.x + b.w && a.y + a.h > b.y && a.y < b.y + b.h;
}
