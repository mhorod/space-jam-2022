from vector import Vec2
from level import *
import pygame as pg
from pygame.locals import *
from game import Game
from transform import *
from events import Events
from locations import *

INTERNAL_SIZE = (1920, 1080)


class Window:
    def __init__(self, title):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), FULLSCREEN)
        pg.display.set_caption(title)
        self.draw_loading()
        self.clock = pg.time.Clock()
        self.running = False
        self.root = LevelContainer()
        self.game = Game(self.root)
        self.root.change_level(MainMenu(self.root))

    def draw_loading(self):
        self.screen.fill((0, 0, 0))
        surface = pg.Surface(INTERNAL_SIZE)
        surface.fill((0, 0, 0))
        text = pg.font.SysFont('Arial', 100).render(
            'Loading...', True, (255, 255, 255))
        surface.blit(text, (INTERNAL_SIZE[0]//2 - text.get_width() //
                     2, INTERNAL_SIZE[1]//2 - text.get_height()//2))
        surface, pos = self.fit_surface(surface)
        self.screen.blit(surface, pos)
        pg.display.update()

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

        self.root.update(Events(events, self.current_transform()))

    def draw(self):
        self.screen.fill((0, 0, 0))
        surface = pg.Surface(INTERNAL_SIZE)
        self.root.draw(surface)
        surface, pos = self.fit_surface(surface)
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
