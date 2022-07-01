import pygame as pg
from pygame.locals import *

from level import Level, LevelContainer
from sprite import Sprite
from vector import Vec2


class Location(Level):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = self.load_image("background")

    def load_image(self, object_name):
        return pg.image.load(self.path(object_name))

    def path(self, object_name):
        return f"assets/locations/{self.name}/{object_name}.png"

    def load_sprite(self, object_name):
        return Sprite(Vec2(0, 0), self.path(object_name))

    def load_sprites(self, names):
        return [self.load_sprite(name) for name in names]


class Garden(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('garden', *args, **kwargs)
        self.objects = self.load_sprites(["bench", "duck", "gate", "path"])
        self.objects[0].callback = lambda: self.parent.change_level('bench')
        self.objects[1].callback = lambda: self.parent.change_level('duck')
        self.bench = CloseUp('bench', self)
        self.bench = CloseUp('duck', self)
        self.extend_children(self.objects)


class CloseUp(Location):
    '''
    Sublocation that is zoomed in on a specific object
    '''

    def __init__(self, name, parent_location):
        super().__init__(name, parent_location.parent)
        self.parent_location = parent_location

    def update(self, events: list):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Exiting")
                    self.parent.change_level(self.parent_location)
