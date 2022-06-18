import sys
import pygame


class Snake:
    def __init__(self):
        self.snake_cell = 10
        self.eat_inc = 1  # eat increment
        self.head_color = (255, 0, 0)  # red
        self.body_color = (0, 255, 0)  # green

        self.size = None
        self.command = None
        self.x, self.y = None, None
        self.x_turn = None
        self.y_turn = None

    def spawn(self, w, h):
        self.size = 1
        self.x_turn = 0
        self.y_turn = 0
        self.command = []
        self.x = w // 2
        self.y = h // 2

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    try:
                        if self.command[0] == 4:
                            continue
                        else:
                            self.x_turn = self.snake_cell
                            self.y_turn = 0
                            self.command.append(2)
                    except IndexError:
                        self.x_turn = self.snake_cell
                        self.y_turn = 0
                        self.command.append(2)
                elif event.key == pygame.K_LEFT:
                    try:
                        if self.command[0] == 2:
                            continue
                        else:
                            self.x_turn = -self.snake_cell
                            self.y_turn = 0
                            self.command.append(4)
                    except IndexError:
                        self.x_turn = -self.snake_cell
                        self.y_turn = 0
                        self.command.append(4)
                elif event.key == pygame.K_UP:
                    try:
                        if self.command[0] == 3:
                            continue
                        else:
                            self.x_turn = 0
                            self.y_turn = -self.snake_cell
                            self.command.append(1)
                    except IndexError:
                        self.x_turn = 0
                        self.y_turn = -self.snake_cell
                        self.command.append(1)
                elif event.key == pygame.K_DOWN:
                    try:
                        if self.command[0] == 1:
                            continue
                        else:
                            self.x_turn = 0
                            self.y_turn = self.snake_cell
                            self.command.append(3)
                    except IndexError:
                        self.x_turn = 0
                        self.y_turn = self.snake_cell
                        self.command.append(3)
                if len(self.command) > 1:
                    del self.command[0]

