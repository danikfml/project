import pygame
from arkanoid.config import (
    DIR_RESOURCES_IMAGES, DIR_RESOURCES_SOUND)
from arkanoid.core.stage import Stage, NextStage


class IntroStage(Stage):
    def __init__(self):
        super().__init__()

        self.background = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'back_intro_01.jpg').convert()
        self.keydown_handlers[pygame.K_SPACE].append(self._handle)

        self._running = True


    def _handle(self, key):
        if key == pygame.K_SPACE:
            self._running = False


    def show(self, params=None):
        self._running = True
        pygame.mixer.music.load(
            DIR_RESOURCES_SOUND + r'snd_intro_outro.mp3')
        pygame.mixer.music.play(loops=-1)


    def hide(self):
        pygame.mixer.music.fadeout(500)


    def update(self, time):
        if not self._running:
            return NextStage('game', None)


    def draw(self, surface):
        surface.blit(self.background, (0, 0))

