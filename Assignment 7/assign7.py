from copy import deepcopy
from math import inf, sqrt
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import random


def euclidean_distance(x1, x2, y1, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


def distances(cities, x_coords, y_coords):
    distance = [[0]*len(cities) for _ in range(len(cities))]
    for i in range(0, len(cities)-1):
        for j in range(i+1, len(cities)):
            distance[i][j] = euclidean_distance(
                x_coords[i], x_coords[j], y_coords[i], y_coords[j])

    return distance


def pheremone_update(pheremones, degredation):
    for i in range(0, len(pheremones)-1):
        for j in range(i+1, len(pheremones)):
            pheremones[i][j] = pheremones[i][j]*degredation

    return pheremones


def pheremone_update_best(q, pheremones, best_path, best_length):
    for i in range(len(best_path)-1):
        pheremones[best_path[i]-1][best_path[i+1]-1] += q/best_length
        pheremones[best_path[i+1]-1][best_path[i]-1] += q/best_length

    pheremones[best_path[-1]-1][best_path[0]-1] += q/best_length
    pheremones[best_path[0]-1][best_path[-1]-1] += q/best_length
    return pheremones


def get_total_length(cities, distance):
    total_length = 0
    for i in range(len(cities)-1):
        total_length += distance[cities[i]-1][cities[i+1] -
                                              1] + distance[cities[i+1]-1][cities[i]-1]

    total_length += distance[cities[-1]-1][cities[0] -
                                           1] + distance[cities[0]-1][cities[-1]-1]

    return total_length


def travel_cities(cities, distance, pheremones):
    starting = 1
    visited = [starting]

    alpha = 0.9
    beta = 1.5

    for k in range(len(cities)-1):
        probabilities = []
        available_cities = []
        for i in range(0, visited[-1]-1):
            if i+1 not in visited:
                prob = pheremones[i][visited[-1]-1]**alpha / \
                    distance[i][visited[-1]-1]**beta
                probabilities.append(prob)
                available_cities.append(i+1)

        for j in range(visited[-1], len(distance)):
            if j+1 not in visited:
                prob = pheremones[visited[-1]-1][j]**alpha / \
                    distance[visited[-1]-1][j]**beta
                probabilities.append(prob)
                available_cities.append(j+1)

        next_city = random.choices(available_cities, weights=probabilities)

        visited.append(next_city[0])

    return visited


def aco(cities, x_coord, y_coord, n_iters):
    q = 10
    degredation = 0.9
    n_ants = 150

    pheremones = [[1]*len(cities) for _ in range(len(cities))]
    dist = distances(cities, x_coord, y_coord)

    print(
        f"best possible path: {[1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21]}")
    print(
        f"best possible length: {get_total_length([1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21], dist)}")

    best_length = inf
    best_path = []

    average_fitness = []
    best_fitness = []

    for iter in range(n_iters):
        paths = [travel_cities(cities, dist, pheremones)
                 for _ in range(n_ants)]
        total_lengths = [get_total_length(path, dist) for path in paths]
        current_avg = sum(total_lengths) / len(total_lengths)
        average_fitness.append(current_avg)

        pheremone_update(pheremones, degredation)
        for i in range(len(paths)):
            if total_lengths[i] < best_length:
                best_length = total_lengths[i]
                best_path = paths[i]

            pheremones = deepcopy(pheremone_update_best(
                q, pheremones, paths[i], total_lengths[i]))

        best_fitness.append(best_length)

    return best_path, best_length, average_fitness, best_fitness


city_coord = pd.read_excel(
    "/Users/kamilaneliba/Documents/GitHub/ece457A/Assignment 7/city_coordinates.xlsx")

city_num = list(range(1, 30))
x_coord, y_coord = city_coord[['X-coord.']
                              ].values, city_coord[['Y-coord.']].values

n_iter = 200
best_path, best_length, avg_fit, best_iter = aco(
    city_num, x_coord, y_coord, n_iter)

print(f"best length: {best_length}")
print(f"best path: {best_path}")

num_iter = list(range(1, n_iter+1))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(num_iter, avg_fit, 'g-')
ax2.plot(num_iter, best_iter, 'b-')

ax1.set_title("Average and Best Fitness over Time")

ax1.set_xlabel("Iteration Number")
ax1.set_ylabel("Average Fitness", color='g')
ax2.set_ylabel("Best Fitness", color='b')

plt.show()
