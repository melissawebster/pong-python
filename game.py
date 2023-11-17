import pygame
from obj import Obj


class Display:

    def __init__(self, size_x, size_y, title):
        self.window = pygame.display.set_mode([size_x, size_y])
        self.title = pygame.display.set_caption(title)


class Game:

    def __init__(self):
        pygame.init()
        self.running = True
        self.window = Display(1280, 720, 'Pong Python')

        self.bg = Obj("assets/field.png", 0, 0)
        self.player1 = Obj("assets/player1.png", 50, 300)
        self.player2 = Obj("assets/player2.png", 1150, 300)
        self.ball = Obj("assets/ball.png", 616, 340)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.player1.move_up()
                if event.key == pygame.K_a:
                    self.player1.move_down()
    
    def update(self):
        while self.running:
            self.events()

            #Obj draws
            self.bg.draw(self.window.window)
            self.player1.draw(self.window.window)
            self.player2.draw(self.window.window)
            self.ball.draw(self.window.window)

            pygame.display.update()
 

    def move_player1_up(self):
        self.player1.rect[1] -= 8

Game().update()