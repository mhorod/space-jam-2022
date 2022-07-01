import pygame as pg
from vector import Vec2


class Sprite:
    def __init__(self, position, file_name):
        self.is_clicked = False
        self.is_highlighted = False
        self.initialize()
        self.surface = pg.image.load(file_name).convert_alpha()
        self.position = position

    def is_hovered(self, point):
        on_image = point - self.position
        if not self.surface.get_rect().collidepoint(on_image):  # Checks if point is within bounding box
            return False
        pixel = self.surface.get_at(on_image)
        alpha = pixel[3]
        return alpha != 0

    def on_mouse_down(self, event):
        on_screen = Vec2.from_tuple(event.pos)
        if self.is_hovered(on_screen):
            self.is_clicked = True
        else:
            self.is_clicked = False

    def on_mouse_up(self, event):
        self.is_clicked = False

    def on_motion(self, event):
        on_screen = Vec2.from_tuple(event.pos)
        if self.is_hovered(on_screen):
            self.is_highlighted = True
        else:
            self.is_highlighted = False

    def draw(self, screen):
        if self.is_highlighted:
            mask = pg.mask.from_surface(self.surface)
            outline = mask.to_surface()
            outline.set_colorkey((0, 0, 0))
            offset = 2
            screen.blit(outline, self.position + Vec2(offset, 0))
            screen.blit(outline, self.position + Vec2(-offset, 0))
            screen.blit(outline, self.position + Vec2(0, -offset))
            screen.blit(outline, self.position + Vec2(0, offset))

        screen.blit(self.surface, self.position)
