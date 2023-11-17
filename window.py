import pygame

class Window:

    def __init__(self, size_x, size_y, title):
        pygame.init()
        self.window = pygame.display.set_mode([size_x, size_y])
        self.title = pygame.display.set_caption(title)
        self.running = True
        self.draw_obj_list = []

    def add_obj(self, item):
        self.draw_obj_list.append(item)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        while self.running:
            self.events()
            pygame.display.update()
