import pygame as pg
from pygame.locals import *

import pygame_widgets as pgw
from pygame_widgets.button import Button

from sprite import Sprite
from vector import Vec2


class Window:
    def __init__(self, title):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), FULLSCREEN)
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = False
        self.spr = Sprite.from_file(
            Vec2(100, 100), "assets/main_char.png")  # TODO: Delete

    def start(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.process_events()
            self.draw()

    def process_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == QUIT:
                self.running = False
            elif event.type == VIDEORESIZE:
                print(event.dict)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.spr.on_click(event)  # TODO: Delete
        self.screen.fill((50, 50, 50))
        pgw.update(events)

    def draw(self):
        self.spr.draw(self.screen)  # TODO: Delete
        pg.display.update()


window = Window("Epic Game")
window.start()
