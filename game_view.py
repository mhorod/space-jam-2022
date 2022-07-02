from level import Level, Levels, LevelContainer
from locations import *

from memory import Memory


class GameView(LevelContainer):
    '''
    View of the game on the screen
    '''

    def __init__(self, game, hud):
        super().__init__()
        self.game = game
        game.view = self
        self.name = "game"

        self.hud = hud
        Levels.add('game', self)
        self.index = 0
        self.levels = [LocationView(self, location)
                       for location in self.game.locations]

        self.change_level(self.levels[self.index])

    def on_load(self):
        self.game.start()

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

    def trigger_memory(self, memory_name):
        memory = Memory(memory_name, self.game.location.view)
        memory.start()
        self.change_level(memory)

    def change_location(self, location):
        self.change_level(location.view, TransitionAnimation.AnimEnum.swipe)
