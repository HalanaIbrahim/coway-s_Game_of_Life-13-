import copy, random, sys, time

#cell grid 
WIDTH = 79
HEIGHT = 24

#game characters 

ALIVE = '0'
DEAD = '-'

#empty dictionary 
nextCell = {}

#loop that randomly assings the characters 
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            nextCell [(x, y)] = ALIVE
        else:
            nextCell [(x, y)] = DEAD
    

while True:
    print('\n * 50')
    cell = copy.deepcopy(nextCell)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cell[(x,y)], end=' ')
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
    aliveNe = 0
    
