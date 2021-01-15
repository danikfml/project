import pygame
import random
from arkanoid.config import (
    DIR_RESOURCES_IMAGES, DIR_RESOURCES_SOUND
)
from arkanoid.core.stage import Stage, NextStage
from arkanoid.core.objects import (
    NormalBrick, IndestructibleBrick, Ball, Paddle, Level, Text
)


class GameStage(Stage):
    def __init__(self):
        super().__init__()

        self.background = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'back_game_01.jpg').convert()
        self.area = pygame.Rect(156, 26, 819, 648)

        self.game_over = False
        self.score = 0
        self.lives = 3

        self._create_paddle()


    def _create_paddle(self):
        self.paddle = Paddle(self.area)
        self.paddle_group = pygame.sprite.GroupSingle(self.paddle)
        self.keydown_handlers[pygame.K_LEFT].append(self.paddle.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(self.paddle.handle)
        self.keyup_handlers[pygame.K_LEFT].append(self.paddle.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(self.paddle.handle)


    def _create_bricks(self):
        self.bricks_group = Level(self.area)
        self.bricks_group.load_first()


    def _create_ball(self):
        self.ball = Ball(self.area)
        self.ball_group = pygame.sprite.GroupSingle(self.ball)


    def _create_panels(self):
        self.panels_group = pygame.sprite.Group((
            Text(lambda: f'{self.lives:0>2}', (77, 85)),
            Text(lambda: f'{self.score:0>4}', (1053, 85)),
            Text(lambda: f'{self.bricks_group.level_number:0>3}', (1053, 219))
        ))


    def _reset_paddle_position(self):
        self.paddle.reset()


    def _reset_ball_position(self):
        self.ball.reset(self.paddle.rect)


    def show(self, params=None):
        pygame.mixer.music.load(
            DIR_RESOURCES_SOUND + r'snd_game.mp3')
        pygame.mixer.music.play(loops=-1)

        self.game_over = False
        self.score = 0
        self.lives = 3

        self._create_bricks()
        self._create_ball()
        self._create_panels()

        self._reset_paddle_position()
        self._reset_ball_position()


    def hide(self):
        pygame.mixer.music.fadeout(500)


    def update(self, time):
        if self.game_over:
            return NextStage('outro', {
                'win': not(self.ball.is_dead),
                'score': self.score
            })

        self.paddle.update(time)
        self.ball.update(time)
        if self.ball.is_dead:
            self.lives -= 1
            self.game_over = self.lives == 0
            if not self.game_over:
                self._create_ball()
                self._reset_ball_position()

        if pygame.sprite.spritecollide(self.paddle, self.ball_group, False, collided=pygame.sprite.collide_mask):
            # Угол отскока зависит от удаления от середины ракетки точки соприкосновения шарика и ракетки.
            self.ball.bounce_horizontal(self.paddle.rect.centerx - self.ball.rect.centerx)

        # Проверка столкновения шарика с блоками.
        collided_bricks = pygame.sprite.spritecollide(self.ball, self.bricks_group, False)
        if len(collided_bricks) > 0:
            # Если шарик столкнулся с блоком, то меняем направление движения.
            self.ball.bounce_horizontal()
            # Удаляем блоки, участвовавшие в столкновении.
            for brick in collided_bricks:
                brick.hit()
                if brick.is_destroyed:
                    self.score += 1
                    brick.kill()
                    del brick

        if len(self.bricks_group) == self.bricks_group.indestructible_brick_count:
            try:
                self.bricks_group.load_next()
                self._reset_ball_position()
            except:
                self.game_over = True

        self.bricks_group.update()
        self.panels_group.update()


    def draw(self, surface):
        surface.blit(self.background, (0, 0))

        saved_rect = surface.get_clip()
        surface.set_clip(self.area)

        self.bricks_group.draw(surface)
        self.paddle_group.draw(surface)
        self.ball_group.draw(surface)

        surface.set_clip(saved_rect)

        self.panels_group.draw(surface)
