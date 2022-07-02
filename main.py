import pygame as pg
from pygame.locals import *

from vector import Vec2
from level import *

from transform import *
from events import Events
from locations import *
from assets import *
from inventory import Inventory

from game import Game
from game_view import GameView

INTERNAL_SIZE = (1920, 1080)


class HUD:
    def __init__(self, inventory):
        self.surface = pg.Surface(INTERNAL_SIZE).convert_alpha()
        self.open_inventory = Sprite(
            Vec2(0, 0), "assets/ui/open_inventory.png")
        self.inventory = inventory
        self.open_inventory.callback = lambda: self.inventory.toggle()
        self.shown = False

    def hide(self):
        self.shown = False

    def show(self):
        self.shown = True

    def draw(self, surface):
        if self.shown:
            self.surface.fill((0, 0, 0, 0))
            self.inventory.draw(self.surface)
            self.open_inventory.draw(self.surface)
            surface.blit(self.surface, (0, 0))

    def update(self, events):
        if self.shown:
            self.open_inventory.update(events)
            self.inventory.update(events)


class Window:
    def __init__(self, title):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), FULLSCREEN)
        pg.display.set_caption(title)
        self.load_assets()
        self.clock = pg.time.Clock()
        self.running = False

        self.root = LevelContainer()

        self.game = Game()

        self.inventory = Inventory(self.game)
        self.hud = HUD(self.inventory)
        self.hud.show()

        self.game_view = GameView(self.game, self.hud)

        self.root.change_level(MainMenu(self.root))

        self.game_surface = pg.Surface(INTERNAL_SIZE)

    def load_assets(self):
        w = self.screen.get_width() // 2
        h = 20
        x = (self.screen.get_width() - w) // 2

        def update_loading(done, total):
            self.screen.fill((20, 20, 20))
            percentage = done/total
            text = pg.font.SysFont("Arial", 100).render(
                f"Loading... {done}/{total}", True, (255, 255, 255))

            text_x = (self.screen.get_width() - text.get_width()) // 2
            text_y = (self.screen.get_height() - text.get_height()) // 2

            y = text_y + text.get_height() + h

            self.screen.blit(text, (text_x, text_y))
            pg.draw.rect(self.screen, (255, 255, 255), (x, y, w, h), 1)
            pg.draw.rect(self.screen, (40, 240, 60),
                         (x, y, int(w * percentage), h))
            pg.display.flip()

            pg.display.update()

        Assets.load_assets(update_loading)

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

        events = Events(events, self.current_transform())
        self.root.update(events)
        self.hud.update(events)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.game_surface.fill((0, 0, 0))

        self.root.draw(self.game_surface)
        self.hud.draw(self.game_surface)

        surface, pos = self.fit_surface(self.game_surface)
        self.screen.blit(surface, pos)
        pg.display.update()

    def fit_surface(self, surface):
        size, offset = self.fit_to(self.screen.get_size())
        surface = pg.transform.scale(surface, size)
        return surface, offset

    def fit_to(self, res):
        '''
        Scales internal resolution to fit the screen resolution without stretching.
        e.g. if screen is wider than internal resolution then height is fit and width is centered
        '''
        target_ratio = res[0]/res[1]
        ratio = INTERNAL_SIZE[0]/INTERNAL_SIZE[1]

        if target_ratio > ratio:
            height = res[1]
            width = height * ratio
            x = (res[0] - width) // 2
            y = 0
        else:
            width = res[0]
            height = width / ratio
            x = 0
            y = (res[1] - height) // 2
        return (int(width), int(height)), (int(x), int(y))

    def current_transform(self):
        '''
        Returns current transform matrix for internal resolution
        '''
        size, offset = self.fit_to(self.screen.get_size())
        scale = size[0]/INTERNAL_SIZE[0]
        return Transform([Scale(scale), Translate(Vec2(*offset))])

    def scale_pos(self, pos):
        '''
        Scales position from screen resolution to internal resolution
        '''
        x, y = pos
        size, offset = self.fit_to(self.screen.get_size())
        scale = INTERNAL_SIZE[0]/size[0]
        x = (x - offset[0]) * scale
        y = (y - offset[1]) * scale
        return int(x), int(y)


window = Window("Epic Game")
window.start()
