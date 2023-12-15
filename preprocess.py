import music21 as ms
import numpy as np
import os
from population import Individual, Population
from constants import *
from fitfunction import FitFunction
from utils import *

# write hleper functions or classes freely when needed
# remember to name them as _example_method()
# you can change the parameters of methods begin with _

class Converter:
    """
    Class for converting data between music files and arrays
    """
    def __init__(self):
        # change this part when in need
        pass

    def music2arrays(self, file: str) -> np.ndarray:
        """
        Convert the given file to an numpy array
        """
        stream = ms.converter.parse(DATAPATH + file)
        array = np.array([], dtype=np.int64)

        for note in stream.stripTies().flatten().notes:
            pitch = note.pitch.midi

            duration = note.duration.quarterLength
            duration = (duration * 2) - 1
            assert int(duration) == duration
            duration = int(duration)

            array = np.append(array, pitch)
            for dur in range(duration):
                array = np.append(array, EXTEND[0])

        array = np.reshape(array, (-1, 8))
        # the array will be like:[[60,-1,-1,-1,72,-1,-1,-1],
        #                         [56,-1,58,-1,59,68,60,60],...]
        return array

    def individual2music(self, result: Individual, file_path: str) -> None:
        """
        Convert <result> to a music file, and save it in <file_path>
        If file_path is an empty string, then show it instead of save it.
        """
        melody = result.melody.ravel()
        if melody.dtype in [np.int32, np.int64]:
            melody = map(to_note_str, melody)

        stream = ms.stream.Stream()
        stream.metadata = ms.metadata.Metadata()
        stream.metadata.title = 'Test'
        stream.insert(0, ms.meter.TimeSignature('4/4'))
        stream.insert(0, ms.key.Key('C'))

        for data in melody:
            if data in EXTEND:
                stream[-1].duration.quarterLength += 0.5
            else:  # add a new note
                note = ms.note.Note(data)
                note.duration.quarterLength = 0.5
                # note.volume.velocity = 64  # from 0 to 127
                # note.activeSite.instrument.midiProgram = 0  # 0 means piano
                stream.append(note)
        stream.makeNotation(inPlace=True)

        if file_path == '':
            stream.show()
        else:
            stream.write('xml', DATAPATH + file_path)

    def array2music(self, arr: np.ndarray, file_path: str) -> None:
        """
        Convert <arr> to a music file, and save it in <file_path>
        If file_path is an empty string, then show it instead of save it.

        Note that <arr> can be either array of strings or array of numbers.
        """
        self.individual2music(Individual(arr), file_path)

    def generate_population(self, file_paths: list[str]) -> Population:
        """
        Read the files in <file_paths> and generate a Population
        consisting of them
        """
        if file_paths == []:
            raise Exception("Cannot convert empty file list to population")

        members = []
        for file in file_paths:
            array = self.music2arrays(file)
            members.append(Individual(array))
        population = Population(members, FitFunction().final_evaluate, MUTATE_RATE)
        return population

if __name__ == '__main__':
    if 'data' not in os.listdir('.'):
        os.mkdir('data/')
    converter = Converter()
    test_melody = np.array([
            ['C', '', '', 'D', 'E', '', '', 'C'],
            ['E', '', 'C', '', 'E', '', '', ''],
            ['D', '', '', 'E', 'F', 'F', 'E', 'D'],
            ['F', '', '', '', '', '', '', ''],
            ['E', '', '', 'F', 'G', '', '', 'E'],
            ['', '', 'E', '', 'G', '', '', ''],
            ['F', '', '', 'G', 'A', 'A', 'G', 'F'],
            ['A', '', '', '', '', '', '', ''],
            ['G', '', '', 'C', 'D', 'E', 'F', 'G'],
            ['A', '', '', '', '', '', '', ''],
            ['A', '', '', 'D', 'E', 'F', 'G', 'A'],
            ['B', '', '', '', '', '', '', ''],
            ['B', '', '', 'E', 'F', 'G', 'A', 'B'],
            ['C5', '', '', '', '', '', 'C5', 'B'],
            ['A', '', 'F', '', 'B', '', 'G', ''],
            ['C5', '', 'G', '', 'E', '', 'D', '']])
    test_ind = Individual(test_melody)
    converter.individual2music(test_ind, 'test.xml')
    test_arr = converter.music2arrays('test.xml')
    print(test_arr)
    converter.array2music(test_arr, '')
    print(converter.generate_population(['test.xml']).adaptibilty)
