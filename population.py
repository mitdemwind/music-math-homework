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

    def mutate(self, op: int) -> None:
        """
        Apply mutation on the individual
        Three kinds of mutation:
         1. change a note's pitch
         2. change a note's length
         3. inversion, retrograde, transition

         Write these in different functions below
        """
        if op == 1:
            self._modify_random_note()
            return
        if op == 2:
            self._change_rhythm()
            return
        if op == 3:
            self._other_operations()
            return
        print("Invalid option for Individual.mutate")

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

    # TODO
    def _other_operations(self):
        # change this method's name or add new methods
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
    print(func(a.melody))
