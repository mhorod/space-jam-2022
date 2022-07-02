import pygame as pg
from assets import Assets
from sprite import Sprite
from vector import Vec2
from transform import *


class Item(Sprite):
    def __init__(self, name):
        super().__init__(Vec2(0, 0), Item.path(name))
        self._surface = self.surface.copy()
        self.name = name

    def path(name):
        return f"assets/items/{name}.png"

    def take_from_inventory(self):
        w, h = self.surface.get_size()
        x = (1920 - w) // 2
        y = (1080 - h) // 2
        self.position = Vec2(x, y)
        pass

    def put_into_inventory(self):
        w, h = self.surface.get_size()
        S = 200
        if w >= h:
            w, h = S, S * h // w
        else:
            w, h = S * w // h, S

        self.surface = pg.transform.scale(self.surface, (w, h))
        self.recalculate_outline()


class Inventory:
    def __init__(self, game):
        self.game = game
        self.game.inventory = self

        self.items = []
        self.is_open = False
        self.surface = Assets.files["assets/ui/inventory.png"]
        self.item_surface = pg.Surface((500, 1080)).convert_alpha()

    def add_item(self, item):
        item.put_into_inventory()
        index = len(self.items)
        y = (index // 2) * 200 + 100
        x = (index % 2) * 200 + 100
        item.position = Vec2(x, y)
        item.callback = lambda: self.game.use_item(item)
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
        print(self.items, item)

    def place_items(self):
        for index, item in enumerate(self.items):
            index = len(self.items)
            y = (index // 2) * 200 + 100
            x = (index % 2) * 200 + 100
            item.position = Vec2(x, y)

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
                item.draw(self.item_surface)

            target.blit(self.item_surface, (1420, 0))

    def toggle(self):
        self.is_open = not self.is_open
