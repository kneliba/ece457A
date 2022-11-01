from copy import deepcopy

flow = [[0, 0, 5, 0, 5, 2, 10, 3, 1, 5, 5, 5, 0, 0, 5, 4, 4, 0, 0, 1],
        [0, 0, 3, 10, 5, 1, 5, 1, 2, 4, 2, 5, 0, 10, 10, 3, 0, 5, 10, 5],
        [5, 3, 0, 2, 0, 5, 2, 4, 4, 5, 0, 0, 0, 5, 1, 0, 0, 5, 0, 0],
        [0, 10, 2, 0, 1, 0, 5, 2, 1, 0, 10, 2, 2, 0, 2, 1, 5, 2, 5, 5],
        [5, 5, 0, 1, 0, 5, 6, 5, 2, 5, 2, 0, 5, 1, 1, 1, 5, 2, 5, 1],
        [2, 1, 5, 0, 5, 0, 5, 2, 1, 6, 0, 0, 10, 0, 2, 0, 1, 0, 1, 5],
        [10, 5, 2, 5, 6, 5, 0, 0, 0, 0, 5, 10, 2, 2, 5, 1, 2, 1, 0, 10],
        [3, 1, 4, 2, 5, 2, 0, 0, 1, 1, 10, 10, 2, 0, 10, 2, 5, 2, 2, 10],
        [1, 2, 4, 1, 2, 1, 0, 1, 0, 2, 0, 3, 5, 5, 0, 5, 0, 0, 0, 2],
        [5, 4, 5, 0, 5, 6, 0, 1, 2, 0, 5, 5, 0, 5, 1, 0, 0, 5, 5, 2],
        [5, 2, 0, 10, 2, 0, 5, 10, 0, 5, 0, 5, 2, 5, 1, 10, 0, 2, 2, 5],
        [5, 5, 0, 2, 0, 0, 10, 10, 3, 5, 5, 0, 2, 10, 5, 0, 1, 1, 2, 5],
        [0, 0, 0, 2, 5, 10, 2, 2, 5, 0, 2, 2, 0, 2, 2, 1, 0, 0, 0, 5],
        [0, 10, 5, 0, 1, 0, 2, 0, 5, 5, 5, 10, 2, 0, 5, 5, 1, 5, 5, 0],
        [5, 10, 1, 2, 1, 2, 5, 10, 0, 1, 1, 5, 2, 5, 0, 3, 0, 5, 10, 10],
        [4, 3, 0, 1, 1, 0, 1, 2, 5, 0, 10, 0, 1, 5, 3, 0, 0, 0, 2, 0],
        [4, 0, 0, 5, 5, 1, 2, 5, 0, 0, 0, 1, 0, 1, 0, 0, 0, 5, 2, 0],
        [0, 5, 5, 2, 2, 0, 1, 2, 0, 5, 2, 1, 0, 5, 5, 0, 5, 0, 1, 1],
        [0, 10, 0, 5, 5, 1, 0, 2, 0, 5, 2, 2, 0, 5, 10, 2, 2, 1, 0, 6],
        [1, 5, 0, 5, 1, 5, 10, 10, 2, 2, 5, 5, 5, 0, 10, 0, 0, 1, 6, 0]]

distance = [[0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7],
            [1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5, 6],
            [2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5],
            [3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3, 6, 5, 4, 3, 4],
            [4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3],
            [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
            [2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5],
            [3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4],
            [4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3],
            [5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2],
            [2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5],
            [3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4],
            [4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3],
            [5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2],
            [6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1],
            [3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [4, 3, 4, 5, 6, 3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3],
            [5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2],
            [6, 5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1],
            [7, 6, 5, 4, 3, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0]]


def evaluate(solution):
    cost = 0
    for i in range(0, len(solution)-1):
        for j in range(i+1, len(solution)):
            cost += distance[i][j] * flow[solution[i]-1][solution[j]-1]
    return cost


def find_all_neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        j = i+1
        for j in range(len(solution)):
            if i < j:
                copy = deepcopy(solution)
                copy[i], copy[j] = copy[j], copy[i]
                cost = evaluate(copy)
                neighbours.append([copy, cost, [copy[i], copy[j]]])

    return neighbours


def decremented_tabu(tabu_list):
    for i in range(len(tabu_list)):
        if tabu_list[i][1] == 1:
            tabu_list.pop(i)
            continue

        tabu_list[i][1] = tabu_list[i][1] - 1

    return tabu_list


def in_tabu(pos, tabu_list):
    for i in range(len(tabu_list)):
        if pos == tabu_list[i][0]:
            return True
    return False


def tabu_search():
    tabu_num = 14
    departments = list(range(1, 21))

    tabu_list = []

    i = 200
    while i > 0:
        print(i)
        tabu_list = deepcopy(decremented_tabu(tabu_list))

        neighbours = find_all_neighbours(departments)
        neighbours.sort(key=lambda col: col[1])

        print(neighbours)
        print(tabu_list)

        j = 0
        if in_tabu(neighbours[0][2], tabu_list) == False:
            tabu_list.append([neighbours[0][2], tabu_num])
        else:
            not_in_tabu = False

            while not_in_tabu == False:
                if in_tabu(neighbours[j][2], tabu_list) == False:
                    not_in_tabu = True
                j += 1

        departments = deepcopy(neighbours[j][0])
        i -= 1

    print(departments)
    print(evaluate(departments))


tabu_search()
