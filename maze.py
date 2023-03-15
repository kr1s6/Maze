import random


def road_to_exit(row, col):
    meta_r = (0, w-1)
    meta_c = (0, k-1)
    if row in meta_r or col in meta_c:  # locating the exit
        make_d(row, col)
        return True
    else:
        if tab[row - 1][col] == 0:
            tab[row - 1][col] = tab[row][col] + 1
            xx = road_to_exit(row - 1, col)
        elif tab[row + 1][col] == 0:
            tab[row + 1][col] = tab[row][col] + 1
            xx = road_to_exit(row + 1, col)
        elif tab[row][col - 1] == 0:
            tab[row][col - 1] = tab[row][col] + 1
            xx = road_to_exit(row, col - 1)
        elif tab[row][col + 1] == 0:
            tab[row][col + 1] = tab[row][col] + 1
            xx = road_to_exit(row, col + 1)
        else:  # return from dead end
            if tab[row - 1][col] == (tab[row][col] - 1) and tab[row - 1][col] != -1:
                xx = road_to_exit(row - 1, col)
            elif tab[row + 1][col] == (tab[row][col] - 1) and tab[row + 1][col] != -1:
                xx = road_to_exit(row + 1, col)
            elif tab[row][col - 1] == (tab[row][col] - 1) and tab[row][col - 1] != -1:
                xx = road_to_exit(row, col - 1)
            elif tab[row][col + 1] == (tab[row][col] - 1) and tab[row][col + 1] != -1:
                xx = road_to_exit(row, col + 1)
            else:  # next possible road doesn't exist
                return False
    if xx is True:
        return True
    elif xx is False:
        return False


def make_d(row, col):  # making the road to the exit with "D"
    if not(tab[row][col] == 1):
        if tab[row - 1][col] == (tab[row][col] - 1):
            make_d(row - 1, col)
        elif tab[row + 1][col] == (tab[row][col] - 1):
            make_d(row + 1, col)
        elif tab[row][col - 1] == (tab[row][col] - 1):
            make_d(row, col - 1)
        elif tab[row][col + 1] == (tab[row][col] - 1):
            make_d(row, col + 1)
    tab[row][col] = "D"


def show():
    for z in range(w):
        for y in range(k):
            if tab[z][y] == -1:
                tab[z][y] = "X"
            elif tab[z][y] == 0:
                tab[z][y] = " "

    for z in tab:
        for y in z:
            if type(y) == " ":
                print(y, end=" ")
            elif type(y) == int:
                if y >= 10:
                    print(y, end=" ")
                else:
                    print(y, end="  ")
            else:
                print(y, end="  ")
        print()


def show_false():
    for z in range(w):
        for y in range(k):
            if tab[z][y] == -1:
                tab[z][y] = "X"
            else:
                tab[z][y] = " "

    for z in tab:
        for y in z:
            if type(y) == " ":
                print(y, end=" ")
            elif type(y) == int:
                if y >= 10:
                    print(y, end=" ")
                else:
                    print(y, end="  ")
            else:
                print(y, end="  ")
        print()


w = int(input("How many rows in labyrinth? : "))
k = int(input("How many columns? : "))

with open("maze.txt", 'w') as maze:
    string = "WWWWWWWWWX"
    string3 = "WXXXXXXXXXXX"
    border_w = (0, w-1)
    border_k = (0, k-1)
    exit = False
    i = 0
    while i < w:
        j = 0
        while j < k:
            if i in border_w and j in border_k:  # labyrinth's corners
                maze.write("W")
            elif (i in border_w or j in border_k) and not exit:  # making walls when there isn't "exit" yet
                r = random.choice("WWWWWWWWWX")
                maze.write(r)
                if r == 'X' and not (i in border_w and j in border_k):  # check if "exit" exists
                    exit = True
                    print(f"Exit = tab[{i}][{j}]")
                    save_exit_w = i
                    save_exit_k = j
            elif (i in border_w or j in border_k) and exit:  # making walls when is "exit"
                maze.write("W")
            elif exit is True:  # making inside the labyrinth when is "exit"
                if (i == save_exit_w) or ((save_exit_w == 0) and (i == save_exit_w + 1)) \
                        or ((save_exit_w == (w-1)) and (i == save_exit_w - 1)):
                    r = random.choice("WXXXXXXXXXXXXXXXXXXX")  # 5% szans
                    maze.write(r)
                elif (j == save_exit_k) or ((save_exit_k == 0) and j == (save_exit_k + 1)) \
                        or (save_exit_k == (k-1) and j == (save_exit_k - 1)):
                    r = random.choice("WXXXXXXXXXXXXXXXXXXX")
                    maze.write(r)
                elif (save_exit_w in border_w) and (((save_exit_w % 2 == 0) and (i % 2 == 1))
                                                    or ((save_exit_w % 2 == 1) and (i % 2 == 0))):
                    r = random.choice(string3)  # gdy wyjście jest na górze
                    maze.write(r)
                elif (save_exit_k in border_k) and (((save_exit_k % 2 == 0) and (i % 2 == 1))
                                                    or ((save_exit_k % 2 == 1) and (i % 2 == 0))):
                    r = random.choice(string3)  # gdy wyjście jest na lewo lub prawo
                    maze.write(r)
                else:
                    r = random.choice(string)
                    maze.write(r)
            elif exit is False:  # making inside the labyrinth when there isn't "exit"
                if i % 2 == 1:
                    r = random.choice(string3)
                    maze.write(r)
                else:
                    r = random.choice(string)
                    maze.write(r)
            j += 1
        maze.write("\n")
        i += 1
    print(f"Czy wyjście zostało wygenerowane? {exit}")


with open("maze.txt", 'r') as maze:
    tab = []
    x = 0
    for line in maze.readlines():
        line = line.strip()
        tab.append([])
        for one in line:
            tab[x].append(one)
        x = x + 1

zero = False
for i in range(w):
    for j in range(k):
        if tab[i][j] == 'W':
            tab[i][j] = -1
        else:
            tab[i][j] = 0
            zero = True

if zero is True:
    random_row = random.randint(0, w - 1)
    random_column = random.randint(0, k - 1)
    while tab[random_row][random_column] != 0:
        random_row = random.randint(0, w - 1)
        random_column = random.randint(0, k - 1)

    tab[random_row][random_column] = 1
    print(f"start = tab[{random_row}][{random_column}]")

    road = road_to_exit(random_row, random_column)
    print(f"Is there road to exit? : {road}")
    if road is True:
        show()
    elif road is False:
        print("There isn't road to exit from labyrinth")
        show()

elif zero is False:
    print("Labyrinth is too small or there is something wrong")
    show_false()