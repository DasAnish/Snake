import Game
from DynamicTuple import DynamicTuple
from Snake import Snake

class SnakeBot(Snake):

    def __init__(self, window_size):
        Snake.__init__(self, window_size)
        self.dir = Game.LEFT

    def get_dir(self):
        return self.dir

    def update(self, apple_pos):
        # TODO: Implement the Neural Network
        Snake.update(self, Game.LEFT)
