import numpy as np
from pickle import load, dump
import random

class DNA:

    def __init__(self, index, mutation_rate=0.01, from_values=False,
                 w1=None, w2=None, b1=None, b2=None):
        self.mutation_rate = mutation_rate
        self.index = index
        if not from_values:
            self.w1 = self.get_w1()
            self.w2 = self.get_w2()
            self.b1 = self.get_b1()
            self.b2 = self.get_b2()
        else:
            self.w1 = w1
            self.w2 = w2
            self.b1 = b1
            self.b2 = b2
            self.update_values()

    def update_values(self):
        pass

    def get_w1(self):
        return np.ones((900, 16))

    def get_w2(self):
        return np.ones((16, 4))

    def get_b1(self):
        return np.ones(16)

    def get_b2(self):
        return np.ones(4)

    def __mul__(self, othr):
        merge = np.vectorize(lambda x, y: x if (random.random<0.5) else y)
        w1 = merge(self.w1.flatten(), othr.w1.flatten())
        w2 = merge(self.w2.flatten(), othr.w2.flatten())
        b1 = merge(self.b1, othr.b1)
        b2 = merge(self.b2, othr.b2)

        w1 = w1.reshape((900, 16))
        w2 = w2.reshape((16, 4))

        return DNA(self.index, from_values=True, w1=w1, w2=w2, b1=b1, b2=b2)
