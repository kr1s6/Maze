import random
import maze_module as mm


if __name__ == '__main__':
    r = int(input("How many rows in labyrinth? : "))
    c = int(input("How many columns? : "))

    with open("maze.txt", 'w') as maze:
        exit = mm.exit(r, c)
        paths = mm.make_paths(r, c, exit)
        paths.append(exit)
        start = random.choice(paths)
        print(f"exit = {exit}")
        print(f"Start = {start}")

        tab = []
        for i in range(r):
            tab.append([])
            for j in range(c):
                if (i, j) == start:
                    tab[i].append(1)
                elif (i, j) in paths:
                    tab[i].append('_')
                else:
                    tab[i].append('W')
        for i in range(r):
            print(*tab[i])
