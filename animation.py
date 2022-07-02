import pygame as pg
from vector import Vec2
from math import floor
from enum import Enum

# UWAGA: Najgorszy kod pytongowy jaki w życiu wiedzieliście
# Nie dotykać i z szacunku do autora proszę nie oglądać

INTERNAL_SIZE = (1920, 1080)


class TransitionAnimation:
    class AnimEnum:
        no_anim = None
        fade = 0
        swipe = 1

    def __init__(self, image_list, total_frames, stride, start_pos, end_pos, fade=False, follow_color=(0, 0, 0, 0)):
        self.surfaces = [img.convert_alpha() for img in image_list]
        self.total_frames = total_frames
        self.curr_frame = 0
        self.stride = stride
        self.is_animating = False

        self.follow_surface = pg.Surface(INTERNAL_SIZE)
        self.follow_surface.fill(follow_color)
        self.follow_surface.set_alpha(follow_color[3])

        self.position = start_pos
        self.fade = fade
        if fade:
            self.alpha = 0
        else:
            self.alpha = 255

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.called = False

    def load_animations():
        return [
            TransitionAnimation(
                [pg.image.load("assets/transitions/t1.png")],
                20,
                3,
                Vec2(0, 0), Vec2(0, 0), True, (0, 0, 0, 0)
            ),
            TransitionAnimation(
                [
                    pg.image.load("assets/transitions/r1.png"),
                    pg.image.load("assets/transitions/r2.png"),
                    pg.image.load("assets/transitions/r3.png")
                ],
                10,
                2,
                Vec2(0, 0), Vec2(1920, 0), False, (0, 0, 0, 255)
            )
        ]

    def start(self, level, callback):
        self.callback = callback
        self.level = level
        self.is_animating = True

    def stop(self):
        self.curr_frame = 0
        self.is_animating = False

    def update_animation(self):
        if self.curr_frame > self.total_frames:
            if not self.fade and not self.called:
                self.callback(self.level)
            self.stop()
        self.curr_frame += 1

        if self.curr_frame >= self.total_frames // 2 and self.fade and not self.called:
            self.callback(self.level)
            called = True
        time = self.curr_frame / self.total_frames
        self.position = (self.end_pos - self.start_pos) * time

        if self.fade:
            self.alpha = 255 - 510 * abs(time - 0.5)

    def draw(self, surface):
        index = (floor(self.curr_frame / self.stride) + 1) % len(self.surfaces)
        self.follow_surface.set_alpha(self.alpha)
        self.surfaces[index].set_alpha(self.alpha)
        surface.blit(self.follow_surface, self.position -
                     Vec2(INTERNAL_SIZE[0], 0))
        surface.blit(
            self.surfaces[index], self.position)
