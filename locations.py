from location import *
from memory import *
from animation import *
from use_result import *


class Garden(Location):
    def __init__(self):
        items = ['bench', 'duck', 'gate', 'path']
        locations = [Bench(), Duck()]
        super().__init__('garden', items, locations)


class Bench(Location):
    def __init__(self):
        items = []
        locations = []
        super().__init__('bench', items, locations)


class Duck(Location):
    def __init__(self):
        items = []
        locations = []
        super().__init__('duck', items, locations)

    def use_item(self, item):
        if item.name == 'bread':
            return TriggerMemory('pond_no_face')
        else:
            return Nothing()


class Kitchen(Location):
    def __init__(self):
        items = ["bin", "breadbox", "drawer", "fridge", "sink"]
        locations = []
        super().__init__('kitchen', items, locations)


class Bedroom(Location):
    def __init__(self):
        items = []
        locations = []
        super().__init__('bedroom', items, locations)


class MainMenu(LocationView):
    def __init__(self, parent):
        location = Location('main_menu', ['play', 'exit'], [])
        super().__init__(parent, location)
        self.sprites['play'].callback = lambda: (self.parent.change_level(
            'game'))
        self.sprites['exit'].callback = lambda: self.parent.quit()
