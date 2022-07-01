import pygame
from pygame.locals import *

import pygame_widgets
from pygame_widgets.button import Button


class Window:
    def __init__(self, title):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), FULLSCREEN)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = False
        self.button = Button(
            # Mandatory Parameters
            self.screen,  # Surface to place button on
            100,  # X-coordinate of top left corner
            100,  # Y-coordinate of top left corner
            300,  # Width
            150,  # Height

            # Optional Parameters
            text='Hello',  # Text to display
            fontSize=50,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            # Colour of button when not being interacted with
            inactiveColour=(200, 50, 0),
            # Colour of button when being hovered over
            hoverColour=(150, 0, 0),
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: print('Click')  # Function to call when clicked on
        )

    def start(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.process_events()
            self.draw()

    def process_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                self.running = False
            elif event.type == VIDEORESIZE:
                print(event.dict)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

        self.screen.fill((0, 0, 0))
        pygame_widgets.update(events)

    def draw(self):
        pygame.display.update()


window = Window("Epic Game")
window.start()
