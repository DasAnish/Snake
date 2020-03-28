import random
from Brains.DNA import DNA


class Population:

    def __init__(self):
        self.population = []
        self.population_size= 20

        # creates a population of 20(population size will change).
        for i in range(self.population_size):
            self.population.append(DNA(i))

    def create_next_gen(self):
        '''
        This function goes through the population and randomly based on the scores decides
        who gets to mate with whom.
        :return: returns a new generation of population.
        '''
        s = sum(self.scores)
        probs = [sum(self.scores[:i])/s
                 for i in range(1, len(self.scores)+1)]
        next_gen = []

        for i in range(20):
            r1 = random.random()
            r2 = random.random()

            parent1 = -1
            parent2 = -1

            for v in probs:
                if r1 < v and parent1 == -1:
                    parent1 = probs.index(v)

                if r2 < v and parent2 == -1:
                    parent2 = probs.index(v)

                if r1 < v and r2 < v:
                    break
            # get the values and then multiply
            next_gen.append(self.population[parent1] * self.population[parent2])
            next_gen[-1].index = i
        self.population = next_gen()

    def update_score(self, index, score):
        self.scores[index] = score

