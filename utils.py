# Write static helper functions here
import numpy as np
from constants import *


pitchname = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

complete_pitchname = ['C','#C','D','#D','E','F','#F','G','#G','A','#A','B']

adjusted = {0: 0, 1: 0, 2: 2, 3: 2, 4: 4, 5: 5, 6: 5, 7: 7,
        8: 7, 9: 9, 10: 9, 11: 11}

def to_pitchclass(midi_number: int) -> tuple[int]:
    """
    Convert a midi numder into (pitchClass, octaveNumber)
    e.g. to_pitchclass(60) == (0, 4) is the note C4
    """
    return (midi_number % 12, midi_number // 12 - 1)

def to_scaleclass(midi_number: int) -> tuple[int]:
    """
    Convert a midi numder into (pitchClass, octaveNumber)
    e.g. to_pitchclass(60) == (0, 4) is the note C4
    """
    return (MAJSCALE.index(midi_number % 12), midi_number // 12 - 1)

def to_note(scaleclass: int, octave: int) -> int:
    """
    The inverse function of to_scaleclass
    e.g. to_note(0, 4) == 60 is C4
    """
    return MAJSCALE[scaleclass] + 12 * (1 + octave)

def lift(note: int, distance: int) -> int:
    """
    Returns a new note raised by the distance
    e.g. lift(C4, 1) == D4, lift(C4, 5) == A4
    """
    pc, octave = to_scaleclass(note)
    pc += distance
    octave += pc // 7
    pc %= 7
    return to_note(pc, octave)

def to_note_str(note: int) -> str:
    """
    Convert a pitch number to the pitch name
    e.g. to_note_str(60) == 'C4'
    """
    if note == EXTEND[0]:
        return EXTEND[1]
    pc, octave = to_scaleclass(note)
    return pitchname[pc] + str(octave)

def fit_scale(note: int) -> int:
    return adjusted[note % 12] + 12 * (note // 12)

def distance(note1:int,note2:int)->int:
    """compute the distance(音程) between two notes"""
    cnt = 0
    name1, level1 = to_pitchclass(note1)
    name2, level2 = to_pitchclass(note2)
    if level1 != level2:
        cnt += (level2 - level1) * 12
    return abs(cnt + name2 - name1)

if __name__ == '__main__':
    assert lift(60, 1) == 62
    assert lift(60, 5) == 69

