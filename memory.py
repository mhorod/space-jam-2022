import pygame as pg
from level import Level

import time
from assets import Assets
from animation import *


class Memory(Level):
    def __init__(self, name, parent_location, *args, **kwargs):
        super().__init__(name, parent_location.parent, *args, **kwargs)
        self.name = name
        self.background = Assets.files[f"assets/memories/{name}.png"]
        self.time = None
        self.parent_location = parent_location

    def start(self):
        self.time = time.time()
        self.parent.hud.hide()

    def update(self, events):
        if time.time() - self.time > 3:
            self.parent.change_level(
                self.parent_location, TransitionAnimation.AnimEnum.fade)
            self.parent.hud.show()


class Memories:
    def load_memories():
        pass
