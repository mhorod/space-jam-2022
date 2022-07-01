import pygame as pg
from pygame.locals import *

from vector import Vec2


class Sprite:
    def __init__(self, position: Vec2, surface, callback=lambda: None):
        self.position = position
        self.surface = surface
        self.callback = callback

    def from_file(position: Vec2, file_name, callback=lambda: None):
        surface = pg.image.load(file_name).convert_alpha()
        position = position
        return Sprite(position, surface, callback)

    def draw(self, screen):
        screen.blit(self.surface, self.position)

    def update(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                self.on_click(event)

    def is_clicked(self, on_screen):
        on_image = on_screen - self.position
        if not self.surface.get_rect().collidepoint(on_image):
            return False

        pixel = self.surface.get_at(on_image)
        alpha = pixel[3]
        if alpha == 0:
            return False

        return True

    def on_click(self, event):
        on_screen = Vec2.from_tuple(event.pos)
        if self.is_clicked(on_screen):
            self.callback()
