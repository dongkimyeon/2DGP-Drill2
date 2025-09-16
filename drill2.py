from pico2d import *
from enum import Enum
import math

open_canvas(800,800)
grass = load_image('grass.png')
character = load_image('character.png')

class Direction(Enum):
    LEFT, RIGHT, UP, DOWN  = 0, 1, 2, 3

class State(Enum):
    CIRCLE, RECT = 0, 1

x = 400
y = 90

speed = 20
move_diff = 0

mid_X = 400
mid_Y = 400

angle = math.atan2( y - mid_Y, x - mid_X)

r = math.sqrt((mid_X - x) ** 2 + (mid_Y - y) ** 2) # 반지름

state = State.RECT
direction = Direction.RIGHT

def Move_Rectangle():
    global direction
    global x, y
    global state
    global move_diff
    move_diff += speed
    if(x == 400 and y == 90):
        print(move_diff)
    if direction == Direction.RIGHT:
        x += speed
        if x >= 800:
            direction = Direction.UP

    if direction == Direction.UP:
        y += speed
        if y >= 800:
            direction = Direction.LEFT
    if direction == Direction.LEFT:
        x -= speed
        if x <= 0:
            direction = Direction.DOWN
    if direction == Direction.DOWN:
        y -= speed
        if y <= 90:
            direction = Direction.RIGHT


def Move_Circle():
    global angle
    global x, y
    global r
    global state

    angle -= 0.1
    #print(math.degrees(angle))
    x = mid_X + r * math.cos(angle)
    y = mid_Y + r * math.sin(angle)
    if math.degrees(angle) <= -360 -90:
        angle = math.atan2( y - mid_Y, x - mid_X)
        state = State.RECT


while (True):
    #게임 렌더링
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    if(state == State.RECT):
        Move_Rectangle()
        if(move_diff >= 3000):
            move_diff = 0
            state = State.CIRCLE
    elif(state == State.CIRCLE):
        Move_Circle()

    delay(0.01)


#게임 종료
close_canvas()