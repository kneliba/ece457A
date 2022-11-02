from copy import deepcopy
import random

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


def neighbourhood_search(solution, tabu_num, tabu_list, aspiration, all_time_best_cost, half, frequency):
    best_solution = []
    best_cost = 100000
    frequency_cost = 0

    if (aspiration == False):
        all_time_best_cost = 0

    best_i = -1
    best_j = -1

    for i in range(0, len(solution)-1):
        for j in range(i+1, len(solution)):
            if half == True:
                if random.choice([0, 1]) == 1:
                    continue

            copy = deepcopy(solution)
            copy[i], copy[j] = copy[j], copy[i]

            if (frequency == True):
                frequency_cost = tabu_list[best_j][best_i]
            cost = evaluate(copy) + frequency_cost * 2

            if (tabu_list[i][j] == 0 or cost < all_time_best_cost) and len(best_solution) == 0:
                best_solution = deepcopy(copy)
                best_cost = cost
                best_i = i
                best_j = j

            if (tabu_list[i][j] == 0 or cost < all_time_best_cost) and cost < best_cost:
                best_solution = deepcopy(copy)
                best_cost = cost
                best_i = i
                best_j = j

    tabu_list[best_i][best_j] = tabu_num
    if (frequency == True):
        tabu_list[best_j][best_i] += 1

    return best_solution, tabu_list, best_cost


def decremented_tabu(tabu_list):
    tabu = deepcopy(tabu_list)
    for i in range(0, 19):
        for j in range(i+1, 20):
            if (tabu[i][j] != 0):
                tabu[i][j] -= 1

    return tabu


def tabu_search(start_point, tabu_num, half_neighours, frequency, aspiration):
    departments = start_point

    tabu_list = [[0]*20 for i in range(20)]

    best_departments = deepcopy(departments)
    cost = evaluate(best_departments)
    best_cost = cost
    best_iteration = 0

    i = 0
    while i < 3000:
        # print(f"i:{i} {departments} {cost} Best cost: {best_cost}")

        [departments, tabu_list, cost] = neighbourhood_search(
            departments, tabu_num, tabu_list, aspiration, best_cost, half_neighours, frequency)

        tabu_list = deepcopy(decremented_tabu(tabu_list))

        if cost < best_cost:
            best_cost = cost
            best_departments = deepcopy(departments)
            best_iteration = i

        i += 1

    print(
        f"order: {best_departments}, cost: {evaluate(best_departments)}, num_i: {best_iteration} \n")


half_neighours = False
frequency = False
aspiration = False
tabu_num = 14

departments = list(range(1, 21))  # incrementing

departments1 = [20, 19, 18, 17, 16, 15, 14,
                13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # decrementing
departments2 = [20, 1, 19, 2, 18, 3, 17, 4,
                16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]  # oscillating

print("default + tabu: 13")
tabu_search(departments, tabu_num=13, half_neighours=False,
            frequency=False, aspiration=False)

print("default + decrease tabu: 10")
tabu_search(departments, tabu_num=10, half_neighours=False,
            frequency=False, aspiration=False)

print("default + increase tabu: 16")
tabu_search(departments, tabu_num=16, half_neighours=False,
            frequency=False, aspiration=False)

print("change departments:")
tabu_search(departments1, tabu_num=13, half_neighours=False,
            frequency=False, aspiration=False)

print("change departments:")
tabu_search(departments2, tabu_num=13, half_neighours=False,
            frequency=False, aspiration=False)

print("aspiration:")
tabu_search(departments, tabu_num=13, half_neighours=False,
            frequency=False, aspiration=True)
print("aspiration + half neighbours:")
tabu_search(departments, tabu_num=13, half_neighours=True,
            frequency=False, aspiration=True)
print("aspiration + frequency:")
tabu_search(departments, tabu_num=13, half_neighours=False,
            frequency=True, aspiration=True)
