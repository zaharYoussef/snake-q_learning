import pygame
import time
from snake_game import SnakeGame

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

def render_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    game = SnakeGame(SCREEN_WIDTH, SCREEN_HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        action = None  # Default action: no movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and game.snake_dir != (0, 20):
            action = 0  # Go up
        elif keys[pygame.K_DOWN] and game.snake_dir != (0, -20):
            action = 1  # Go down
        elif keys[pygame.K_LEFT] and game.snake_dir != (20, 0):
            action = 2  # Go left
        elif keys[pygame.K_RIGHT] and game.snake_dir != (-20, 0):
            action = 3  # Go right

        if action is not None:
            state, reward, done, score = game.step(action)
            if done:
                print(f"Game Over! Score: {score}")
                time.sleep(2)
                state = game.reset()

        screen.fill(BLACK)
        draw_snake(screen, game.snake)
        draw_food(screen, game.food)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    render_game()
