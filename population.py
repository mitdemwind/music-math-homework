class Individual():
    """
    Individual music fragments
    """

    def __init__(self, melody, fitfunc):
        self.melody = melody
        self.fitfunc = fitfunc
        self.mutate_rate = 0

    def __len__(self):
        return len(self.melody)

    def adaptibilty(self):
        """
        Calculate the fitness score
        """
        return self.fitfunc(self)

    def mutate(self):
        """
        Apply mutation on the individual
        3 kinds of mutation:
         - change a single note
         - change a segment
         - inversion, retrograde, transition
        """
        pass


class Population():
    """
    Population of music fragments to apply genetic algorithm
    """

    def __init__(self):
        self.members = []
        self._adaptibilty = []
        self.fitfunc = None
        self.mutate_rate = 0;

    def __len__(self):
        return len(self.members)

    @property
    def adaptibilty(self):
        return self._adaptibilty

    def select(self):
        """
        Select good individuals to generate children
        """
        pass

    @staticmethod
    def _cross(seg1, seg2):
        pass

    def cross(self):
        """
        Generate the children using the given parents
        """
        pass

    def mutate(self):
        """
        Apply mutation on some individuals
        """
        pass

    def update(self):
        """
        Update the population to the next generation
        """
        self.cross()
        self.mutate()

