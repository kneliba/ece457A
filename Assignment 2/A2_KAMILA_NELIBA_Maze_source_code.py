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


def search_maze(search_type, start, end1, end2, order):
    fringe = []
    position = [start[0], start[1]]
    if search_type == "depth":
        order.reverse()

    expanded = []
    parent = deepcopy(maze)

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
                if x - 1 >= 0 and maze[y][x-1] == 0 and [y, x-1] not in expanded:
                    fringe.append([y, x-1])
                    parent[y][x-1] = [y, x]

            if move == 'u':
                if y + 1 < 25 and maze[y+1][x] == 0 and [y+1, x] not in expanded:
                    fringe.append([y+1, x])
                    parent[y+1][x] = [y, x]

            if move == 'r':
                if x + 1 < 25 and maze[y][x+1] == 0 and [y, x+1] not in expanded:
                    fringe.append([y, x+1])
                    parent[y][x+1] = [y, x]

            if move == 'd':
                if y - 1 >= 0 and maze[y-1][x] == 0 and [y-1, x] not in expanded:
                    fringe.append([y-1, x])
                    parent[y-1][x] = [y, x]

    goalfound = expanded[-1]
    final_path = backtrace(parent, start, goalfound)
    print_path(final_path, start, end1, end2)
    print_info(goalfound, final_path, len(expanded))


start = [11, 2]
end1 = [19, 23]
end2 = [21, 2]

order1 = ['l', 'u', 'r', 'd']
order2 = ['r', 'u', 'l', 'd']

print("BFS Order(1)")
search_maze("breadth", start, end1, end2, order1)
print("BFS Order(2)")
search_maze("breadth", start, end1, end2, order2)
print("DFS Order(1)")
search_maze("depth", start, end1, end2, order1)
print("DFS Order(2)")
search_maze("depth", start, end1, end2, order2)
