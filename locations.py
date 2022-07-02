from location import *
from memory import *
from animation import *
from use_result import *
from inventory import *


class Garden(Location):
    def __init__(self):
        objects = ['bench', 'duck', 'gate', 'path']
        locations = [Bench(), Duck()]
        super().__init__('garden', objects, locations)


class Bench(Location):
    def __init__(self):
        objects = []
        locations = []
        super().__init__('bench', objects, locations)


class Duck(Location):
    def __init__(self):
        objects = []
        locations = []
        super().__init__('duck', objects, locations)

    def use_item(self, item):
        if item.name == 'bread':
            return ComposedUseResult([TriggerMemory('pond_no_face'), ConsumeItem(item)])
        else:
            return Nothing()


class Bench(Location):
    def __init__(self):
        super().__init__('bench', items=[Item('crowbar')])


class Kitchen(Location):
    def __init__(self):
        objects = ["bin", "breadbox", "sink", "kitchen_drawer",
                   "freezer", "floorboards", "kitchen_doors"]
        locations = [KitchenDrawer(), Floorboards(), Freezer(), BreadBox()]
        super().__init__('kitchen', objects, locations)


class KitchenDrawer(Location):
    def __init__(self):
        super().__init__('kitchen_drawer', items=[Item('walkman')])


class Floorboards(Location):
    def __init__(self):
        super().__init__('floorboards', items=[
            Item('rings'), Item('key_floor')])


class Freezer(Location):
    def __init__(self):
        super().__init__('freezer', items=[Item('postit')])


class BreadBox(Location):
    def __init__(self):
        super().__init__('breadbox', items=[Item('bread')])


class Bedroom(Location):
    def __init__(self):
        objects = ['large_drawer']
        locations = [LargeDrawer()]
        super().__init__('bedroom', objects, locations)


class LargeDrawer(Location):
    def __init__(self):
        super().__init__('large_drawer', items=[Item('dress')])


class Bedroom(Location):
    def __init__(self):
        objects = ["large_drawer"]
        locations = [LargeDrawer()]
        super().__init__('bedroom', objects, locations)


class MainMenu(LocationView):
    def __init__(self, parent):
        location = Location('main_menu', ['play', 'exit'], [])
        super().__init__(parent, location)
        self.sprites['play'].callback = lambda: (self.parent.change_level(
            'game'))
        self.sprites['exit'].callback = lambda: self.parent.quit()
