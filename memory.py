"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#More color options for the tiles
available_colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'lime', 'pink', 'teal', 'olive', 'navy', 'maroon', 'brown', 'aquamarine', 'crimson', 'indigo', 'gold', 'silver', 'lavender', 'plum', 'coral', 'peru', 'orchid', 'skyblue', 'violet', 'khaki', 'salmon', 'tan', 'black', 'gray']
#Tap counter variable
tapcounter = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    #Tap counter adder
    global tapcounter
    tapcounter += 1
def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    goto(0,-250)
    #tap counter print
    write('Number of taps: ' + str(tapcounter), align='center', font=('Arial', 24, 'normal'))
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 24, y+2)
        #Define a color for each number
        color(available_colors[tiles[mark]])
        
        #Center the number in the square
        write(tiles[mark], align='center',font=('Arial', 30, 'normal'))
    
    #Know if the image was completed    
    if all(not hide[count] for count in range(64)):
        print("La imagen fue completada")
        
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
