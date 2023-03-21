import random


# making exit's coordinates
def exit_from_maze(r, c):
    exit_r = random.randint(0, r - 1)
    if exit_r in (0, r - 1):
        exit_c = random.randint(1, c - 2)
    else:
        exit_c = random.choice((0, c-1))
    return exit_r, exit_c


###############################################################
#making paths inside maze
def make_paths(r, c, exit):
    x, y = exit_ex(r, c, exit)
    paths = list()
    for i in range(1, r-1):
        for j in range(1, c-1):
            if i == x or j == y:
                if random.random() <= 0.95:
                    paths.append((i, j))
            else:
                if random.random() <= 0.618033:
                    paths.append((i, j))
    paths.append(exit)
    return paths


#finding one block before exit to use for higher possibility to find road to exit
def exit_ex(r, c, exit):
    x, y = exit
    exitt = list()
    if x == 0:
        exitt = (x + 1, y)
    elif x == (r - 1):
        exitt = (x - 1, y)
    elif y == 0:
        exitt = (x, y + 1)
    elif y == (c - 1):
        exitt = (x, y - 1)
    return exitt


##############################################################################
#searching for road to exit
def road_to_exit(paths, point, exit, roads, count):
    if point == exit:
        print("EXIT")
        return True
    x, y = point
    for m, n in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
        if (m, n) in paths:
            try:
                if roads[(m, n)] <= count:
                    continue
                elif roads[(m, n)] > count + 1:
                    roads[(m, n)] = count + 1
            except KeyError:
                roads[(m, n)] = count + 1
                if (m, n) == exit:
                    print("EXIT")
                    return True

    for m, n in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
        try:
            if roads[(m, n)] == count + 1:
                roads = road_to_exit(paths, (m, n), exit, roads, count + 1)
                if roads is True:
                    break
        except KeyError:
            continue
    return roads