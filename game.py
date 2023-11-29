import pygame


class Display:

    def __init__(self, size_x, size_y, title):
        self.window = pygame.display.set_mode([size_x, size_y])
        self.title = pygame.display.set_caption(title)

class Obj:

    def __init__(self, image, x, y, game):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

        self.game = game
        self.move_player_up_bool = False
        self.move_player_down_bool = False
        self.ball_dir_x = -3
        self.ball_dir_y = -1

    def draw(self, window):
        window.blit(self.image, (self.rect[0], self.rect[1]))

    def move_player_up(self):
        if self.move_player_up_bool == True:
            self.rect[1] -= 8
            if self.rect[1] < 6:
                self.rect[1] = 6

    def move_player_down(self):
        if self.move_player_down_bool == True:
            self.rect[1] += 8
            if self.rect[1] > 566:
                self.rect[1] = 566

    def move_ball(self):
        self.rect[0] += self.ball_dir_x
        self.rect[1] += self.ball_dir_y
        #ball hits player and switches position
        if self.rect[0] < 80:
            if self.game.player1.rect[1] < self.rect[1] + 23 and self.game.player1.rect[1] + 146 > self.rect[1]:
                self.ball_dir_x *= -1
            else:
                pass #call score function
        if self.rect[0] > 1110:
            if self.game.player2.rect[1] < self.rect[1] + 23 and self.game.player2.rect[1] + 146 > self.rect[1]:
                self.ball_dir_x *= -1
            else:
                pass #call score function
        #ball hits top/bottom and switches position
        if self.rect[1] < 0 or self.rect[1] > 674:
            self.ball_dir_y *= -1

class Game:

    def __init__(self):
        pygame.init()
        self.running = True
        self.window = Display(1280, 720, 'Pong Python')

        self.bg = Obj("assets/field.png", 0, 0, self)
        self.player1 = Obj("assets/player1.png", 50, 300, self)
        self.player2 = Obj("assets/player2.png", 1150, 300, self)
        self.ball = Obj("assets/ball.png", 616, 340, self)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                #Player1
                if event.key == pygame.K_q:
                    self.player1.move_player_up_bool = True
                    self.player1.move_player_up()
                if event.key == pygame.K_a:
                    self.player1.move_player_down_bool = True
                    self.player1.move_player_down()
                #Player2
                if event.key == pygame.K_UP:
                    self.player2.move_player_up_bool = True
                    self.player2.move_player_up()
                if event.key == pygame.K_DOWN:
                    self.player2.move_player_down_bool = True
                    self.player2.move_player_down()
            
            if event.type == pygame.KEYUP:
                #Player1
                if event.key == pygame.K_q:
                    self.player1.move_player_up_bool = False
                if event.key == pygame.K_a:
                    self.player1.move_player_down_bool = False
                #Player2
                if event.key == pygame.K_UP:
                    self.player2.move_player_up_bool = False
                if event.key == pygame.K_DOWN:
                    self.player2.move_player_down_bool = False

    
    def update(self):
        while self.running:
            self.events()

            #Obj draws
            self.bg.draw(self.window.window)

            self.player1.draw(self.window.window)
            self.player1.move_player_up()
            self.player1.move_player_down()

            self.player2.draw(self.window.window)
            self.player2.move_player_up()
            self.player2.move_player_down()

            self.ball.draw(self.window.window)
            self.ball.move_ball()

            pygame.display.update()
 

Game().update()