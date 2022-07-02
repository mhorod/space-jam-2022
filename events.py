import pygame as pg
from pygame.locals import *


class Events:
    def __init__(self, events, transform):
        self.events = events
        self.mouse_events = []
        self.key_events = []
        for event in events:
            if event.type in (MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION):
                self.mouse_events.append(event)
            elif event.type in (KEYDOWN, KEYUP):
                self.key_events.append(event)
        self.transform = transform

    def screen_to_world(self, point):
        return self.transform.inverse()(point)

    def __iter__(self):
        return iter(self.events)
