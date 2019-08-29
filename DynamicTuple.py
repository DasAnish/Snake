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
        self.x += other.x
        self.y += other.y

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def to_tuple(self):
        return (self.x, self.y)