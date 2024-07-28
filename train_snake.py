import numpy as np
from snake_game import SnakeGame
from q_learning_agent import QLearningAgent

def train():
    episodes = 1500
    game = SnakeGame()
    agent = QLearningAgent(state_size=11, action_size=4, learning_rate=0.1, discount_factor=0.9, epsilon_decay=0.995)  # Adjusted parameters

    for e in range(episodes):
        state = game.reset()
        state = tuple(state)
        total_reward = 0
        while True:
            action = agent.choose_action(state)
            next_state, reward, done, score = game.step(action)
            next_state = tuple(next_state)
            agent.learn(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
            if done:
                print(f"Episode {e + 1}/{episodes}, Score: {score}, Total Reward: {total_reward}, Epsilon: {agent.epsilon:.2f}")
                total_reward = 0
                break

    agent.save("q_learning_snake_agent.pkl")

if __name__ == "__main__":
    train()
