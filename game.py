from level import Level, Levels, LevelContainer
from locations import *


class Game(LevelContainer):
    def __init__(self, hud):
        super().__init__()
        self.hud = hud
        Levels.add('game', self)
        self.index = 0
        self.levels = [Garden(
            self), Kitchen(self), Bedroom(self)]
        self.change_level(self.levels[self.index])

    def update(self, events):
        super().update(events)
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.index = (self.index - 1) % len(self.levels)
                    self.change_level(self.levels[self.index])
                elif event.key == K_RIGHT:
                    self.index = (self.index + 1) % len(self.levels)
                    self.change_level(self.levels[self.index])
