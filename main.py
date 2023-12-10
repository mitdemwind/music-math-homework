from population import *
from preprocess import *
from constants import *

# write this part at last

if __name__ == "__main__":
    converter = Converter()

    # Ensure the 'data' directory exists
    if 'data' not in os.listdir('.'):
        os.mkdir('data/')

    # Example: Convert a music file to arrays and print the result
    test_melody = converter.music2arrays('test.xml')
    print("Converted Music to Arrays:")
    print(test_melody)

    # Example: Generate a population from a list of music files
    population = converter.generate_population(['test.xml'])
    print("Generated Population:")
    print(population)

    # Run the genetic algorithm for a certain number of generations
    num_generations = 5
    for generation in range(num_generations):
        print(f"Generation {generation + 1}")
        best_individual = max(population.members, key=population.fitfunc, default=None)
        if best_individual is not None:
            print(f"Best Individual: {best_individual}")
            print(f"Best Fitness: {population.fitfunc(best_individual)}")
        else:
            print("No individuals in the population.")
        print("")

        # Update the population to the next generation
        population.update()

    # Print the final population information
    print("Final Population:")
    print(population)
