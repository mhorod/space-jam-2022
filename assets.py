import os
import pygame as pg


class Assets:
    files = {}

    def load_assets(callback):
        files_to_load = []
        for root, _, files in os.walk("assets"):
            for name in files:
                files_to_load.append(os.path.join(root, name))

        for index, file in enumerate(files_to_load):
            Assets.files[file] = pg.image.load(file).convert_alpha()
            callback(index, len(files_to_load))
