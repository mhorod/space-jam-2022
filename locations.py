from location import *


class Garden(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('garden', *args, **kwargs)
        self.objects = self.load_sprites(["bench", "duck", "gate", "path"])
        self.load_closeups(('duck', 'bench'))


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
    def __init__(self, *args, **kwargs):
        super().__init__('main_menu', *args, **kwargs)
        self.objects = self.load_sprites(["play", "exit"])
        self.sprites['play'].callback = lambda: self.parent.change_level(
            'game')
        self.sprites['exit'].callback = lambda: self.parent.quit()
