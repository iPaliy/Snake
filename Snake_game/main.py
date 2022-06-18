from snake import Snake
from field import Field


if __name__ == '__main__':
    snake = Snake()
    field = Field(snake)
    field.start()
    field.play()
