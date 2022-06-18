import random
import pygame
import sys
from snake import Snake


class Field:
    def __init__(self, snake: Snake):
        pygame.init()

        self.snake = snake

        self.size = self.w, self.h = (300, 300)
        self.text_size = 32

        self.field_color = (255, 255, 255)  # white
        self.food_color = (0, 0, 255)  # blue
        self.counter_color = (120, 0, 80)  # purple

        self.clock = pygame.time.Clock()
        self.fps_increment = 0.1  # SPEED

        self.screen = pygame.display.set_mode(self.size)

        self.fps = None  # snake_speed
        self.score = None

        self.game_run = None
        self.game_close = None

        self.food_x = None
        self.food_y = None

        self.coord_list = None

    def text_overlay(self):
        text = pygame.font.SysFont(None, self.text_size)
        game_score = text.render(f'Your score: {self.score}', True, self.counter_color)
        rect = game_score.get_rect()
        self.screen.blit(game_score, rect)
        pygame.display.update()

    def end_text(self, first, second, third, fourth):
        text = pygame.font.SysFont(None, self.text_size)
        first_txt = text.render(first, True, self.counter_color)
        self.screen.blit(first_txt, (70, 100))
        second_txt = text.render(second, True, self.counter_color)
        self.screen.blit(second_txt, (70, 120))
        third_txt = text.render(third, True, self.counter_color)
        self.screen.blit(third_txt, (70, 140))
        fourth_txt = text.render(fourth, True, self.counter_color)
        self.screen.blit(fourth_txt, (70, 160))
        pygame.display.update()

    def eat(self):
        if self.snake.x == self.food_x and self.snake.y == self.food_y:
            self.food_x = random.randrange(0, self.w, self.snake.snake_cell)
            self.food_y = random.randrange(0, self.h, self.snake.snake_cell)
            self.score += 1
            self.snake.size += self.snake.eat_inc
            self.fps += self.fps_increment

    def menu(self):
        self.screen.fill(self.field_color)
        text = pygame.font.SysFont(None, self.text_size)
        first_txt = text.render('Press S to start', True, self.counter_color)
        self.screen.blit(first_txt, (70, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.restart()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def generate_food(self):
        while True:
            if (self.food_x, self.food_y) not in self.coord_list[:-1]:
                break
            else:
                self.food_x = random.randrange(0, self.w, self.snake.snake_cell)
                self.food_y = random.randrange(0, self.h, self.snake.snake_cell)
        pygame.draw.rect(self.screen, self.food_color,
                         (self.food_x , self.food_y , self.snake.snake_cell, self.snake.snake_cell))


    def bite(self):
        for g in self.coord_list[:-1]:
            if g == (self.snake.x, self.snake.y):
                self.game_close = True

    def draw_snake(self):
        if len(self.coord_list) > self.snake.size:
            del self.coord_list[0]
        for x, y in self.coord_list:
            if (x, y) == self.coord_list[-1]:
                color = self.snake.head_color
            else:
                color = self.snake.body_color

            pygame.draw.rect(self.screen, color, (x, y, self.snake.snake_cell, self.snake.snake_cell))

    def start(self):
        self.snake.spawn(self.w, self.h)

        self.fps = 10
        self.score = 0
        self.game_run = True
        self.game_close = False

        self.food_x = random.randrange(0, self.w, self.snake.snake_cell)
        self.food_y = random.randrange(0, self.h, self.snake.snake_cell)

        self.coord_list = []

    def play(self):
        while not self.game_run:
            self.menu()
        while self.game_run:
            while self.game_close:
                self.screen.fill(self.snake.body_color)
                self.end_text(f'Your score: {self.score}', 'GAME OVER', 'S to start', 'C to close')
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            self.restart()

                        if event.key == pygame.K_c:
                            pygame.quit()
                            sys.exit()
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            self.screen.fill(self.field_color)
            self.text_overlay()
            self.draw_snake()
            self.snake.control()
            self.bite()
            self.snake.x += self.snake.x_turn
            self.snake.y += self.snake.y_turn
            self.coord_list.append((self.snake.x, self.snake.y))
            try:
                head = self.coord_list[-1]

                if not (0 <= head[0] < self.w) or not (0 <= head[1] < self.h):
                    self.game_close = True

            except IndexError:
                continue
            self.generate_food()
            self.eat()
            pygame.display.update()

            self.clock.tick(self.fps)

    def restart(self):
        self.start()
        self.play()
