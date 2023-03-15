import random


# making exit's coordinates
def exit(r, c):
    exit_r = random.randint(0, r - 1)
    if exit_r in (0, r - 1):
        exit_c = random.randint(1, c - 2)
    else:
        exit_c = random.choice((0, c-1))
    return exit_r, exit_c


#making borders of the labyrinth
def borders(r, c, door):
    bounds = set()
    for i in range(r):
        bounds.add((i, 0))
        bounds.add((i, c-1))
    for j in range(c):
        bounds.add((0, j))
        bounds.add((r-1, j))
    bounds.remove(door)
    return bounds
