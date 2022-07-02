import pygame as pg
from pygame.locals import *

from level import Level
from sprite import Sprite
from vector import Vec2

from assets import Assets

import copy

from use_result import *


class Location:
    '''
    Logical part of the location - represents an area where things can be
    '''

    def __init__(self, name, objects=None, locations=None, items=None, doors=[]):
        self.name = name
        self.objects = objects or []
        self.items = items or []
        self.locations = locations or []
        self.doors = doors or []
        self.view = None

    def take_item(self, item):
        '''
        Take item from this location
        '''
        return Nothing()

    def use_item(self, item):
        '''
        Use item in this location
        '''
        return Nothing()


class LocationView(Level):
    '''
    Graphical part of location that can be drawn on the screen
    '''

    def __init__(self, parent, location: Location):
        super().__init__(location.name, parent)
        self.background = self.load_image("background")
        self.sprites = {}
        self.close_ups = {}
        self.location = location
        self.objects = self.load_sprites(location.objects)
        self.load_closeups(location.locations)
        self.connect_doors(location.doors)

        location.view = self

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

    def load_closeups(self, locations):
        for location in locations:
            self.close_ups[location.name] = CloseUp(self, location)
            self.sprites[location.name].callback =\
                (lambda l: lambda: self.parent.game.change_location(l))(location)

    def connect_doors(self, doors):
        for name, dest in doors:
            self.sprites[name].callback = lambda: self.parent.game.change_location(
                dest)


class CloseUp(LocationView):
    '''
    Sublocation that is zoomed in on a specific object
    '''

    def __init__(self, parent_location, location):
        super().__init__(parent_location.parent, location)
        self.back_arrow = self.load_sprite("ui/back_arrow", absolute_path=True)
        self.back_arrow.callback = lambda: parent_location.parent.change_level(
            parent_location)
