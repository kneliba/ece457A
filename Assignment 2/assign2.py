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
    print(path)
    return path


def search_maze(search_type, start, end1, end2, order):
    fringe = []
    position = [start[0], start[1]]

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

        if order == 1:
            # left
            if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in fringe and [y, x-1] not in expanded:
                fringe.append([y, x-1])
                parent[y][x-1] = [y, x]
            # up
            if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in fringe and [y+1, x] not in expanded:
                fringe.append([y+1, x])
                parent[y+1][x] = [y, x]
            # right
            if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in fringe and [y, x+1] not in expanded:
                fringe.append([y, x+1])
                parent[y][x+1] = [y, x]
            # down
            if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in fringe and [y-1, x] not in expanded:
                fringe.append([y-1, x])
                parent[y-1][x] = [y, x]

        if order == 2:
            # right
            if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in fringe and [y, x+1] not in expanded:
                fringe.append([y, x+1])
                parent[y][x+1] = [y, x]

            # up
            if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in fringe and [y+1, x] not in expanded:
                fringe.append([y+1, x])
                parent[y+1][x] = [y, x]

            # left
            if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in fringe and [y, x-1] not in expanded:
                fringe.append([y, x-1])
                parent[y][x-1] = [y, x]

            # down
            if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in fringe and [y-1, x] not in expanded:
                fringe.append([y-1, x])
                parent[y-1][x] = [y, x]

        if order == 3:
            # down
            if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in fringe and [y-1, x] not in expanded:
                fringe.append([y-1, x])
                parent[y-1][x] = [y, x]

            # right
            if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in fringe and [y, x+1] not in expanded:
                fringe.append([y, x+1])
                parent[y][x+1] = [y, x]

            # up
            if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in fringe and [y+1, x] not in expanded:
                fringe.append([y+1, x])
                parent[y+1][x] = [y, x]

            # left
            if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in fringe and [y, x-1] not in expanded:
                fringe.append([y, x-1])
                parent[y][x-1] = [y, x]

        if order == 4:
            # down
            if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in fringe and [y-1, x] not in expanded:
                fringe.append([y-1, x])
                parent[y-1][x] = [y, x]

            # left
            if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in fringe and [y, x-1] not in expanded:
                fringe.append([y, x-1])
                parent[y][x-1] = [y, x]

            # up
            if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in fringe and [y+1, x] not in expanded:
                fringe.append([y+1, x])
                parent[y+1][x] = [y, x]

            # right
            if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in fringe and [y, x+1] not in expanded:
                fringe.append([y, x+1])
                parent[y][x+1] = [y, x]

    goalfound = expanded[-1]
    print(len(expanded))
    return backtrace(parent, start, goalfound)


start = [11, 2]
end1 = [19, 23]
end2 = [21, 2]

final_path = search_maze("depth", start, end1, end2, 4)
# print(final_path)
print(len(final_path))
