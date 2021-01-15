from arkanoid.core.game import Game
from arkanoid import IntroStage, GameStage, OutroStage


class Arkanoid(Game):
    def __init__(self):
        super().__init__('Арканоид', (1130, 700))

        self._stages = {
            'intro': IntroStage(),
            'game': GameStage(),
            'outro': OutroStage(),
            'quit': None
        }


    def get_stage(self, name=None):
        if not name:
            name = 'intro'

        return self._stages.get(name, None)
