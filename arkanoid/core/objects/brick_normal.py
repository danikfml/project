import pygame
from random import randrange
from arkanoid.config import DIR_RESOURCES_IMAGES
from .brick import Brick


class NormalBrick(Brick):
    _crack_mask = None
    _crack_mask_rect = None


    def __init__(self, topleft, brick_id):
        super().__init__(topleft, brick_id)

        self._health = 3

        if not(self.__class__._crack_mask):
            self.__class__._crack_mask = pygame.image.load(
                DIR_RESOURCES_IMAGES + r'crack_mask_01.png').convert()
            self.__class__._crack_mask.set_colorkey(self.__class__._crack_mask.get_at((0, 0)))
            self.__class__._crack_mask_rect = self.__class__._crack_mask.get_rect()


    def _reduce_health(self):
        if self._health > 0:
            self._health -= 1

            lefttop = (randrange(self.rect.width - self.__class__._crack_mask_rect.width, 0),
                       randrange(self.rect.height - self.__class__._crack_mask_rect.height, 0))
            self.image.blit(self.__class__._crack_mask, lefttop, special_flags=pygame.BLEND_MULT)


    def hit(self):
        self._reduce_health()


    def is_destroyed(self):
        return self._health == 0
