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
num_generations = 10
for generation in range(num_generations):
    print(f"Generation {generation + 1}")
    best_individual = population.members[np.argmax(population.adaptibilty)]

    if best_individual is not None:
        # print(f"Best Individual: {best_individual}")
        print(f"Best Fitness: {population.fitfunc(best_individual)}")
    else:
        print("No individuals in the population.")
    print("")

    # Update the population to the next generation
    population.update()

# Print the final population information
print("Final Population:")
best_individual = population.members[np.argmax(population.adaptibilty)]
print(f"Best Fitness: {population.fitfunc(best_individual)}")
fg = converter.individual2music(best_individual, 'return')

from randmusic_5 import bgmusic
sss = ms.stream.Score([fg, bgmusic])
sss.show()
save = input("Save it or not:")
if save == 'y':
    sss.write('xml', './data/result.xml')
