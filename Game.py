from DynamicTuple import DynamicTuple
import pygame
from Snake import Snake
from random import randint
import time

# Constants

LEFT = L = 0
UP = U = 1
RIGHT = R = 2
DOWN = D = 3
SIZE = 20

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

true = True
false = False

class Game:
    def __init__(self, name, winX, winY, appleFileName, snakeFileName):
        self.window = DynamicTuple(winX, winY) # In terms of boxes
        self.imageApple = pygame.image.load(appleFileName)
        self.imageSnake = pygame.image.load(snakeFileName)
        self.FPS = 16
        self.clock = pygame.time.Clock()

        self.snake = Snake(self.window.to_tuple())

        self.font = pygame.font.SysFont('Consolas', 30)



        ######### Inializing Pygame
        pygame.init()
        self.gameDiplay = pygame.display.set_mode(self.window.to_tuple())
        pygame.display.set_caption(name)


        ######## Initial stuff
        self.fill(WHITE)
        self.message_to_screen("Snake Game", GREEN, 150,
                               self.window.y * SIZE // 2 - 150)
        self.message_to_screen("Press\n" +
                               "C to Continue\n"+
                               "E to Exit\n"+
                               "P to Pause",
                               RED, 40,
                               self.window.y * SIZE // 2 + 100)
        self.update_screen()

    def text_objects(self, text, color):
        text_surface = self.font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_to_screen(self, text, color, size, y_pos):
        self.font = pygame.font.SysFont('Consolas', size)
        surface, rect = self.text_objects(text, color)
        rect.center = self.window.x * SIZE / 2, y_pos
        self.gameDiplay.blit(surface, rect)

    def fill(self, color):
        self.gameDiplay.fill(color)

    def update_screen(self):
        pygame.display.update()

    def get_apple_position(self):
        return DynamicTuple(randint(0, self.window.x - 1),
                            randint(0, self.window.y - 1))

    def plot_snake(self, direction):
        for part in self.snake.body_pos: # Plotting the body
            x = part.x
            y = part.y
            pygame.draw.rect(self.gameDiplay,
                             (x, y, SIZE, SIZE))

        # Plotting the head
        head = self.imageSnake
        if (direction == R): head = pygame.transform.rotate(self.imageSnake, 270)
        elif (direction == L): head = pygame.transform.rotate(self.imageSnake, 90)
        elif (direction == D): head = pygame.transform.rotate(self.imageSnake, 180)

        self.gameDiplay.blit(head,
                             (self.snake.head_pos.x,
                              self.snake.head_pos.y))

    def pause_game(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    if event.key == pygame.K_e:
                        pygame.quit()


            self.fill(WHITE)
            self.message_to_screen('PAUSED', GREEN, 200,
                                   self.window.y * SIZE // 2 - 150)
            self.message_to_screen('Press \n'+
                                   'C to Continue\n'+
                                   'E to Exit',
                                   RED,
                                   50,
                                   self.window.y * SIZE // 2 + 100)
            self.update_screen()

    def display_score(self):
        self.font = pygame.font.SysFont('Consolas', 30)
        text = self.font.render('Score: {0}'.format(self.snake.length), True, BLACK)
        self.gameDiplay.blit(text, [0, 0])

    def main_loop(self):
        dir = RIGHT

        playing = True
        apple_position = self.get_apple_position()

        while playing:
            self.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: playing = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p: self.pause_game()
                    elif event.key in (pygame.K_RIGHT, pygame.K_d): dir = RIGHT
                    elif event.key in (pygame.K_LEFT, pygame.K_a): dir = LEFT
                    elif event.key in (pygame.K_DOWN, pygame.K_s): dir = DOWN
                    elif event.key in (pygame.K_UP, pygame.K_w): dir = UP

            self.snake.update(dir)

            # Plotting food
            self.gameDiplay.blit(self.imageApple,
                                 (apple_position.x, apple_position.y,
                                  SIZE, SIZE))

            # checking for collision
            self.snake.ate_food = (self.snake.head_pos.x == apple_position.x and
                                   self.snake.head_pos.y == apple_position.y)

            self.plot_snake(dir)
            self.display_score()
            self.update_screen()

            if (self.snake.ate_food): apple_position = self.get_apple_position()

            self.clock.tick(self.FPS)

    def game_loop(self):
        # TODO: handle the tasks that need to be done around the mainloop
        pass



