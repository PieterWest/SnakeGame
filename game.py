import pygame
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 800
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.home_screen = pygame.Surface((self.DISPLAY_W/2,self.DISPLAY_H/2))
        self.home_image = pygame.image.load('Graphics/HomeScreen.jpg')
        pygame.display.set_caption("Silly Snake")
        icon = pygame.image.load('Graphics/SnakeIcon1.png')
        pygame.display.set_icon(icon)
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.home = pygame.display.set_mode(((self.DISPLAY_W - 100,self.DISPLAY_H -100)))
        self.font_name = ('Font/bubblegum/Bubblegum.ttf')
        self.GREEN, self.BROWN = (175,215,70), (56, 74, 12)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.GREEN)
            self.draw_text('Thanks for Playing ', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.BROWN)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
