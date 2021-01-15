import pygame
from .stage import Stage


class Game:
    def __init__(self, window_caption, window_size):
        pygame.mixer.init(44100, -16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption(window_caption)
        pygame.mouse.set_visible(0)


    def get_stage(self, name=None):
        return None


    def run(self):
        stage = self.get_stage()
        if stage:
            stage.show()

            clock = pygame.time.Clock()
            while True:
                # Количество секунд, прошедших с последнего кадра
                time = clock.tick() / 1000.0
    
                running = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    stage.handle_event(event)

                if not running:
                    break

                next_stage = stage.update(time)
                if next_stage:
                    stage.hide()
                    stage = self.get_stage(next_stage.name)
                    if not stage:
                        # Вывод сообщения об ошибке: stage не найден.
                        break
                    stage.show(next_stage.params)
                    continue

                stage.draw(self.screen)

                pygame.display.update()
        else:
            # Вывод сообщения об ошибке: stage не выбран.
            pass

        pygame.quit()
    
