import pygame

class SungJinKen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super()._init_()
        self.image = pygame.image.load("Assets/KenSprite1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = 3

    def update(self):
        self.rect.x += self.speed_x # Horizonal Ken Movement

        # Reverse direction if hitting edges
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed_x *= -1