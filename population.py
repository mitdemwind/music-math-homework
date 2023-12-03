import numpy as np
from constants import *

# write helper functions freely when needed
# remember to name them as _example_method()
# you can change the parameters of methods begin with _

class Individual:
    """
    Individual music fragments
    """

    def __init__(self, melody: np.ndarray, fitfunc):
        """
        Parameters:
         - melody:
          a 2d array which has the following structure:
          Each row is a measure, consisting of some notes
          the notes are represented by a pitch number (C4 as 60)
          a measure consists of 4 or 8 notes according to the beat

         - fitfunc:
          the function used to calculate adaptibilty score
        """
        try:
            self.melody = np.array(melody)
        except Exception as e:
            print("Error when casting melody to numpy array")
            print("==========")
            raise e
        self.fitfunc = fitfunc

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

    def adaptibilty(self) -> float:
        """
        Calculate the fitness score
        """
        return self.fitfunc(self.melody)

    def mutate(self) -> None:
        """
        Apply mutation on the individual
        3 kinds of mutation:
         - change a single note
         - change of rhythm
         - inversion, retrograde, transition

         Write these in different functions below
        """
        # TODO
        pass

    def _modify_random_note(self):
        """ modify a random note in the melody by some offsets """
        idx = tuple(np.random.randint(self.shape))
        self.melody[idx] += np.random.choice([-7,-5,-4,-2,2,4,5,7], 1)
        # maybe change this a little?

    # TODO
    def _change_rhythm(self):
        pass
    def _other_operations(self):
        # change this method's name or add new methods
        pass


class Population:
    """
    Population of music fragments to apply genetic algorithm
    """

    def __init__(self, fitfunc, mutate_rate: float):
        self._members = []
        self.fitfunc = fitfunc
        self.mutate_rate = mutate_rate
        self._adaptibilty = np.ndarray(map(fitfunc, self.members))

    def initialize(self, num: int) -> None:
        """
        Ramdomly construct <num> of individuals and initialize the population
        """
        # TODO
        pass

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
        idx = self._adaptibilty.argsort()[-numbers:]
        return [self._members[i] for i in idx]

    @staticmethod
    def _cross(p1: Individual, p2: Individual) -> Individual:
        """
        Generate children using two individuals
        """
        # TODO
        pass

    def cross(self) -> None:
        """
        Generate the next generation randomly
        """
        # TODO
        pass

    def mutate(self) -> None:
        """
        Apply mutation on some individuals
        """
        # TODO
        pass

    def update(self) -> None:
        """
        Update the population to the next generation
        """
        self.cross()
        self.mutate()
        self._adaptibilty = list(map(fitfunc, self._members))


# some simple tests
# you can modify this part for debugging
if __name__ == '__main__':
    a = Individual(np.array([[3, 0], [1, 1], [2, 2]]), lambda x: x[0][0], 0.1)
    print(len(a), a.adaptibilty())
    a._modifyRandom()
    print(a.melody)
