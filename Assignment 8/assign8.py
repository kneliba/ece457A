
from math import inf
import random
from matplotlib import pyplot as plt
import numpy as np


def evaluate(x, y):
    return (4 - 2.1*x**2 + (x**4)/3)*x**2 + x*y + (-4 + 4*y**2)*y**2


def get_new_position(particles, velocity):
    new_particles = [[0 for j in range(2)]
                     for i in range(pop_size)]
    for i in range(len(particles)-1):
        new_particles[i][0] = particles[i][0] + velocity[i][0]
        new_particles[i][1] = particles[i][1] + velocity[i][1]
    return new_particles


def get_new_velocity(particles, velocity, p_best, g_best):
    c1 = 0.2
    c2 = 0.2

    r1 = random.uniform(0.0, 1)
    r2 = random.uniform(0.0, 1)

    w = random.uniform(0.4, 1)

    new_velocity = [[0 for j in range(2)]
                    for i in range(pop_size)]
    for i in range(len(particles)-1):
        new_velocity[i][0] = w*velocity[i][0] + c1*r1 * \
            (p_best[i][0] - particles[i][0]) + \
            c2*r2*(g_best[0] - particles[i][0])
        new_velocity[i][1] = w*velocity[i][1] + c1*r1 * \
            (p_best[i][1] - particles[i][1]) + \
            c2*r2*(g_best[1] - particles[i][1])
    return new_velocity


def PSO(pop_size, n_iter):
    average_fitness = []
    best_fitness = []
    g_best = inf
    g_best_i = -1
    g_best_fit = inf

    velocity = [[0 for j in range(2)]
                for i in range(pop_size)]
    print(velocity)
    particles = [[random.uniform(-5, 5) for j in range(2)]
                 for i in range(pop_size)]

    p_best = particles
    p_best_fit = [inf for i in range(pop_size)]

    j = 0
    for _ in range(n_iter):
        fitness = [evaluate(particle[0], particle[1])
                   for particle in particles]

        current_avg = sum(fitness) / len(fitness)
        average_fitness.append(current_avg)

        for i in range(len(particles)):
            if fitness[i] < p_best_fit[i]:
                p_best[i] = particles[i]
                p_best_fit[i] = fitness[i]

            if fitness[i] < g_best_fit:
                g_best = p_best[i]
                g_best_fit = fitness[i]
                g_best_i = i

        velocity = get_new_velocity(
            particles, velocity, p_best, g_best)
        particles = get_new_position(particles, velocity)

        best_fitness.append(g_best_fit)
        j += 1

        print(
            f"i:{j} Best: {g_best_fit}, x y:{p_best[g_best_i]} Average:{current_avg}")

    return g_best_fit, p_best[g_best_i], average_fitness, best_fitness


pop_size = 100
n_iter = 100
g_best, x_y, avg_fit, best_iter = PSO(pop_size, n_iter)

print(f"final solution: {g_best}")
print(f"x, y: {x_y}")

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
