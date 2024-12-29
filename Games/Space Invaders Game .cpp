// 12/29/2024
// This was a rewarding experience that allowed me to put my C++ skills into practice. It reinforced concepts like object-oriented programming, collision detection, and game physics. 
// Building this project deepened my understanding of C++ and SFML while teaching me how to break complex tasks into manageable parts.

#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace sf;

const int WINDOW_WIDTH = 800;
const int WINDOW_HEIGHT = 600;
const float PLAYER_SPEED = 400.0f;
const float BULLET_SPEED = 500.0f;
const float ENEMY_SPEED = 100.0f;

struct Bullet {
    RectangleShape shape;
    float speed = BULLET_SPEED;
};

struct Enemy {
    RectangleShape shape;
};

int main() {
    RenderWindow window(VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), "Space Invaders");
    window.setFramerateLimit(60);

    RectangleShape player(Vector2f(60.0f, 20.0f));
    player.setFillColor(Color::Green);
    player.setPosition(WINDOW_WIDTH / 2 - player.getSize().x / 2, WINDOW_HEIGHT - 50);

    std::vector<Bullet> bullets;

    std::vector<Enemy> enemies;
    const int rows = 4, cols = 8;
    const float spacing = 20.0f;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            Enemy enemy;
            enemy.shape.setSize(Vector2f(40.0f, 20.0f));
            enemy.shape.setFillColor(Color::Red);
            enemy.shape.setPosition(j * (40 + spacing) + 100, i * (20 + spacing) + 50);
            enemies.push_back(enemy);
        }
    }

    float enemyDirection = 1.0f;

    Clock clock;

    while (window.isOpen()) {
        Event event;
        while (window.pollEvent(event)) {
            if (event.type == Event::Closed) {
                window.close();
            }
        }

        float deltaTime = clock.restart().asSeconds();

        if (Keyboard::isKeyPressed(Keyboard::Left) && player.getPosition().x > 0) {
            player.move(-PLAYER_SPEED * deltaTime, 0);
        }
        if (Keyboard::isKeyPressed(Keyboard::Right) && player.getPosition().x + player.getSize().x < WINDOW_WIDTH) {
            player.move(PLAYER_SPEED * deltaTime, 0);
        }

        if (Keyboard::isKeyPressed(Keyboard::Space)) {
            Bullet bullet;
            bullet.shape.setSize(Vector2f(5.0f, 10.0f));
            bullet.shape.setFillColor(Color::Yellow);
            bullet.shape.setPosition(player.getPosition().x + player.getSize().x / 2 - 2.5f, player.getPosition().y);
            bullets.push_back(bullet);
        }

        for (size_t i = 0; i < bullets.size(); ++i) {
            bullets[i].shape.move(0, -bullets[i].speed * deltaTime);
            if (bullets[i].shape.getPosition().y < 0) {
                bullets.erase(bullets.begin() + i);
                --i;
            }
        }

        float movement = ENEMY_SPEED * deltaTime * enemyDirection;
        bool changeDirection = false;
        for (Enemy& enemy : enemies) {
            enemy.shape.move(movement, 0);
            if (enemy.shape.getPosition().x <= 0 || enemy.shape.getPosition().x + enemy.shape.getSize().x >= WINDOW_WIDTH) {
                changeDirection = true;
            }
        }
        if (changeDirection) {
            enemyDirection *= -1;
            for (Enemy& enemy : enemies) {
                enemy.shape.move(0, 20);
            }
        }

        for (size_t i = 0; i < bullets.size(); ++i) {
            for (size_t j = 0; j < enemies.size(); ++j) {
                if (bullets[i].shape.getGlobalBounds().intersects(enemies[j].shape.getGlobalBounds())) {
                    bullets.erase(bullets.begin() + i);
                    enemies.erase(enemies.begin() + j);
                    --i;
                    break;
                }
            }
        }

        for (const Enemy& enemy : enemies) {
            if (enemy.shape.getPosition().y + enemy.shape.getSize().y >= WINDOW_HEIGHT) {
                window.close(); 
            }
        }

        window.clear();
        window.draw(player);
        for (const Bullet& bullet : bullets) {
            window.draw(bullet.shape);
        }
        for (const Enemy& enemy : enemies) {
            window.draw(enemy.shape);
        }
        window.display();

        if (enemies.empty()) {
            window.close();
        }
    }

    return 0;
}
