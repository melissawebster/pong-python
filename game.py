from window import Window
from obj import Obj

class Game:

    def __init__(self):
        self.window = Window(1280, 720, 'Pong Python')

        self.bg = Obj("assets/field.png", 0, 0)
        self.bg.draw(self.window.window)
        self.window.add_obj(self.bg)

        self.player1 = Obj("assets/player1.png", 50, 300)
        self.player1.draw(self.window.window)
        self.window.add_obj(self.player1)

        self.player2 = Obj("assets/player2.png", 1150, 300)
        self.player2.draw(self.window.window)
        self.window.add_obj(self.player2)
 
Game().window.update()