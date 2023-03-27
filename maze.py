import random
import maze_module as mm


if __name__ == '__main__':
    try:
        r = int(input("How many rows in labyrinth? : "))
        c = int(input("How many columns? : "))
    except ValueError:
        print("Wrong values")
        exit()

    exit = mm.exit_from_maze(r, c)
    paths = mm.make_paths(r, c, exit)
    start = random.choice(paths)

    roads = dict()
    roads[start] = count = 1
    mm.road_to_exit(paths, start, exit, roads, count)
    print(f"exit = {exit}")
    print(f"Start = {start}")

    if roads.get(exit):
        print("EXIT")
        mm.path(roads, exit, start)
    else:
        print("There isn't path to the exit :c")

    tab = []
    for i in range(r):
        tab.append([])
        for j in range(c):
            try:
                if roads.get((i, j)):
                    if type(roads[(i, j)]) == int:
                        tab[i].append('_')
                    else:
                        tab[i].append(roads.get((i, j)))
                elif paths.index((i, j)):
                    tab[i].append('_')
                else:
                    tab[i].append('W')
            except ValueError:
                tab[i].append('W')
    for i in range(r):
        print(*tab[i])

        # tab = []
        # for i in range(r):
        #     tab.append([])
        #     for j in range(c):
        #         try:
        #             if roads.get((i, j)):
        #                 if type(roads[(i, j)]) == int:
        #                     if roads[(i, j)] > 9:
        #                         tab[i].append('_')
        #                     else:
        #                         tab[i].append(roads.get((i, j)))
        #                 else:
        #                     tab[i].append(roads.get((i, j)))
        #             elif paths.index((i, j)):
        #                 tab[i].append('_')
        #             else:
        #                 tab[i].append('W')
        #         except ValueError:
        #             tab[i].append('W')
        # for i in range(r):
        #     print(*tab[i])