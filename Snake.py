import Game
from DynamicTuple import DynamicTuple


class Snake:

    def __init__(self, window_size):
        self.length = 0
        self.head_pos = DynamicTuple(window_size[0] // 2, window_size[1] // 2)
        self.body_pos = []
        # list of tuples
        self.ate_food = False

    def update(self, dir):
        head_pos = self.head_pos.to_tuple()
        self.body_pos.append(self.head_pos.copy())
        if dir == Game.D:
            self.head_pos += DynamicTuple(0, Game.SIZE)
        elif dir == Game.U:
            self.head_pos -= DynamicTuple(0, Game.SIZE)
        elif dir == Game.L:
            self.head_pos -= DynamicTuple(Game.SIZE, 0)
        else:
            self.head_pos += DynamicTuple(Game.SIZE, 0)


        # Most recent position is in the back
        if not self.ate_food:
            self.body_pos = self.body_pos[1:]
        if self.ate_food: self.length += 1
        self.ate_food = False

    def score(self):
        return self.length


