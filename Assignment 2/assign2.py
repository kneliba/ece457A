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


def breadthfirst(start, end1, end2, heirarchy):
    fringe = []
    position = [start[0], start[1]]

    expanded = []

    while (position != end1 and position != end2):
        if (len(fringe) > 0):
            position = fringe[0]
            fringe.pop(0)

        y = position[0]
        x = position[1]

        expanded.append(position)

        # left
        if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in fringe and [y, x-1] not in expanded:
            fringe.append([y, x-1])

        # up
        if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in fringe and [y+1, x] not in expanded:
            fringe.append([y+1, x])

        # right
        if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in fringe and [y, x+1] not in expanded:
            fringe.append([y, x+1])

        # down
        if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in fringe and [y-1, x] not in expanded:
            fringe.append([y-1, x])

    return expanded


def depthfirst(start, end1, end2):
    fringe = []
    position = [start[0], start[1]]

    expanded = []

    while (position != end1 and position != end2):
        if (len(fringe) > 0):
            position = fringe[-1]
            fringe.pop(-1)
            print(len(fringe))
            print(expanded)

        y = position[0]
        x = position[1]

        expanded.append(position)

        # left
        if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in fringe and [y, x-1] not in expanded:
            fringe.append([y, x-1])

        # up
        if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in fringe and [y+1, x] not in expanded:
            fringe.append([y+1, x])

        # right
        if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in fringe and [y, x+1] not in expanded:
            fringe.append([y, x+1])

        # down
        if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in fringe and [y-1, x] not in expanded:
            fringe.append([y-1, x])

    return expanded


start = [11, 2]
end1 = [19, 23]
end2 = [21, 2]

final_path = breadthfirst(start, end1, end2)
#final_path = depthfirst(start, end1, end2)
print(final_path)
print(len(final_path))
