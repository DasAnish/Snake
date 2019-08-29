class DynamicTuple:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return DynamicTuple(self.x + other.x,
                            self.y + other.y)

    def __sub__(self, other):
        return DynamicTuple(self.x - other.x,
                            self.y - other.y)

    def __mul__(self, i):
        return DynamicTuple(self.x*i, self.y*i)

    def __div__(self, i):
        return DynamicTuple(self.x/i, self.y/i)

    def __iadd__(self, other):
        return self+other

    def __isub__(self, other):
        return self-other

    def to_tuple(self):
        return (self.x, self.y)

    def __str__(self):
        return "(%d, %d)" %(self.x, self.y)

    def _le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def copy(self):
        return DynamicTuple(self.x, self.y)