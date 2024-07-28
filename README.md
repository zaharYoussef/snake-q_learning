# Snake Game Q-Learning Agent

## Introduction

This project implements a Q-learning agent to learn how to play the classic game Snake. The motivation behind this project was my interest in agent learning and a desire to implement a project to understand and apply the basics of reinforcement learning.

## Files

The project consists of the following files:

1. **snake_game.py**: Contains the game logic and returns the rewards used for training the agent.
2. **render_game.py**: Used to ensure the game is playable and free of bugs. You can run this file and play the game of Snake.
3. **render_trained_snake.py**: Visualizes the agent playing the game after training.
4. **train_snake.py**: Contains the training loop for the Q-learning agent.
5. **q_learning_agent.py**: Defines the Q-learning agent and its methods.

## Requirements

The project is implemented in Python 3.7.4. All necessary packages are listed in the `requirements.txt` file.


## Q-Learning and Epsilon-Greedy Strategy
Reinforcement learning is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward. The agent explores the environment, receives feedback through rewards or penalties, and uses this feedback to improve its future actions.

In this project, I am using Q-learning, a model-free reinforcement learning algorithm, combined with an epsilon-greedy strategy to balance exploration and exploitation.

### Q-Learning
Q-learning seeks to find the best action to take given the current state by learning a Q-value for each state-action pair. This Q-value represents the expected utility of taking a specific action in a given state. The agent updates its Q-values using the Bellman equation:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left( r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right)
$$

Where:
- $\alpha$ is the learning rate,
- $\gamma$ is the discount factor,
- $r$ is the reward,
- $s$ is the current state,
- $a$ is the action,
- $s'$ is the next state,
- $a'$ is the next action.

### Epsilon-Greedy Strategy

The epsilon-greedy strategy is used to balance exploration (trying new actions) and exploitation (choosing the best-known action). With probability $\epsilon$, the agent selects a random action (exploration), and with probability $1 - \epsilon$, it selects the action that maximizes the Q-value (exploitation). Over time, $\epsilon$ decays to encourage more exploitation as the agent becomes more confident in its learned Q-values. This decay allows the agent to gradually shift focus from exploring the environment to exploiting its knowledge to maximize rewards.

## Usage

To train an agent simply run the `train_snake.py` code. Once the training is done you can run `render_trained_snake.py` and see the agent play the game.