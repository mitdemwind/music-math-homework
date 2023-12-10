import numpy as np
from constants import *
from utils import *

# write helper functions freely when needed
# remember to name them as _example_method()
# you can change the parameters of methods begin with _

class Individual:
    """
    Individual music fragments
    """

    def __init__(self, melody: np.ndarray):
        """
        Parameters:
         - melody:
          a 2d array which has the following structure:
          Each row is a measure, consisting of some notes
          the notes are represented by a pitch number (C4 as 60)
          the number for extending last note is defined as EXTEND
          a measure consists of 4 or 8 notes according to the beat
        """
        try:
            self.melody = np.array(melody)
        except Exception as e:
            print("Error when casting melody to numpy array")
            print("==========")
            raise e

    def __len__(self):
        """ return the number of measures contained in this fragment """
        return self.melody.shape[0]

    @property
    def beat(self):
        """ the beat of the music, i.e. how many notes in one measure """
        return self.melody.shape[1]

    @property
    def shape(self) -> tuple:
        return self.melody.shape

    def adaptibilty(self, func: callable) -> float:
        """
        Calculate the adaptibilty score using the given function
        """
        return func(self.melody)

    def mutate(self) -> None:
        """
        Apply mutation on the individual
        Three kinds of mutation:
         1. change a note's pitch
         2. change a note's length
         3. inversion, retrograde, transition

         Write these in different functions below
        """
        # TODO: need to move the probabilty to constants.py instead of hard-code it
        mutation_prob = np.random.rand()
        if mutation_prob < 0.33:
            self._modify_random_note()
        elif 0.33 <= mutation_prob < 0.67:
            self._change_rhythm()
        else:
            self._other_operations()

    def _modify_random_note(self) -> None:
        """ Modify a random note in the melody by at most 2 scales """
        idx = tuple(np.random.randint(self.shape))
        while(self.melody[idx] == -1):
            idx = tuple(np.random.randint(self.shape))

        offset = np.random.randint(-2, 3)
        while(offset == 0):
            offset = np.random.randint(-2, 3)
        self.melody[idx] = lift(self.melody[idx], offset)

    def _change_rhythm(self) -> None:
        """
        Randomly choose a note, and make it longer or
        make the previous note shorter
        """
        idx = np.random.randint(self.melody.size)
        while(self.melody.ravel()[idx] == -1):
            idx = np.random.randint(self.melody.size)
        temp = self.melody.ravel()[idx]

        # make it shorter if possible
        choices = []
        if idx != 0:
            choices.append(1)
        if idx != self.melody.size - 1:
            choices.append(2)
        c = np.random.choice(choices)

        if c == 1:
            self.melody.ravel()[idx] = -1
            self.melody.ravel()[idx - 1] = temp
            return
        if c == 2:
            self.melody.ravel()[idx] = -1
            self.melody.ravel()[idx + 1] = temp
            return

    def _other_operations(self):
        """ Perform other types of mutations or operations on the melody """
        operation_prob = np.random.rand()

        if operation_prob < 0.33:
            self._modify_random_note()
        elif 0.33 <= operation_prob < 0.67:
            self._change_rhythm()
        else:
            self._transpose_random_measure()

    def _transpose_random_measure(self):
        # TODO
        pass


class Population:
    """
    Population of music fragments to apply genetic algorithm
    """

    def __init__(self,
            members: list[Individual],
            fitfunc: callable,
            mutate_rate: float
            ):
        """
        Parameters:
         - members:
          A list of individuals that contain music fragments
         - fitfunc:
          A function calculating adaptibilty of Individuals
         - mutate_rate:
          The probability of mutation in genetic algorithm
        """
        self._members = members
        self.fitfunc = fitfunc
        self.mutate_rate = mutate_rate
        self._adaptibilty = np.array(list(map(self.fitfunc, self._members)))

    def append(self, member: Individual):
        self._members.append(member)
        self._adaptibilty = np.append(self._adaptibilty, self.fitfunc(member), axis=0);

    def set_members(self, members: list[Individual]):
        self._members = members
        self._adaptibilty = np.array(list(map(self.fitfunc, members)))

    @property
    def members(self):
        return self._members

    def initialize(self, num: int) -> None:
        """
        Ramdomly construct <num> of individuals and initialize the population
        """
        for _ in range(num):
            # Randomly generate a melody for a new individual
            melody_length = 8  # The measure length is fixed to 8
            random_melody = C4 + np.random.choice(MAJSCALE, size=(1, melody_length))

            # Create a new Individual and add it to the population
            new_individual = Individual(random_melody)
            self.append(new_individual)

    def __len__(self):
        return len(self._members)

    def __str__(self):
        # maybe change this for debugging more conveniently
        return f'a population with {len(self)} individuals'

    @property
    def adaptibilty(self) -> np.ndarray:
        """ an 1d array consisting of the adaptibilty of each individual """
        return self._adaptibilty

    def _select_best(self, number: int) -> list[Individual]:
        """
        Select <number> of individuals with highest adaptibilty
        """
        idx = self._adaptibilty.argsort()[-number:]
        return [self._members[i] for i in idx]

    @staticmethod
    def _cross(p1: Individual, p2: Individual) -> Individual:
        """
        Generate children using two individuals
        """
        # Select a random crossover point
        crossover_point = np.random.randint(min(p1.shape[1], p2.shape[1]))

        # Create a new melody by combining genetic material from both parents
        child_melody = np.hstack([p1.melody[:, :crossover_point], p2.melody[:, crossover_point:]])

        # Create a new Individual using the combined melody
        child = Individual(child_melody)


    def cross(self) -> None:
        """
        Generate the next generation randomly
        """
        new_generation = []
        for _ in range(len(self._members) // 2):
            # Randomly select two parents
            parent1 = np.random.choice(self._members)
            parent2 = np.random.choice(self._members)
            # Generate children using crossover
            child1 = self._cross(parent1, parent2)
            child2 = self._cross(parent1, parent2)
            new_generation.extend([child1, child2])

        # Update the population with the new generation
        self._members = new_generation
        self._adaptibilty = np.array(list(map(self.fitfunc, self._members)))

    def mutate(self) -> None:
        """
        Apply mutation on some individuals
        """
        mutation_indices = np.random.rand(len(self._members)) < self.mutate_rate
        for i, mutate_flag in enumerate(mutation_indices):
            if mutate_flag:
                self._members[i].mutate()

    def update(self) -> None:
        """
        Update the population to the next generation
        """
        self.cross()
        self.mutate()
        self._adaptibilty = np.array(list(map(self.fitfunc, self._members)))


# some simple tests
# you can modify this part for debugging
if __name__ == '__main__':
    a = Individual(np.array([[3, 0], [1, 1], [2, 2]]))
    print(len(a))
    a._modify_random_note()
    print(a.melody)
    from fitfunction import FitFunction
    func = FitFunction()
    print(func(a))
