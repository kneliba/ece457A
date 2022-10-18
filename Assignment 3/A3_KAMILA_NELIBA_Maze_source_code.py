
from copy import deepcopy

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


def print_path(path, start, end2, end1):
    maze_copy = deepcopy(maze)

    for point in path:
        y = point[0]
        x = point[1]
        maze_copy[y][x] = 2

    maze_copy[start[0]][start[1]] = 'S'
    maze_copy[end1[0]][end1[1]] = 'E'
    maze_copy[end2[0]][end2[1]] = 'E'

    all_rows = []
    oriented_maze = deepcopy(maze_copy[::-1])

    for row in oriented_maze:
        current_row = []

        for value in row:
            if value == 1:
                current_row.append(chr(0x25A0))

            elif value == 0:
                current_row.append('.')

            elif value == 2:
                current_row.append('*')

            else:
                current_row.append(value)

        all_rows.append(' '.join(current_row))

    print('\n'.join(all_rows))


def print_info(final_goal, final_path, cost):
    print(f"Goal found: {final_goal}")
    print(f"Path cost: {len(final_path)}")
    print(f"Nodes explored: {cost} \n")


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1][0]][path[-1][1]])
    path.reverse()

    return path


def get_manhattan_distance(position, end1, end2):
    y = position[0]
    x = position[1]

    man1 = abs(y-end1[0]) + abs(x-end1[1])
    man2 = abs(y-end2[0]) + abs(x-end2[1])

    return min(man1, man2)


def search_maze(start, end1, end2):
    fringe = []
    position = [start[0], start[1], 0, 0, 0]
    expanded = []
    parent = deepcopy(maze)

    i = 0
    while ([position[0], position[1]] != end1 and [position[0], position[1]] != end2):
        print(expanded)

        if (len(fringe) > 0):
            fringe.sort(key=lambda col: col[4])
            print(fringe)
            position = fringe[0]
            fringe.pop(0)

            if [position[0], position[1]] in expanded:
                continue  # go to next loop

        print(position)

        y = position[0]
        x = position[1]

        expanded.append([y, x])

        if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in expanded:
            man_dist = get_manhattan_distance([y, x+1], end1, end2)
            fringe.append([y, x+1, position[2]+1, man_dist,
                          position[2]+1 + man_dist])
            parent[y][x+1] = [y, x]

        if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in expanded:
            man_dist = get_manhattan_distance([y+1, x], end1, end2)
            fringe.append([y+1, x, position[2]+1, man_dist,
                          position[2]+1 + man_dist])
            parent[y+1][x] = [y, x]

        if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in expanded:
            man_dist = get_manhattan_distance([y, x-1], end1, end2)
            fringe.append([y, x-1, position[2]+1, man_dist,
                          position[2]+1 + man_dist])
            parent[y][x-1] = [y, x]

        if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in expanded:
            man_dist = get_manhattan_distance([y-1, x], end1, end2)
            fringe.append([y-1, x, position[2]+1, man_dist,
                          position[2]+1 + man_dist])
            parent[y-1][x] = [y, x]

        i += 1

    goalfound = expanded[-1]
    final_path = backtrace(parent, start, goalfound)
    print_path(final_path, start, end1, end2)
    print_info(goalfound, final_path, len(expanded))


start = [11, 2]
end1 = [19, 23]
end2 = [21, 2]
search_maze(start, end1, end2)
