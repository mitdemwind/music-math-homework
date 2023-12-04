import music21 as ms
import numpy as np
from population import *
from constants import *

# write hleper functions or classes freely when needed
# remember to name them as _example_method()
# you can change the parameters of methods begin with _

class Converter:
    """
    Class for converting data between music files and arrays
    """
    def __init__(self):
        # change this part when in need
        # TODO
        pass

    def music2arrays(self, file: str) -> np.ndarray:
        """
        Convert the given file to an numpy array
        """
        stream = ms.converter.parse(file)
        array = np.array([], dtype=np.int)
        for note in stream.flat.notes:
            pitch = note.pitch.midi
            duration = note.duration.quarterLength
            duration = (duration * 2) - 1
            array = np.append(array, pitch)
            for dur in range(duration):
                array = np.append(array, EXTEND)
        array = np.reshape(array, (-1, 8))
        """
        the array will be like:([60,-1,-1,-1,72,-1,-1,-1],
                                [56,-1,58,-1,59,68,60,60],...)
        """
        return array

    def individual2music(self, result: Individual, file_path: str) -> None:
        """
        Convert <result> to a music file, and save it in <file_path>
        """
        # TODO
        pass

    def generate_population(self, file_paths: list) -> Population:
        """
        Read the files in <file_paths> and generate a Population
        consisting of them
        """
        # TODO
        pass