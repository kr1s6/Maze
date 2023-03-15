import maze_module as mm


if __name__ == '__main__':
    r = int(input("How many rows in labyrinth? : "))
    c = int(input("How many columns? : "))

    with open("maze.txt", 'w') as maze:
        exit = mm.exit(r, c)
        print(f"exit = {exit}")
        #############################
        borders = mm.borders(r, c, exit)
        #############################
        paths = mm.make_paths(r, c, exit)

        oddsW = "WWWWWWWWWX"
        oddsX = "WXXXXXXXXXXX"