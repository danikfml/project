import pygame
from enum import Enum
from arkanoid.config import (
    DIR_RESOURCES_IMAGES, DIR_RESOURCES_SOUND)
from arkanoid.core.stage import Stage, NextStage


_OutroStageState = Enum('State', 'Current Game Quit')


class OutroStage(Stage):
    def __init__(self):
        super().__init__()

        self.background_w = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'back_outro_w01.jpg').convert()
        self.background_l = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'back_outro_l01.jpg').convert()

        self.keydown_handlers[pygame.K_SPACE].append(self._handle)
        self.keydown_handlers[pygame.K_ESCAPE].append(self._handle)

        self.font = pygame.font.Font(None, 150)

        self._win = True
        self._score = 0
        self._state = _OutroStageState.Current


    def _handle(self, key):
        if key == pygame.K_SPACE:
            self._state = _OutroStageState.Game
        elif key == pygame.K_ESCAPE:
            self._state = _OutroStageState.Quit


    def show(self, params=None):
        if not params:
            pass

        self._state = _OutroStageState.Current
        self._win = params.get('win', True)
        self._score = params.get('score', 0)

        pygame.mixer.music.load(
            DIR_RESOURCES_SOUND + r'snd_intro_outro.mp3')
        pygame.mixer.music.play(loops=-1)


    def hide(self):
        pygame.mixer.music.fadeout(500)


    def update(self, time):
        if self._state == _OutroStageState.Game:
            return NextStage('game', None)
        elif self._state == _OutroStageState.Quit:
            return NextStage('quit', None)


    def draw(self, surface):
        score_surface = self.font.render(str(self._score), True, pygame.Color('red'))
        score_position = score_surface.get_rect()

        if self._win:
            surface.blit(self.background_w, (0, 0))
            score_position.centerx = 375
            score_position.centery = 220
        else:
            surface.blit(self.background_l, (0, 0))
            score_position.centerx = 755
            score_position.centery = 230

        surface.blit(score_surface, score_position)
