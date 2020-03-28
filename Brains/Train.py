import pygame
from GameFiles.Game import *
from GameFiles.DynamicTuple import DynamicTuple
from GameFiles.SnakeBot import SnakeBot
from Brains.Population import Population

"""This will run the training schedules."""


class Training(Game):

    def __init__(self, name, winX, winY):
        self.window = DynamicTuple(winX, winY)
        self.FPS=16
        self.clock = pygame.tick.clock()

        pygame.init()
        self.font = pygame.font.SysFont('Bradley Hand ITC', 30)
        self.gameDisplay = pygame.display.set_mode(self.window.to_tuple())
        pygame.display.set_caption(name)

        self.population = Population()
        self.snake_population = []

        for i in range(self.population.population_size):
            self.snake_population.append(SnakeBot(self.window.to_tuple(),
                                                  self.population.population[i]))

        self.colors = [
            (255, 0, 0),
            (255, 85, 0),
            (255, 170, 0),
            (255, 255, 0),
            (170, 255, 0),
            (85, 255, 0),
            (0, 255, 0),
            (0, 255, 85),
            (0, 255, 170),
            (0, 255, 255),
            (0, 170, 255),
            (0, 85, 255),
            (0, 0, 255),
            (85, 0, 255),
            (170, 0, 255),
            (255, 0, 255),
            (255, 0, 170),
            (255, 0, 85),
            (85, 85, 85),
            (170, 170, 170)
        ]

        self.apple_positions = []
        for i in range(20):
            self.apple_positions.append(self.get_apple_position())

        self.running = [True for _ in range(self.population.population_size)]


    def plot_snake(self, i):
        snake = self.snake_population[i]

        for part in snake.body_pos:
            x = part.x
            y = part.y
            pygame.draw.rect(self.gameDiplay, self.colors[i],
                             (x, y, SIZE, SIZE))

        pygame.draw.rect(self.gameDiplay, self.colors[i],
                         (snake.head_pos.x, snake.head_pos.y, SIZE, SIZE))

        apple = self.apple_positions[snake.apples_eaten]
        pygame.draw.rect(self.gameDiplay, self.colors[i],
                         (apple.x, apple.y, SIZE, SIZE))

    def plot_snakes(self):
        for i in range(self.population.population_size):
            self.plot_snake(i)

    @staticmethod
    def ate_food(snake, apple_pos):
        eaten = Game.ate_food(snake, apple_pos)
        if eaten: snake.apples_eaten +=1

    def check_food_for_snakes(self):
        for i, snake in enumerate(self.snake_population):
            self.ate_food(snake,
                          self.apple_positions[snake.apples_eaten])

    def check_collisions(self):
        for i, snake in enumerate(self.snake_population):
            if self.check_collision(snake, self.window):
                self.running[i] = False

    def gen_loop(self):
        while any(self.running):
            pass

