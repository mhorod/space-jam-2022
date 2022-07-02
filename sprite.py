import pygame as pg
from pygame.locals import *

from vector import Vec2


class Sprite:
    def __init__(self, position, file_name, callback=lambda: None):
        self.is_clicked = False
        self.is_highlighted = False
        self.surface = pg.image.load(file_name).convert_alpha()
        self.position = position
        self.outline = self.calculate_outline()
        self.callback = callback

    def update(self, events):
        for event in events.mouse_events:
            if event.type == MOUSEBUTTONDOWN:
                self.on_mouse_down(event, events)
            elif event.type == MOUSEBUTTONUP:
                self.on_mouse_up(event, events)
            elif event.type == MOUSEMOTION:
                self.on_motion(event, events)

    def is_hovered(self, point):
        on_image = point - self.position
        if not self.surface.get_rect().collidepoint(on_image):  # Checks if point is within bounding box
            return False
        pixel = self.surface.get_at(on_image)
        alpha = pixel[3]
        return alpha != 0

    def on_mouse_down(self, event, events):
        on_screen = events.screen_to_world(Vec2.from_tuple(event.pos)).int()
        if self.is_hovered(on_screen):
            self.is_clicked = True
            self.callback()
        else:
            self.is_clicked = False

    def on_mouse_up(self, event, events):
        self.is_clicked = False

    def on_motion(self, event, events):
        on_screen = events.screen_to_world(Vec2.from_tuple(event.pos)).int()
        if self.is_hovered(on_screen):
            self.is_highlighted = True
        else:
            self.is_highlighted = False

    def draw(self, screen):
        if self.is_highlighted:
            screen.blit(self.outline, self.position)
        screen.blit(self.surface, self.position)

    def calculate_outline(self):
        mask = pg.mask.from_surface(self.surface)
        outline = mask.to_surface()
        outline.set_colorkey((0, 0, 0))
        offset = 2
        screen = pg.Surface(
            (self.surface.get_width() + offset * 2, self.surface.get_height() + offset * 2))
        screen.set_colorkey((0, 0, 0))
        screen.blit(outline, self.position + Vec2(offset, 0))
        screen.blit(outline, self.position + Vec2(-offset, 0))
        screen.blit(outline, self.position + Vec2(0, -offset))
        screen.blit(outline, self.position + Vec2(0, offset))
        return screen
