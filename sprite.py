from this import d
import pygame as pg
from vector import Vec2


class Sprite:
    def from_color(position: Vec2, size, color):
        sprite = Sprite()
        sprite.surface = pg.surface.Surface(size)
        sprite.surface.fill(color)
        sprite.position = position
        return sprite

    def from_file(position: Vec2, file_name):
        sprite = Sprite()
        sprite.surface = pg.image.load(file_name).convert_alpha()
        sprite.position = position
        return sprite

    def draw(self, screen):
        screen.blit(self.surface, self.position)

    def update(self):
        pass

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
        if self.is_clicked(self, on_screen):
            pass
