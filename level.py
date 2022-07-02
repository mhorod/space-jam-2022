import pygame as pg
from pygame.locals import *


class Drawable:
    def draw(self, surface: pg.Surface):
        pass

    def update(self, events: list):
        pass


class Levels:
    levels = {}

    def add(name, level):
        if name in Levels.levels:
            raise ValueError(f"Level with name '{name}' already exists")
        else:
            Levels.levels[name] = level


class LevelContainer(Drawable):
    def __init__(self):
        self.level = None

    def change_level(self, level):
        if type(level) == str:
            level = Levels.levels[level]
        self.level = level

    def draw(self, surface):
        if self.level:
            self.level.draw(surface)

    def update(self, events):
        if self.level:
            self.level.update(events)

    def quit(self):
        pg.quit()
        quit()


class Level(Drawable):
    def __init__(self, name, parent: LevelContainer):
        self.name = name
        Levels.add(name, self)

        self.parent = parent
        self.background: pg.Surface = None
        self.objects = []

    def exit(self):
        self.parent.change_level(None)

    def append_child(self, child):
        self.objects.append(child)

    def extend_children(self, children):
        self.objects.extend(children)

    def draw(self, target: pg.Surface):
        if self.background:
            target.blit(self.background, (0, 0))
        for obj in self.objects:
            obj.draw(target)

    def update(self, events: list):
        for obj in self.objects:
            obj.update(events)
