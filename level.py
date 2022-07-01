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


class Button(Drawable):
    def __init__(self, x, y, width, height, text, callback=lambda: None):
        self.surface = pg.Surface((width, height))
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.pos = (x, y)
        self.callback = callback

    def draw(self, target: pg.Surface):
        font = pg.font.SysFont('Arial', 40)
        text = font.render(self.text, True, (255, 255, 255))
        text_pos = (self.surface.get_width() // 2 - text.get_width() //
                    2, self.surface.get_height() // 2 - text.get_height() // 2)
        self.surface.blit(text, text_pos)
        target.blit(self.surface, self.pos)

    def update(self, events: list):
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == BUTTON_LEFT:
                    if self.rect.collidepoint(event.pos):
                        self.callback()


class MainMenu(Level):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = pg.Surface((0, 0))
        self.play_button = Button(
            100, 100, 100, 50, 'Play', lambda: self.parent.change_level('game'))
        self.append_child(self.play_button)
