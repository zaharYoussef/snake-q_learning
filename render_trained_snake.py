import pygame
import time
from snake_game import SnakeGame
from q_learning_agent import QLearningAgent

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

def render_game(agent, episodes=5):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Trained Snake Game')
    clock = pygame.time.Clock()
    game = SnakeGame(SCREEN_WIDTH, SCREEN_HEIGHT)

    for episode in range(episodes):
        state = game.reset()
        state = tuple(state)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            action = agent.choose_action(state)
            next_state, reward, done, score = game.step(action)
            state = tuple(next_state)

            if done:
                print(f"Episode {episode + 1}/{episodes}, Score: {score}")
                time.sleep(2)
                running = False

            screen.fill(BLACK)
            draw_snake(screen, game.snake)
            draw_food(screen, game.food)
            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()

def validate(agent, num_validation_episodes=100):
    game = SnakeGame()
    scores = []
    total_rewards = []

    for episode in range(num_validation_episodes):
        state = game.reset()
        state = tuple(state)
        episode_score = 0
        episode_reward = 0

        while True:
            action = agent.choose_action(state)
            next_state, reward, done, score = game.step(action)
            state = tuple(next_state)
            episode_reward += reward

            if done:
                episode_score = score
                break

        scores.append(episode_score)
        total_rewards.append(episode_reward)

    average_score = sum(scores) / num_validation_episodes
    average_reward = sum(total_rewards) / num_validation_episodes

    print(f"Validation Results - Average Score: {average_score}, Average Total Reward: {average_reward}")

if __name__ == "__main__":
    agent = QLearningAgent(state_size=11, action_size=4)
    agent.load("q_learning_snake_agent.pkl")

    # Set epsilon to 0 to disable exploration
    agent.epsilon = 0

    # Run validation
    validate(agent, num_validation_episodes=5)

    # Render a few episodes
    render_game(agent, episodes=5)
