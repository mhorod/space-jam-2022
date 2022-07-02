import pygame as pg
from pygame.locals import *

from level import Level
from sprite import Sprite
from vector import Vec2

from assets import Assets

import copy


class Location(Level):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = self.load_image("background")
        self.sprites = {}
        self.close_ups = {}

    def load_image(self, object_name):
        return Assets.files[self.path(object_name)]

    def path(self, object_name):
        return f"assets/locations/{self.name}/{object_name}.png"

    def load_sprite(self, object_name, absolute_path=False):
        path = self.path(
            object_name) if not absolute_path else 'assets/' + object_name + '.png'
        sprite = Sprite(Vec2(0, 0), path)
        self.sprites[object_name] = sprite
        self.append_child(sprite)
        return sprite

    def load_sprites(self, names):
        return [self.load_sprite(name) for name in names]

    def load_closeups(self, names):
        for name in names:
            self.close_ups[name] = CloseUp(name, self)
            self.sprites[name].callback = (
                lambda n: lambda: self.parent.change_level(n))(copy.copy(name))


class CloseUp(Location):
    '''
    Sublocation that is zoomed in on a specific object
    '''

    def __init__(self, name, parent_location):
        super().__init__(name, parent_location.parent)
        self.back_arrow = self.load_sprite("ui/back_arrow", absolute_path=True)
        self.back_arrow.callback = lambda: parent_location.parent.change_level(
            parent_location)
