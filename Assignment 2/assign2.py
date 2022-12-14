
maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1][0]][path[-1][1]])
    path.reverse()

    return path


def print_maze(given_maze, path, start, end1, end2):

    lines = []
    reverse = given_maze[::1]
    # https://python-tcod.readthedocs.io/en/latest/tcod/charmap-reference.html
    whiteSquare = chr(0x2591)
    blackSquare = chr(0x25A0)
    smileFace = chr(0x263B)
    for row in reverse:
        line = []
        for x in row:
            if x == 1:
                stuff = blackSquare
            elif x == 0:
                stuff = whiteSquare
            # elif x == 2:
            #     stuff = smileFace
            line.append(stuff)
        lines.append(' '.join(line))
    print('\n'.join(lines))


def search_maze(search_type, start, end1, end2, order):
    fringe = []
    position = [start[0], start[1]]
    if search_type == "depth":
        order.reverse()

    expanded = []
    parent = maze

    while (position != end1 and position != end2):
        if (len(fringe) > 0):
            if search_type == "breadth":
                position = fringe[0]
                fringe.pop(0)
            if search_type == "depth":
                position = fringe[-1]
                fringe.pop(-1)

        y = position[0]
        x = position[1]

        expanded.append(position)

        for move in order:
            if move == 'l':
                if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in fringe and [y, x-1] not in expanded:
                    fringe.append([y, x-1])
                    parent[y][x-1] = [y, x]

            if move == 'u':
                if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in fringe and [y+1, x] not in expanded:
                    fringe.append([y+1, x])
                    parent[y+1][x] = [y, x]

            if move == 'r':
                if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in fringe and [y, x+1] not in expanded:
                    fringe.append([y, x+1])
                    parent[y][x+1] = [y, x]

            if move == 'd':
                if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in fringe and [y-1, x] not in expanded:
                    fringe.append([y-1, x])
                    parent[y-1][x] = [y, x]

    goalfound = expanded[-1]
    return backtrace(parent, start, goalfound)


start = [11, 2]
end1 = [19, 23]
end2 = [21, 2]

order1 = ['l', 'u', 'r', 'd']
order2 = ['r', 'u', 'l', 'd']

final_path = search_maze("breadth", start, end1, end2, order2)
print_maze(maze, final_path, start, end1, end2)
