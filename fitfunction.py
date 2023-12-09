import numpy as np
from population import Individual
from constants import *

class FitFunction():
    def __init__(self):
        pass

    def __call__(self, music: Individual):
        # TODO
        return music.melody[0][0]

    # need some helper functions
