import pygame
import math, random
from arkanoid.config import DIR_RESOURCES_IMAGES


class Ball(pygame.sprite.Sprite):
    def __init__(self, area):
        super().__init__()

        self._speed_pps = 350
        self._area = area

        self.image = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'ball_01.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = self._area.center

        # Направление движения шарика (градусы).
        self._direction = 270
        self._topleft = list(self.rect.topleft)


    @property
    def is_dead(self):
        return self.rect.top >= self._area.bottom


    def bounce_horizontal(self, offset=0):
        if not self.is_dead:
            self._direction = (360 - self._direction + random.randint(-2, +2) - offset) % 360


    def bounce_vertical(self):
        if not self.is_dead:
            self._direction = (180 - self._direction + random.randint(-2, +2)) % 360


    def reset(self, paddle_rect):
        self.rect.centerx = paddle_rect.centerx
        self.rect.bottom = paddle_rect.top + 1
        self._direction = 270
        self._topleft = list(self.rect.topleft)


    def update(self, time):
        super().update()

        if self.is_dead:
            return

        direction = math.radians(self._direction)
        self._topleft[0] += self._speed_pps * time * math.cos(direction)
        self._topleft[1] += self._speed_pps * time * math.sin(direction)

        if self._topleft[1] <= self._area.top:
            self._topleft[1] = self._area.top + 1
            self.bounce_horizontal()

        if self._topleft[0] <= self._area.left:
            self._topleft[0] = self._area.left + 1
            self.bounce_vertical()

        if self._topleft[0] + self.rect.width > self._area.right:
            self._topleft[0] = self._area.right - self.rect.width - 1
            self.bounce_vertical()

        self.rect.topleft = self._topleft
