from GameFiles.DynamicTuple import DynamicTuple
import pygame
from GameFiles.Snake import Snake
from GameFiles.SnakeBot import SnakeBot
from random import randint

# Constants

LEFT = L = 0
UP = U = 1
RIGHT = R = 2
DOWN = D = 3
SIZE = 20
DSIZE = DynamicTuple(SIZE, SIZE)

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 150)
YELLOW = (255, 255, 0)

true = True
false = False

class Game:
    def __init__(self, name, winX, winY, appleFileName, snakeFileName):
        self.window = DynamicTuple(winX, winY)
        self.imageApple = pygame.image.load(appleFileName)
        self.imageSnake = pygame.image.load(snakeFileName)
        self.FPS = 16
        self.clock = pygame.time.Clock()

        self.snake = Snake(self.window.to_tuple())
        self.snake_bot = SnakeBot(self.window.to_tuple())




        ######### Inializing Pygame
        pygame.init()
        self.font = pygame.font.SysFont('Bradley Hand ITC', 30)
        self.gameDiplay = pygame.display.set_mode(self.window.to_tuple())
        pygame.display.set_caption(name)


        ######## Initial stuff
        # self.fill(WHITE)
        # self.message_to_screen("Snake GameFiles", GREEN, 150,
        #                        self.window.y // 2 - 150)
        # self.message_to_screen("Press\n" +
        #                        "C to Continue\n"+
        #                        "E to Exit\n"+
        #                        "P to Pause",
        #                        RED, 40,
        #                        self.window.y // 2 + 100)
        # self.update_screen()

    def text_objects(self, text, color):
        text_surface = self.font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_to_screen(self, text, color, size, y_pos):
        self.font = pygame.font.SysFont('Consolas', size)
        surface, rect = self.text_objects(text, color)
        rect.center = self.window.x  // 2, y_pos
        self.gameDiplay.blit(surface, rect)

    def fill(self, color):
        self.gameDiplay.fill(color)

    def update_screen(self):
        pygame.display.update()

    def get_apple_position(self):
        return DynamicTuple(randint(0, self.window.x - SIZE),
                            randint(0, self.window.y - SIZE))

    def plot_snake(self, snake, direction):
        for part in snake.body_pos: # Plotting the body
            x = part.x
            y = part.y
            pygame.draw.rect(self.gameDiplay, GREEN,
                             (x, y, SIZE, SIZE))

        # Plotting the head
        head = self.imageSnake
        if direction == R: head = pygame.transform.rotate(self.imageSnake, 270)
        elif direction == L: head = pygame.transform.rotate(self.imageSnake, 90)
        elif direction == D: head = pygame.transform.rotate(self.imageSnake, 180)

        self.gameDiplay.blit(head,
                             (snake.head_pos.x,
                              snake.head_pos.y))

    def pause_game(self):
        paused = True
        self.fill(WHITE)
        self.message_to_screen('PAUSED', GREEN, 100,
                               self.window.y // 2 - 150)
        self.message_to_screen('''Press''', RED, 50, self.window.y // 2 + 100)
        self.message_to_screen('C to Continue', RED, 50, self.window.y // 2 + 150)
        self.message_to_screen('E to Exit', RED, 50, self.window.y // 2 + 200)
        self.update_screen()
        b = false
        while paused:
            for event in pygame.event.get(pygame.QUIT):
                b = true
                pygame.quit()
            if b: break
            for keyEvent in pygame.event.get(pygame.KEYDOWN):
                key = keyEvent.key
                if key == pygame.K_c:
                    paused = false
                    return true
                elif key == pygame.K_e:
                    return false




    def display_score(self):
        self.font = pygame.font.SysFont('Consolas', 30)
        text = self.font.render('Score: {0}'.format(self.snake.length), True, BLACK)
        self.gameDiplay.blit(text, [0, 0])

    @staticmethod
    def ate_food(snake, apple_pos):
        head = snake.head_pos
        return (apple_pos <= head <= (apple_pos + DSIZE) or
                (apple_pos <= (head + DSIZE) <= (apple_pos + DSIZE)))

    @staticmethod
    def check_collision(snake, window):
        head = snake.head_pos
        if head.x > window.x or head.x < 0 or head.y > window.y or head.y < 0:
            return False
        for block in snake.body_pos:
            if block == head:
                return False

        return True

    def main_loop(self, bool_player, bool_bot):
        dir = RIGHT
        dir_bot = LEFT

        playing = bool_player
        playing_bot = bool_bot
        apple_position = self.get_apple_position()
        ate_apple = False

        if bool_player: self.snake = Snake(self.window.to_tuple())
        if bool_bot: self.snake_bot = SnakeBot(self.window.to_tuple())
        b = false
        while playing or playing_bot:
            self.fill(WHITE)
            for event in pygame.event.get(pygame.QUIT):
                pygame.quit()
                b = true
            if b: break
            for event in pygame.event.get(pygame.KEYDOWN):
                key = event.key
                if key == pygame.K_p:
                    b = self.pause_game()
                    playing = playing and b
                    playing_bot = playing_bot and b
                elif key in (pygame.K_RIGHT, pygame.K_d): dir = RIGHT
                elif key in (pygame.K_LEFT, pygame.K_a): dir = LEFT
                elif key in (pygame.K_DOWN, pygame.K_s): dir = DOWN
                elif key in (pygame.K_UP, pygame.K_w): dir = UP

            # Plotting food
            self.gameDiplay.blit(self.imageApple,
                                (apple_position.x, apple_position.y,
                                 SIZE, SIZE))

            if bool_player:
                self.snake.update(dir)
                print(self.snake.head_pos)

                self.snake.ate_food = self.ate_food(self.snake, apple_position)

                # self.plot_snake(self.snake, dir)

                playing = self.check_collision(self.snake, self.window)

            if bool_bot:
                self.snake_bot.update(apple_position)

                self.snake_bot.ate_food = self.ate_food(self.snake_bot, apple_position)

                # self.plot_snake(self.snake_bot, self.snake_bot.get_dir())

                playing_bot = self.check_collision(self.snake_bot, self.window)

            if self.snake.ate_food or self.snake_bot.ate_food:
                apple_position = self.get_apple_position()

            if bool_player: self.plot_snake(self.snake, dir)
            if bool_bot: self.plot_snake(self.snake_bot, self.snake_bot.get_dir())

            self.display_score()
            self.update_screen()



            self.clock.tick(self.FPS)



        # self.game_over()

    # @staticmethod
    # def get_key_pressed():
    #     while True:
    #         for event in pygame.event.get(pygame.KEYDOWN):
    #             yield event.key


    def game_over(self):
        y = self.window.y//2
        self.fill(WHITE)
        self.message_to_screen('Game Over', GREEN, 100, y -150)
        self.message_to_screen('Score: %d'%self.snake.length, BLUE, 25, y +100)
        self.message_to_screen('Press', RED, 50, y + 150)
        self.message_to_screen('C to Play again', RED, 50, y + 200)
        self.message_to_screen('E to Exit', RED, 50, y + 250)
        self.update_screen()

    def game_start(self):
        y = self.window.y // 2

        self.fill(WHITE)
        self.message_to_screen('Welcome', GREEN, 100, y - 150)
        self.message_to_screen('Press', RED, 50, y + 50)
        self.message_to_screen('C to play', RED, 50, y + 100)
        self.message_to_screen('B to play with bot', RED, 50, y + 150)
        # will remove
        self.message_to_screen('V to play only bot', RED, 50, y + 200)
        self.message_to_screen('E to Exit', RED, 50, y + 250)
        self.update_screen()


    def game_loop(self):
        y = self.window.y // 2
        play = true
        game_over = false
        game_exit = false

        self.game_start()
        b = false
        while play:
            for event in pygame.event.get(pygame.QUIT):
                pygame.quit()
                b = true
            if b: break
            #STARTNG GAME
            for keyEvent in pygame.event.get(pygame.KEYDOWN):
                key = keyEvent.key
                if not game_over:
                    if key == pygame.K_c:
                        self.main_loop(true, false)
                        game_over = true
                    elif key == pygame.K_e:
                        play = false
                        pygame.quit()
                    elif key == pygame.K_b:
                        self.main_loop(true, true)
                        game_over = true
                    elif key == pygame.K_v:
                        self.main_loop(false, true)
                        game_over = true
                else:
                    if key == pygame.K_c:
                        self.game_start()
                        game_over = false
                    elif key == pygame.K_e:
                        play = false
            if play and game_over:
                self.game_over()






