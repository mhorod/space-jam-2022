import pygame as pg
from assets import Assets
from sprite import Sprite
from vector import Vec2
from transform import *


class Item(Sprite):
    def __init__(self, name, position):
        super().__init__(position, Item.path(name))
        w, h = self.surface.get_size()
        S = 200
        if w >= h:
            w, h = S, S * h // w
        else:
            w, h = S * w // h, S

        self.surface = pg.transform.scale(self.surface, (w, h))
        self.recalculate_outline()
        self.name = name

    def path(name):
        return f"assets/items/{name}.png"


class Inventory:
    def __init__(self):
        self.items = [Item('bread', Vec2(0, 0)), Item(
            'dress', Vec2(0, 0)), Item('key', Vec2(0, 0))]
        self.is_open = False
        self.surface = Assets.files["assets/ui/inventory.png"]
        self.item_surface = pg.Surface((500, 1080)).convert_alpha()

    def update(self, events):
        transform = Transform([Translate(Vec2(1420, 0))])
        events.transform = transform.and_then(events.transform)
        for item in self.items:
            item.update(events)

    def draw(self, target):
        if self.is_open:
            target.blit(self.surface, (0, 0))
            self.item_surface.fill((0, 0, 0, 0))

            for index, item in enumerate(self.items):
                y = (index // 2) * 200 + 100
                x = (index % 2) * 200 + 100
                item.position = Vec2(x, y)
                item.draw(self.item_surface)

            target.blit(self.item_surface, (1420, 0))

    def toggle(self):
        self.is_open = not self.is_open
