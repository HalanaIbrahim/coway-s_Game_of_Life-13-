import copy, random, sys, time

#cell grid 
WIDTH = 79
HEIGHT = 24

#game characters 

ALIVE = '0'
DEAD = ''

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
    print('\n' * 50)
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

    if cell[(left, above)] == ALIVE:
        aliveNe += 1
    if cell[(x, above)] == ALIVE:
        aliveNe += 1
    if cell[(right, above)] == ALIVE:
        aliveNe += 1
    if cell[(left, y)] == ALIVE:
        aliveNe += 1
    if cell[(right, y)] == ALIVE:
        aliveNe += 1
    if cell[(left, below)] == ALIVE:
        aliveNe += 1
    if cell[(x, below)] == ALIVE:
        aliveNe += 1
    if cell[(right, below)] == ALIVE:
        aliveNe += 1
    
    #Cell rules 
    if cell[(x,y)] == ALIVE and (aliveNe == 2 or aliveNe ==3):
        nextCell[(x, y)] == ALIVE
    elif cell[(x, y)] == DEAD and aliveNe == 3:
        nextCell[(x, y)] = ALIVE
    else:
        nextCell[(x,y)] == DEAD

        try:
            time.sleep(1)
        except:
             KeyboardInterrupt

    break