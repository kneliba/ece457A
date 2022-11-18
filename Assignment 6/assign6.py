from math import inf
from numpy.random import randint
from numpy.random import rand
import matplotlib.pyplot as plt
import numpy as np
import graycode


def get_x_y(chromosome):
    mid_point = int(len(chromosome)/2)

    gc_x, gc_y = chromosome[:mid_point], chromosome[mid_point:]

    bin_x = binary_from_gc(gc_x)
    bin_y = binary_from_gc(gc_y)

    x, y = sum(val*(2**idx) for idx, val in enumerate(reversed(list(bin_x)))
               ), sum(val*(2**idx) for idx, val in enumerate(reversed(bin_y)))

    return (x-5000)/1000, (y-5000)/1000


def flip(bit):
    return '1' if (bit == '0') else '0'


def binary_from_gc(greycode):
    binary = ""
    binary += str(greycode[0])

    for i in range(1, len(greycode)):
        if (greycode[i] == 0):
            binary += binary[i-1]
        else:
            binary += flip(binary[i-1])

    binary_form = [eval(s) for s in list(binary)]
    return binary_form


def evaluate(x, y):
    return (4 - 2.1*x**2 + (x**4)/3)*x**2 + x*y + (-4 + 4*y**2)*y**2


def get_parents(pop, fitness, k):
    # tournament style
    winner = randint(len(pop))

    for i in randint(0, len(pop), k-1):
        if fitness[i] < fitness[winner]:
            winner = i

    return pop[winner]


def mutate(offspring):
    for i in range(len(offspring)):
        if rand() < 0.05:
            offspring[i] = abs(offspring[i]-1)

    return offspring


def get_offspring(parents):
    offspring = []
    for i in range(0, len(parents), 2):
        p1, p2 = parents[i], parents[i+1]
        c1, c2 = p1.copy(), p2.copy()

        # crossover
        if rand() < 0.9:
            pt = randint(1, len(p1)-2)

            c1 = p1[:pt] + p2[pt:]
            c2 = p2[:pt] + p1[pt:]

        offspring.append(mutate(c1))
        offspring.append(mutate(c2))
    return offspring


def simple_ga(n_bits, n_iter, n_pop):
    pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]

    best_chrome, best_eval = inf, inf

    avg_fitness = []
    best_per_iter = []

    j = 0
    for generation in range(n_iter):
        fitness = [evaluate(*get_x_y(gene)) for gene in pop]
        current_avg = sum(fitness)/len(fitness)
        avg_fitness.append(current_avg)

        for i in range(n_pop):
            if fitness[i] < best_eval:
                best_eval, best_chrome = fitness[i], pop[i]

        best_per_iter.append(best_eval)

        best_x, best_y = get_x_y(best_chrome)

        print(
            f"i:{j} Best: {best_eval}, x:{best_x}, y:{best_y} Average:{current_avg}")

        parents = [get_parents(pop, fitness, 3)
                   for gene in range(len(pop))]

        pop = get_offspring(parents)
        j += 1

    return [best_chrome, best_eval, avg_fitness, best_per_iter]


n_bits = 28
n_pop = 140
n_iter = 140

best_chrome, best_eval, avg_fit, best_iter = simple_ga(n_bits, n_pop, n_iter)
print(f"final solution: {best_eval}")
x, y = get_x_y(best_chrome)
print(f"x: {x}, y: {y}")

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
