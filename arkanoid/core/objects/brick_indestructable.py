import pygame
from .brick import Brick


class IndestructibleBrick(Brick):
    def hit(self):
        pass

    def is_destroyed(self):
        return False
