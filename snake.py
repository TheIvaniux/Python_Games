"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def randomColor():
    """Return random color for snake and food."""
    allcolors = ['black', 'blue', 'green', 'yellow', 'purple']
    index=randrange(0, 5)
    colorS = allcolors[index] 
    colorF = allcolors[index-1]
    return colorS, colorF

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorS)

    square(food.x, food.y, 9, colorF)
    
    #if the food isn´t in the boundaries
    if -190 < food.x < 180 and -190 < food.y < 180:
        #5% chance of move
        if (randrange(0,100,1) < 5):
            food.x = food.x + (randrange(-1, 1) * 10)
            food.y = food.y + (randrange(-1, 1) * 10)
    
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
#Set random color for snake and food
colorS, colorF = randomColor()
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
