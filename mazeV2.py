import maze_module as mm


if __name__ == '__main__':
    r = int(input("How many rows in labyrinth? : "))
    c = int(input("How many columns? : "))

    with open("maze.txt", 'w') as maze:
        x, y = mm.exit(r, c)
        exit = (x, y)
        #############################
        

        oddsW = "WWWWWWWWWX"
        oddsX = "WXXXXXXXXXXX"
        corners = {(0, 0), (0, c - 1), (r - 1, 0), (r - 1, c - 1)}