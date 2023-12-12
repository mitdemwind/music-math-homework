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

# Example: Convert a music file to arrays and print the result
test_melody = converter.music2arrays('test.xml')
print("Converted Music to Arrays:")
print(test_melody)

# Example: Generate a population from a list of music files
population = converter.generate_population(['test.xml', 'test.xml', 'test.xml', 'test.xml'])
print("Generated Population:")
print(population)

# Run the genetic algorithm for a certain number of generations
num_generations = 5
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
converter.individual2music(best_individual, '')
