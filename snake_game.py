import random
import numpy as np

class SnakeGame:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.snake = [(self.width // 2, self.height // 2)]
        self.snake_dir = (0, -20)
        self.food = self.place_food()
        self.score = 0
        return self.get_state()

    def place_food(self):
        while True:
            x = random.randint(0, (self.width - 20) // 20) * 20
            y = random.randint(0, (self.height - 20) // 20) * 20
            if (x, y) not in self.snake:
                return (x, y)

    def step(self, action):
        if action == 0 and self.snake_dir != (0, 20):  # Go up
            self.snake_dir = (0, -20)
        elif action == 1 and self.snake_dir != (0, -20):  # Go down
            self.snake_dir = (0, 20)
        elif action == 2 and self.snake_dir != (20, 0):  # Go left
            self.snake_dir = (-20, 0)
        elif action == 3 and self.snake_dir != (-20, 0):  # Go right
            self.snake_dir = (20, 0)

        new_head = (self.snake[0][0] + self.snake_dir[0], self.snake[0][1] + self.snake_dir[1])

        if new_head[0] < 0 or new_head[0] >= self.width or new_head[1] < 0 or new_head[1] >= self.height or new_head in self.snake:
            return self.get_state(), -10, True, self.score  # Game over

        self.snake = [new_head] + self.snake[:-1]

        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.place_food()
            self.score += 1
            return self.get_state(), 10, False, self.score

        # Calculate the gradient reward based on distance to the food
        distance_to_food = abs(self.food[0] - new_head[0]) + abs(self.food[1] - new_head[1])
        if len(self.snake) > 1:
            distance_from_head = abs(self.food[0] - self.snake[1][0]) + abs(self.food[1] - self.snake[1][1])
        else:
            distance_from_head = distance_to_food + 1  # Arbitrary value to ensure the reward is calculated correctly

        if distance_to_food < distance_from_head:
            return self.get_state(), 1, False, self.score
        else:
            return self.get_state(), -0.5, False, self.score

    def get_state(self):
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        state = [
            # Food location
            food_x < head_x,  # Food left
            food_x > head_x,  # Food right
            food_y < head_y,  # Food up
            food_y > head_y,  # Food down
            # Current direction
            self.snake_dir == (0, -20),  # Moving up
            self.snake_dir == (0, 20),   # Moving down
            self.snake_dir == (-20, 0),  # Moving left
            self.snake_dir == (20, 0),   # Moving right
            # Danger of collision
            self.collision((head_x, head_y - 20)),  # Danger up
            self.collision((head_x, head_y + 20)),  # Danger down
            self.collision((head_x - 20, head_y)),  # Danger left
            self.collision((head_x + 20, head_y))   # Danger right
        ]
        return np.array(state, dtype=int)

    def collision(self, point):
        if point[0] < 0 or point[0] >= self.width or point[1] < 0 or point[1] >= self.height or point in self.snake:
            return 1
        else:
            return 0
