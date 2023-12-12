import numpy as np
from population import Individual
from constants import *

# TODO
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

    @staticmethod
    def get_duration_series(music: Individual) -> np.ndarray:
        """ Returns the duration of each note in the music """
        dur_series = []
        for note in music.melody.ravel():
            if note in EXTEND:
                dur_series.append(current_dur)
                current_dur = 0
            else:
                current_dur += 1
        dur_series.append(current_dur)

        return np.array(dur_series)

    @staticmethod
    def get_pitch_series(music.Individual) -> np.ndarray:
        """ Returns the pitch number of each note """
        mask = (music.melody != -1)
        return music.melody[mask]
