#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <ctime>

const int WINDOW_WIDTH = 600;
const int WINDOW_HEIGHT = 600;
const int GRID_SIZE = 20;

enum Direction { Up, Down, Left, Right };

struct SnakeSegment {
    int x, y;
    SnakeSegment(int x, int y) : x(x), y(y) {}
};

class Snake {
private:
    std::vector<SnakeSegment> segments;
    Direction dir;

public:
    Snake(int startX, int startY) : dir(Right) {
        segments.emplace_back(startX, startY);
    }

    void move() {
        int newX = segments[0].x;
        int newY = segments[0].y;

        if (dir == Up) newY -= GRID_SIZE;
        if (dir == Down) newY += GRID_SIZE;
        if (dir == Left) newX -= GRID_SIZE;
        if (dir == Right) newX += GRID_SIZE;

        segments.insert(segments.begin(), SnakeSegment(newX, newY));

        segments.pop_back();
    }

    void grow() {
        segments.push_back(segments.back()); 
    }

    void setDirection(Direction newDir) {
        if ((dir == Up && newDir != Down) ||
            (dir == Down && newDir != Up) ||
            (dir == Left && newDir != Right) ||
            (dir == Right && newDir != Left)) {
            dir = newDir;
        }
    }

    bool checkCollision() const {
        for (size_t i = 1; i < segments.size(); ++i) {
            if (segments[0].x == segments[i].x && segments[0].y == segments[i].y) {
                return true;
            }
        }
        if (segments[0].x < 0 || segments[0].x >= WINDOW_WIDTH ||
            segments[0].y < 0 || segments[0].y >= WINDOW_HEIGHT) {
            return true;
        }
        return false;
    }

    const std::vector<SnakeSegment>& getSegments() const {
        return segments;
    }
};

class Food {
private:
    int x, y;

public:
    Food() {
        respawn();
    }

    void respawn() {
        x = (std::rand() % (WINDOW_WIDTH / GRID_SIZE)) * GRID_SIZE;
        y = (std::rand() % (WINDOW_HEIGHT / GRID_SIZE)) * GRID_SIZE;
    }

    int getX() const { return x; }
    int getY() const { return y; }
};

int main() {
    std::srand(std::time(nullptr));

    sf::RenderWindow window(sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), "Snake Game");
    window.setFramerateLimit(10);

    Snake snake(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2);
    Food food;

    bool gameOver = false;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        if (gameOver) {
            continue;
        }

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
            snake.setDirection(Up);
        } else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
            snake.setDirection(Down);
        } else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
            snake.setDirection(Left);
        } else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
            snake.setDirection(Right);
        }

        snake.move();

        if (snake.getSegments()[0].x == food.getX() &&
            snake.getSegments()[0].y == food.getY()) {
            snake.grow();
            food.respawn();
        }

        if (snake.checkCollision()) {
            gameOver = true;
        }

        window.clear();

        for (const auto& segment : snake.getSegments()) {
            sf::RectangleShape segmentShape(sf::Vector2f(GRID_SIZE, GRID_SIZE));
            segmentShape.setFillColor(sf::Color::Green);
            segmentShape.setPosition(segment.x, segment.y);
            window.draw(segmentShape);
        }

        sf::RectangleShape foodShape(sf::Vector2f(GRID_SIZE, GRID_SIZE));
        foodShape.setFillColor(sf::Color::Red);
        foodShape.setPosition(food.getX(), food.getY());
        window.draw(foodShape);

        if (gameOver) {
            sf::Font font;
            if (!font.loadFromFile("arial.ttf")) {
                return -1;
            }
            sf::Text text("Game Over", font, 50);
            text.setFillColor(sf::Color::White);
            text.setPosition(WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2 - 50);
            window.draw(text);
        }

        window.display();
    }

    return 0;
}
