import os
import numpy as np
from population import *
from preprocess import *
from constants import *
from fitfunction import FitFunction


converter = Converter()

# Ensure the 'data' directory exists
if 'data' not in os.listdir('.'):
    os.mkdir('data/')

initial_files = list(filter(lambda x: 'initial_' in x, os.listdir('./data')))

population = converter.generate_population(initial_files)
print("Generated Population:")
print(population)

# Run the genetic algorithm for a certain number of generations
num_generations = 20
for generation in range(num_generations):
    print(f"Generation {generation + 1}")
    best_individual = population.members[np.argmax(population.adaptibilty)]

    if best_individual is not None:
        print(f"Best Fitness: {population.fitfunc(best_individual)}")
    else:
        print("No individuals in the population.")
    population.update()

# Print the final population information
print("Final Population:")
best_individual = population.members[np.argmax(population.adaptibilty)]
print(f"Best Fitness: {population.fitfunc(best_individual)}")
fg = converter.individual2music(best_individual, 'return')

bg = converter.make_chords(fg.chords())
sss = ms.stream.Score([fg, bg])
sss.show()
