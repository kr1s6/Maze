import random
import maze_module as mm


if __name__ == '__main__':
    r = int(input("How many rows in labyrinth? : "))
    c = int(input("How many columns? : "))

    with open("maze.txt", 'w') as maze:
        exit = mm.exit_from_maze(r, c)
        paths = mm.make_paths(r, c, exit)
        start = random.choice(paths)

        roads = dict()
        count = 1
        roads[start] = count
        mm.road_to_exit(paths, start, exit, roads, count)
        if exit in roads:
            mm.path(roads, exit, start)
        print(f"exit = {exit}")
        print(f"Start = {start}")

        tab = []
        for i in range(r):
            tab.append([])
            for j in range(c):
                if (i, j) in roads:
                    if type(roads[(i, j)]) == int:
                        tab[i].append('*')
                    else:
                        tab[i].append(roads.get((i, j)))
                elif (i, j) in paths and (i, j) not in roads:
                    tab[i].append('_')
                else:
                    tab[i].append('W')
        for i in range(r):
            print(*tab[i])
