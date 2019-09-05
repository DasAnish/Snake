from GameFiles import Game
from GameFiles.Snake import Snake

class SnakeBot(Snake):

    def __init__(self, window_size):
        Snake.__init__(self, window_size)
        self.starting_nodes = window_size[0] * window_size[1] // (Game.SIZE ** 2)
        self.dir = Game.LEFT

    def get_dir(self):
        return self.dir

    def update(self, apple_pos):
        # TODO: Implement the Neural Network
        Snake.update(self, Game.LEFT)
