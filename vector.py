class Vec2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def from_tuple(vector):
        return Vec2(vector[0], vector[1])

    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y

    def __iter__(self):
        return iter((self.x, self.y))

    def __len__(self):
        return 2

    def __add__(self, u):
        return Vec2(self.x + u.x, self.y + u.y)

    def __sub__(self, u):
        return Vec2(self.x - u.x, self.y - u.y)
