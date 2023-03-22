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
        print(f"exit = {exit}")
        print(f"Start = {start}")
        # tabb = []
        # for i in range(r):
        #     tabb.append([])
        #     for j in range(c):
        #         if (i, j) in roads:
        #             if type(roads[(i, j)]) == int:
        #                 if roads[(i, j)] > 9:
        #                     tabb[i].append('*')
        #                 else:
        #                     tabb[i].append(roads.get((i, j)))
        #             else:
        #                 tabb[i].append(roads.get((i, j)))
        #         elif (i, j) in paths and (i, j) not in roads:
        #             tabb[i].append('_')
        #         else:
        #             tabb[i].append('W')
        # for i in range(r):
        #     print(*tabb[i])

        if exit in roads:
            print("EXIT")
            mm.path(roads, exit, start)
        else:
            print("There isn't path to the exit :c")

        tab = []
        for i in range(r):
            tab.append([])
            for j in range(c):
                if (i, j) in roads:
                    if type(roads[(i, j)]) == int:
                        if roads[(i, j)] > 9:
                            tab[i].append('_')
                        else:
                            tab[i].append(roads.get((i, j)))
                    else:
                        tab[i].append(roads.get((i, j)))
                elif (i, j) in paths and (i, j) not in roads:
                    tab[i].append('_')
                else:
                    tab[i].append('W')
        for i in range(r):
            print(*tab[i])