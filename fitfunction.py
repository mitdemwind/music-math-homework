import numpy as np
from population import Individual
from constants import *

class FitFunction():
    def __init__(self):
        pass

    def __call__(self, music: Individual):
        # TODO
        return self._average_pitch_of_first_note(music)

    def _average_pitch_of_first_note(self, music: Individual) -> float:
        """
        Calculate the average pitch of the first note in the first measure.
        """
        first_measure = music.melody[0]
        first_note_pitch = first_measure[0]
        return np.mean(first_note_pitch)
    # need some helper functions
