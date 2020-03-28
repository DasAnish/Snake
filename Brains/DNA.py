import numpy as np
from pickle import load, dump
import random

class DNA:

    def __init__(self, index, mutation_rate=0.01, from_values=False,
                 values=None):
        self.mutation_rate = mutation_rate
        self.index = index
        if not from_values:
            self.w0 = self.get_default_w0()
            self.b0 = self.get_default_b0()
            self.w1 = self.get_default_w1()
            self.w2 = self.get_default_w2()
            self.b1 = self.get_default_b1()
            self.b2 = self.get_default_b2()
        else:
            self.w1, self.w2, self.b1, self.b2 = values
            self.update_values()

    def update_values(self):
        pass

    @staticmethod
    def get_default_w0():
        return np.random.random((10, 900))

    @staticmethod
    def get_default_b0():
        return np.random.random(900)

    @staticmethod
    def get_default_w1():
        return np.random.random((900, 16))

    @staticmethod
    def get_default_w2():
        return np.random.random((16, 4))

    @staticmethod
    def get_default_b1():
        return np.random.random(16)

    @staticmethod
    def get_default_b2():
        return np.random.random(4)

    def __mul__(self, othr):
        '''
        The multiply the two dna's i.e. choose certain values from each

        :param othr: python convention for the other argument.

        :return: will return a new dna
        '''
        # choose a random value from two given lists
        merge = np.vectorize(lambda x, y: x if (random.random<0.5) else y)
        w1 = merge(self.w1.flatten(), othr.w1.flatten()) # flatten to turn into simple lists
        w2 = merge(self.w2.flatten(), othr.w2.flatten())
        b1 = merge(self.b1, othr.b1)
        b2 = merge(self.b2, othr.b2)

        w1 = w1.reshape((900, 16))
        w2 = w2.reshape((16, 4))

        # TODO: introduce mutations.

        return DNA(self.index, from_values=True, w1=w1, w2=w2, b1=b1, b2=b2)
