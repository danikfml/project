import pygame
from arkanoid.config import DIR_RESOURCES_IMAGES


# TODO Не должны создаваться экземпляры класса.
class Brick(pygame.sprite.Sprite):
    def __init__(self, topleft, brick_id):
        super().__init__()

        self.image = pygame.image.load(self._get_image_filename(brick_id)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self._destroyed = False


    @staticmethod
    def _get_image_filename(brick_id):
        return DIR_RESOURCES_IMAGES + f'brick_{brick_id:0>2}.png'


    def hit(self):
        self._destroyed = True


    @property
    def is_destroyed(self):
        return self._destroyed
