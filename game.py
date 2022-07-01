from level import Level
from locations import Garden


class Game(Level):
    def __init__(self, *args, **kwargs):
        super().__init__('game', *args, **kwargs)
        self.garden = Garden(self.parent)
        self.append_child(self.garden)
