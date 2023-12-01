import numpy as np

class Individual():
    """
    Individual music fragments
    """

    def __init__(self, melody: np.ndarray, fitfunc, mutate_rate: float):
        self.melody = melody
        # melody is a 2d array which hasthe following structure:
        #   Each row is a measure, consisting of some notes
        # the notes are represented by a pitch number
        # a measure consists of 4 or 8 notes according to the beat
        self.fitfunc = fitfunc
        self.mutate_rate = mutate_rate

    def __len__(self):
        """ return the number of measures contained in this fragment """
        return self.melody.shape[0]

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

    def _modifyRandom(self):
        """ modify a random note in the melody by some offsets """
        idx = tuple(np.random.randint(self.shape))
        self.melody[idx] += np.random.choice([-7,-5,-4,-2,2,4,5,7], 1)

    # TODO
    def _changeRhythm(self):
        pass
    def _otherOperations(self):
        """ you can change this method's name '"""
        pass


class Population():
    """
    Population of music fragments to apply genetic algorithm
    """

    def __init__(self, fitfunc, mutate_rate):
        self.members = []
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
        return len(self.members)

    @property
    def adaptibilty(self) -> np.ndarray:
        return self._adaptibilty

    def select(self, number: int) -> list[Individual]:
        """
        Select <number> of individuals with highest adaptibilty
        """
        idx = self._adaptibilty.argsort()[-numbers:]
        return [self.members[i] for i in idx]

    @staticmethod
    def _cross(frag1: Individual, frag2: Individual) -> Individual:
        """
        Generate children using two individuals
        """
        # TODO
        pass

    def cross(self) -> None:
        """
        Generate the next generation using the given parents
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
        self._adaptibilty = list(map(fitfunc, self.members))


# some simple tests
if __name__ == '__main__':
    a = Individual(np.array([[3, 0], [1, 1], [2, 2]]), lambda x: x[0][0], 0.1)
    print(len(a), a.adaptibilty())
    a._modifyRandom()
    print(a.melody)
