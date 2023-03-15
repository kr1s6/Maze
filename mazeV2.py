import maze_module as mm


if __name__ == '__main__':
    r = int(input("How many rows in labyrinth? : "))
    c = int(input("How many columns? : "))

    with open("maze.txt", 'w') as maze:
        x, y = mm.exit(r, c)
        exit = (x, y)
        print(f"exit= {exit}")
        #############################
        borders = mm.borders(r, c, exit)
        #############################


        oddsW = "WWWWWWWWWX"
        oddsX = "WXXXXXXXXXXX"