
from locations import *


class Game:
    '''
    Logical game - manages interaction between world objects
    '''

    def __init__(self):
        self.inventory = None
        self.location = None
        self.view = None
        self.locations = [Bedroom(), Garden(), Kitchen()]

    def take_item(self, item):
        self.location.take_item(item)
        self.inventory.add_item(item)

    def use_item(self, item):
        result = self.location.use_item(item)
        result.apply(self)

    def change_location(self, location):
        self.location = location
        self.view.change_location(location)

    def trigger_memory(self, memory_name):
        self.view.trigger_memory(memory_name)

    def start(self):
        self.change_location(self.locations[0])
