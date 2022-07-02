from location import *
from memory import *
from animation import *


class Garden(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('garden', *args, **kwargs)
        self.objects = self.load_sprites(["bench", "duck", "gate", "path"])
        self.load_closeups(('bench',))
        memory = Memory('pond_no_face', self)
        self.sprites['duck'].callback = lambda: (
            memory.start(), self.parent.change_level(memory, TransitionAnimation.AnimEnum.fade))


class Kitchen(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('kitchen', *args, **kwargs)
        self.objects = self.load_sprites(
            ["bin", "breadbox", "drawer", "fridge", "sink"])
        self.load_closeups(('bin', 'breadbox', 'drawer', 'sink'))


class Bedroom(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('bedroom', *args, **kwargs)


class MainMenu(Location):
    def __init__(self, hud, *args, **kwargs):
        super().__init__('main_menu', *args, **kwargs)
        self.objects = self.load_sprites(["play", "exit"])
        self.sprites['play'].callback = lambda: (hud.show(), self.parent.change_level(
            'game'))
        self.sprites['exit'].callback = lambda: self.parent.quit()
