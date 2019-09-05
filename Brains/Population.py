import random

class Population:

    def __init__(self):
        self.population = []

    def create_next_gen(self):
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
            next_gen.append( self.population[parent1] * self.population[parent2])
            next_gen[-1].index = i
        self.population = next_gen()

    def update_score(self, index, score):
        self.scores[index] = score

