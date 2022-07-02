class Transform:
    def __init__(self, transformations=None):
        self.transformations = transformations or []

    def and_then(self, transformation):
        return Transform(self.transformations + [transformation])

    def __call__(self, vec):
        for transformation in self.transformations:
            vec = transformation(vec)
        return vec

    def inverse(self):
        return Transform([t.inverse() for t in reversed(self.transformations)])


class Scale:
    def __init__(self, scale):
        super().__init__()
        self.scale = scale

    def scale(self, scale):
        self.scale = scale

    def __call__(self, vec):
        return vec * self.scale

    def inverse(self):
        return Scale(1 / self.scale)


class Translate:
    def __init__(self, translation):
        super().__init__()
        self.translation = translation

    def __call__(self, vec):
        return vec + self.translation

    def inverse(self):
        return Translate(-self.translation)
