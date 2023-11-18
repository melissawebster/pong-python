import pygame


class Obj:

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.move_up_bool = False
        self.move_down_bool = False

    def draw(self, window):
        window.blit(self.image, (self.rect[0], self.rect[1]))

    def move_up(self):
        if self.move_up_bool == True:
            self.rect[1] -= 8
            if self.rect[1] < 6:
                self.rect[1] = 6

    def move_down(self):
        if self.move_down_bool == True:
            self.rect[1] += 8
            if self.rect[1] > 566:
                self.rect[1] = 566
