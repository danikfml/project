import pygame
from arkanoid.config import DIR_RESOURCES_IMAGES


class Paddle(pygame.sprite.Sprite):
    def __init__(self, area):
        super().__init__()

        self._area = area

        self.image = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'paddle_01.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = self._area.centerx
        self.rect.bottom = self._area.bottom - 1

        self._moving_left = False
        self._moving_right = False
        self._speed_pps = 400.0
        self._left = self.rect.left


    def reset(self):
        self.rect.centerx = self._area.centerx
        self.rect.bottom = self._area.bottom - 1
        self._left = self.rect.left


    def update(self, time):
        super().update()

        offset = self._speed_pps * time
        if self._moving_left:
            self._left -= offset
            if self._left < self._area.left:
                self._left = self._area.left + 1
        elif self._moving_right:
            self._left += offset
            if self._left + self.rect.width > self._area.right:
                self._left = self._area.right - self.rect.width + 1

        self.rect.left = self._left


    def handle(self, key):
        if key == pygame.K_LEFT:
            self._moving_left = not self._moving_left
            self._moving_right = False
        elif key == pygame.K_RIGHT:
            self._moving_right = not self._moving_right
            self._moving_left = False
