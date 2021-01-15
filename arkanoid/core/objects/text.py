import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self,
                 get_text_handler,
                 center_xy,
                 font_color=pygame.Color('black'),
                 font_name='Tahoma',
                 font_size=35,
                 font_is_bold=True):
        super().__init__()

        self.get_text_handler = get_text_handler
        self.center_xy = center_xy
        self.font_color = font_color
        self.font = pygame.font.SysFont(font_name, font_size, font_is_bold)

        self.update()


    def update(self):
        self.image = self.font.render(self.get_text_handler(), True, self.font_color).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.center_xy[0]
        self.rect.centery = self.center_xy[1]
