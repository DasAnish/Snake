from GameFiles import Game
from GameFiles.Snake import Snake
from GameFiles.DynamicTuple import DynamicTuple
import numpy as np
from Brains.DNA import DNA


class SnakeBot(Snake):

    def __init__(self, window_size, dna=None):
        Snake.__init__(self, window_size)
        self.starting_nodes = window_size[0] * window_size[1] // (Game.SIZE ** 2)
        self.window = DynamicTuple(window_size)
        self.dir = Game.LEFT
        self.dna = dna
        self.apples_eaten = 0

    def get_dir(self, apple_pos):
        headx = self.head_pos.x
        heady = self.head_pos.y

        winx = self.window.x
        winy = self.window.y

        left_dist = right_dist = up_dist = down_dist = -1
        lu_dist = ld_dist = ru_dist = rd_dist = -1 #left up and right down

        applex = apple_pos.x - headx
        appley = apple_pos.y - heady

        for i in range(1, headx+1): # for left
            if DynamicTuple(headx-i, heady) in self.body_pos:
                break
        left_dist = i

        for i in range(1, winx-headx):
            if DynamicTuple(headx+i, heady) in self.body_pos:
                break
        right_dist = i

        for i in range(1, heady+1):
            if DynamicTuple(headx, heady-i) in self.body_pos:
                break
        up_dist = i

        for i in range(1, winy-heady):
            if DynamicTuple(headx, heady+i) in self.body_pos:
                break
        down_dist = i

        def check(x, y):
            return x >= winx or y >= winx or x < 0 or y < 0

        for i in range(1, min(winx, winy)):
            newheadx = headx-i #this is left up
            newheady = heady-i

            if check(newheadx, newheady):
                if lu_dist == -1: lu_dist = i

            newheadx = headx+i
            if check(newheadx, newheady):
                if ru_dist == -1: ru_dist = i

            newheady = heady+i
            if check(newheadx, newheady):
                if rd_dist == -1: rd_dist = i

            newheadx = headx - i
            if check(newheadx, newheady):
                if ld_dist == -1: ld_dist = i

            if ld_dist != -1 and lu_dist != -1 and rd_dist != -1 and ru_dist != -1:
                break

        _input = [left_dist, right_dist, up_dist, down_dist,
                  lu_dist, ld_dist, rd_dist, ru_dist,
                  applex, appley]

        activate = lambda x: np.exp(x) / (np.exp(x) + 1)
        softmax = lambda x: np.exp(x) / sum(np.exp(x))

        _layer1 = np.matmul(_input, self.dna.w0) + self.dna.b0
        _layer1 = activate(_layer1)

        _layer2 = np.matmul(_layer1, self.dna.w1) + self.dna.b1
        _layer2 = activate(_layer2)

        _final = np.matmul(_layer2, self.dna.w2) + self.dna.b2
        _final = softmax(_final)

        self.dir = np.argmax(_final)
        return self.dir

        # Snake.update(self, Game.LEFT)
    def update(self, apple_pos):
        Snake.update(self, self.get_dir(apple_pos))
