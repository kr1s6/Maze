import random


# making exit's coordinates
def exit(r, c):
    exit_r = random.randint(0, r - 1)
    if exit_r in (0, r - 1):
        exit_c = random.randint(1, c - 2)
    else:
        exit_c = random.choice((0, c-1))
    return exit_r, exit_c


####################################
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


###############################################################
#making paths inside maze
def make_paths(r, c, door):
    x, y = exit_ex(r, c, door)
    paths = set()
    for i in range(1, r-2):
        for j in range(1, c-2):
            if i == x or j == y:
                if random.random() <= 0.95:
                    paths.add((i, j))
            else:
                if random.random() <= 0.05:
                    paths.add((i, j))


#finding one block before exit, later to use for higher possibility to find road to exit
def exit_ex(r, c, door):
    x, y = door
    door_ex = tuple()
    if x == 0:
        door_ex = (x + 1, y)
    elif x == (r - 1):
        door_ex = (x - 1, y)
    elif y == 0:
        door_ex = (x, y + 1)
    elif y == (c - 1):
        door_ex = (x, y - 1)
    return door_ex