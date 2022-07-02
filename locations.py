from location import *
from memory import *
from animation import *


class Garden(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('garden', *args, **kwargs)
        self.objects = self.load_sprites(["bench", "duck", "gate", "path"])
        bench = Bench(self)
        self.sprites['bench'].callback = lambda: self.parent.change_level(
            'bench', TransitionAnimation.AnimEnum.swipe)

        self.sprites['path'].callback = lambda: self.parent.change_level(
            'kitchen', TransitionAnimation.AnimEnum.swipe
        )

        memory = Memory('pond_no_face', self)
        self.sprites['duck'].callback = lambda: (
            memory.start(), self.parent.change_level(memory, TransitionAnimation.AnimEnum.fade))


class Bench(CloseUp):
    def __init__(self, *args, **kwargs):
        super().__init__('bench', *args, **kwargs)
        self.crowbar = self.load_sprite(
            "items/crowbar", absolute_path=True)
        self.crowbar.callback = lambda: print("")  # TODO


class Kitchen(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('kitchen', *args, **kwargs)
        self.objects = self.load_sprites(
            ["bin", "breadbox", "fridge", "sink", "kitchen_doors", "freezer", "floorboards"])
        self.load_closeups(('bin', 'sink'))

        freezer = Freezer(self)
        self.sprites['freezer'].callback = lambda: self.parent.change_level(
            'freezer', TransitionAnimation.AnimEnum.swipe)

        breadbox = BreadBox(self)
        self.sprites['breadbox'].callback = lambda: self.parent.change_level(
            'breadbox', TransitionAnimation.AnimEnum.swipe)

        floorboards = Floorboards(self)
        self.sprites['floorboards'].callback = lambda: self.parent.change_level(
            'floorboards', TransitionAnimation.AnimEnum.swipe)

        kitchen_drawer = KitchenDrawer(self)
        self.sprites['kitchen_drawer'].callback = lambda: self.parent.change_level(
            'kitchen_drawer', TransitionAnimation.AnimEnum.swipe)

        self.sprites['kitchen_doors'].callback = lambda: self.parent.change_level(
            'garden', TransitionAnimation.AnimEnum.swipe)


class KitchenDrawer(CloseUp):
    def __init__(self, *args, **kwargs):
        super().__init__('kitchen_drawer', *args, **kwargs)
        self.walkman = self.load_sprite(
            "items/walkman", absolute_path=True)
        self.walkman.callback = lambda: print("")  # TODO


class Floorboards(CloseUp):
    def __init__(self, *args, **kwargs):
        super().__init__('floorboards', *args, **kwargs)
        self.rings = self.load_sprite(
            "items/rings", absolute_path=True)
        self.rings.callback = lambda: print("")  # TODO
        self.key = self.load_sprite(
            "items/key_floor", absolute_path=True)
        self.key.callback = lambda: print("")  # TODO


class Freezer(CloseUp):
    def __init__(self, *args, **kwargs):
        super().__init__('freezer', *args, **kwargs)
        self.postit = self.load_sprite(
            "items/postit", absolute_path=True)
        self.postit.callback = lambda: print("")  # TODO


class BreadBox(CloseUp):
    def __init__(self, *args, **kwargs):
        super().__init__('breadbox', *args, **kwargs)
        self.bread = self.load_sprite(
            "items/bread", absolute_path=True)
        self.bread.callback = lambda: print("")  # TODO


class Bedroom(Location):
    def __init__(self, *args, **kwargs):
        super().__init__('bedroom', *args, **kwargs)
        self.objects = self.load_sprites(["large_drawer"])

        large_drawer = LargeDrawer(self)
        self.sprites['large_drawer'].callback = lambda: self.parent.change_level(
            'large_drawer', TransitionAnimation.AnimEnum.swipe)


class LargeDrawer(CloseUp):
    def __init__(self, *args, **kwargs):
        super().__init__('large_drawer', *args, **kwargs)
        self.dress = self.load_sprite("items/dress", absolute_path=True)
        self.dress.callback = lambda: print("")  # TODO


class MainMenu(Location):
    def __init__(self, hud, *args, **kwargs):
        super().__init__('main_menu', *args, **kwargs)
        self.objects = self.load_sprites(["play", "exit"])
        self.sprites['play'].callback = lambda: (hud.show(), self.parent.change_level(
            'game'))
        self.sprites['exit'].callback = lambda: self.parent.quit()
