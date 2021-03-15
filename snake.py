import pygame, sys, random
from pygame.math import Vector2
from menu import *
from game import Game

g = Game()

class SNAKE():
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block_apple = False
        self.new_block_mouse = False

        self.head_up = pygame.image.load('Graphics/SnakeHeadUp3.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/SnakeHeadDown3.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/SnakeHeadRight3.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/SnakeHeadLeft3.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/SnakeTailDown3.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/SnakeTailUp3.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/SnakeTailLeft3.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/SnakeTailRight3.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/SnakeBodyVertical3.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/SnakeBodyHorizontal3.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/SnakeTurnDownRight3.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/SnakeTurnDownLeft3.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/SnakeTurnUpRight3.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/SnakeTurnUpLeft3.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('Sound/apple.wav')
        self.crunch_mouse = pygame.mixer.Sound('Sound/mouse.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): 
            self.head = self.head_left
        elif head_relation == Vector2(-1,0): 
            self.head = self.head_right
        elif head_relation == Vector2(0,1): 
            self.head = self.head_up
        elif head_relation == Vector2(0,-1): 
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): 
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): 
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): 
            self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): 
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block_apple == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block_apple = False
        elif self.new_block_mouse == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0]+ self.direction)
            body_copy.insert(0, body_copy[0]+ self.direction)
            self.body = body_copy[:]
            self.new_block_mouse = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block_apple(self):
        self.new_block_apple = True

    def add_block_mouse(self):
        self.new_block_mouse = True

    def play_apple_crunch_sound(self):
        self.crunch_sound.play()

    def play_mouse_crunch_sound(self):
        self.crunch_mouse.play()

    def reset_wall(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        
    def reset_self(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT():
    def __init__(self):        
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MOUSE():
    def __init__(self):        
        self.randomize()

    def draw_mouse(self):
        mouse_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(mouse, mouse_rect)
        
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

        
class MAIN():
    def __init__(self):           
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.mouse = MOUSE()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()               

    def draw_elements(self):                     
        self.draw_grass()
        self.fruit.draw_fruit()    
        self.snake.draw_snake()
        self.mouse.draw_mouse()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block_apple()
            self.snake.play_apple_crunch_sound()
        elif self.mouse.pos == self.snake.body[0]:
            self.mouse.randomize()
            self.snake.add_block_mouse()
            self.snake.play_mouse_crunch_sound()
            
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            elif block == self.mouse.pos:
                self.mouse.randomize()
            

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over_wall()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over_self()

    def game_over_self(self):
        self.snake.reset_self()
        
    def game_over_wall(self):
        self.snake.reset_wall()
       
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = 'Score ' + str((len(self.snake.body) - 3) * 10) 
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 80)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)

    def game_loop(self):
        while g.playing:
            # draw game elements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    main_game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if main_game.snake.direction.y != 1:
                            main_game.snake.direction = Vector2(0, -1)
                    elif event.key == pygame.K_DOWN:
                        if main_game.snake.direction.y != -1:
                            main_game.snake.direction = Vector2(0, 1)
                    elif event.key == pygame.K_RIGHT:
                        if main_game.snake.direction.x != -1:
                            main_game.snake.direction = Vector2(1, 0)
                    elif event.key == pygame.K_LEFT:
                        if main_game.snake.direction.x != 1:
                            main_game.snake.direction = Vector2(-1, 0)

            screen.fill((175, 215, 70))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)
   
    

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple7.png').convert_alpha()
mouse = pygame.image.load('Graphics/mouse3.png').convert_alpha()
game_font = pygame.font.Font('Font/bubblegum/Bubblegum.ttf', 25)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while g.running:
    g.curr_menu.display_menu()
    main_game.game_loop()