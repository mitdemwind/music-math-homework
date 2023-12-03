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
        # TODO
        pass

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
