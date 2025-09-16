from pico2d import *
from enum import Enum

open_canvas(800,800)
grass = load_image('grass.png')
character = load_image('character.png')

class Direction(Enum):
    LEFT, RIGHT, UP, DOWN, CIRCLE = 0, 1, 2, 3, 4

x = 0
y = 90
speed = 5

direction = Direction.RIGHT
while (True):
    #게임 렌더링
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    if(direction == Direction.RIGHT):
        x += speed
        if(x > 800):
            direction = Direction.UP

    elif(direction == Direction.UP):
        y += speed
        if(y > 800):
            direction = Direction.LEFT

    elif(direction == Direction.LEFT):
        x -= speed
        if(x < 0):
            direction = Direction.DOWN

    elif(direction == Direction.DOWN):
        y -= speed
        if(y < 90):
            direction = Direction.RIGHT



    #게임 로직
    delay(0.01)


#게임 종료
close_canvas()